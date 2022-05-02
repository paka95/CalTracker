from flask import Blueprint, request, render_template, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from website import db
from website.forms import MealForm, ProductForm
from website.models import Product, Meal
from sqlalchemy.sql import func
from datetime import datetime

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def index():
    todays_date = datetime.now()
    todays_date_formatted = todays_date.strftime("%Y-%m-%d")
    return redirect(url_for('views.home', meal_date = todays_date_formatted))



@views.route("/<meal_date>", methods=['GET', 'POST'])
@login_required
def home(meal_date):
    todays_date = datetime.now()
    todays_date_formatted = todays_date.strftime("%Y-%m-%d")
    meals = Meal.query.filter(func.date(Meal.date_added) == meal_date).filter(Meal.user_id == current_user.id).all()

    proteins_total = 0
    carbs_total = 0
    fats_total = 0
    kcal_total = 0
    weight_total = 0

    for m in meals:
        proteins_total = proteins_total + m.proteins
        carbs_total = carbs_total + m.carbohydrates
        fats_total = fats_total + m.fats
        kcal_total = kcal_total + m.kcal
        weight_total = weight_total + m.weight
        print(f"{m.product.name}", m.meal_type)

    products = db.session.query(Product.category).all()

    product_category = set()
    for categories in products:
        product_category.add(categories[0])

    product_form = ProductForm()

    if request.method == 'POST':
        date_specified = request.form.get('date_picker_date')
        return redirect(url_for('views.home', meal_date = date_specified))
    return render_template("home.html", product_form = product_form, product_category = product_category, meals = meals, proteins_total = proteins_total, carbs_total = carbs_total, fats_total = fats_total, kcal_total = kcal_total, weight_total = weight_total, meal_date = meal_date)


@views.route("/add-product", methods=['POST'])
@login_required
def addProduct():
    product_form = ProductForm()
    if request.method == 'POST':
        date_specified = request.form.get('date_picker_date')
        category = request.form.get('cat')
        name = request.form.get('name')
        maker = request.form['maker']
        proteins = request.form.get('proteins')
        proteins = float(proteins)
        carbs = request.form.get('carbs')
        carbs = float(carbs)
        fats = request.form.get('fats')
        fats = float(fats)
        kcal = request.form.get('kcal')
        kcal = float(kcal)

        new_product = Product(category = category, name = name, maker = maker, proteins = proteins, carbohydrates = carbs, fats = fats, kcal = kcal)

        db.session.add(new_product)
        db.session.commit()
        flash("Product added!", category="success")
        return redirect(url_for('views.home', meal_date = date_specified))
    flash("Product could not be added. Please try again.", category='danger')
    return redirect(url_for('views.home', meal_date = date_specified))


@views.route("/add-meal", methods=['POST'])
@login_required
def addMeal():
    date_specified = request.form.get('date_picker_date')
    meal_type = request.form.get('meal_type')
    kat = request.form.get('category')
    prod = request.form.get('product') #id produktu
    weight = request.form.get('weight')

    product = Product.query.filter_by(id=prod).first()

    new_meal = Meal(meal_type = meal_type, product_id = prod, weight = weight, date_added = date_specified, user_id = current_user.id, kcal = (float(weight)/100)*product.kcal, proteins = (float(weight)/100)*product.proteins, carbohydrates = (float(weight)/100)*product.carbohydrates, fats = (float(weight)/100)*product.fats)

    db.session.add(new_meal)
    db.session.commit()

    flash("Meal added!", category='success')
    return redirect(url_for("views.home", meal_date = date_specified))


@views.route("/change-meal/<id>", methods=['GET', 'POST'])
@login_required
def change(id):
    meal = Meal.query.filter_by(id = id).first()
    specified_date = request.form.get('date_picker_date')

    if not meal:
        flash("No meal found", category="danger")
    else:
        # category = request.form.get('category26')
        product = request.form.get('product26')
        weight = request.form.get('weight_updated')
        updated_meal_type = request.form.get('updated_meal_type')
        if product == None:
            meal.product_id = meal.product_id
        else:
            meal.product_id = product
        
        if weight == None:
            meal.weight = meal.weight
        else:
            meal.weight = weight
        # if updated_meal_type == None:
        #     meal.meal_type = meal.meal_type
        # else:
        #     meal.meal_type = updated_meal_type
        # print("Category:", category)
        db.session.commit()
        print("Product:", product)
        print("Weight:", weight)
        flash('Meal updated', category='success')
        return redirect(url_for('views.home', meal_date = specified_date))
    return redirect(url_for('views.home', meal_date = specified_date))


@views.route("/delete-meal/<id>", methods=['POST'])
@login_required
def delete_meal(id):
    date_specified = request.form.get('date_picker_date')
    meal = Meal.query.filter_by(id=id).first()
    db.session.delete(meal)
    db.session.commit()
    flash('Meal deleted', category='info')
    return redirect(url_for('views.home', meal_date = date_specified))


@views.route("/test")
def test():
    meals = Meal.query.filter(func.date(Meal.date_added) == '2022-04-30').filter(Meal.user_id == current_user.id).all()
    # print("meal1:", meals[0].product_id)
    # print("meal2:", meals[1].product_id)
    # new_meal = Meal.query.filter_by(id=2).first()
    for meal in meals:
        print("name:", meal.product.name)
        print("kcal:", meal.product.kcal)
        print("proteins:", meal.product.proteins)
        print("fats:", meal.product.fats)
        print()
        # weight = meal.weight
        # new_product = Product.query.filter_by(id=meal.product_id).first()
        # kcal = (weight/100) * new_product.kcal
        # bialko = (weight/100) * new_product.proteins
        # wegle = (weight/100) * new_product.carbohydrates
        # tluszcze = (weight/100) * new_product.fats
        # print(f"{new_product.name} kcal: ", "{:.2f}".format(kcal))
        # print(f"{new_product.name} bialko: ", bialko)
        # print(f"{new_product.name} wegle: ", wegle)
        # print(f"{new_product.name} tluszcze: ", tluszcze)
        # print(new_meal.product_id)
    return render_template("test.html")


@views.route("/category/<cat>")
def get_cat(cat):
    products = Product.query.filter_by(category=cat).all()
    prod_list = []
    listofdict = []
    

    # print(jsonify(products))

    for prod in products:
        product = {}
        product['name'] = prod.name
        product['id'] = prod.id
        # print("name:", prod.name)
        # print("id:", prod.id)
        # print(product)
        listofdict.append(product)
        prod_list.append(prod.name)
    # print(product)
    print("list of dict:", listofdict)
    print("prod list:", prod_list)
    
    return jsonify(listofdict)
    