from flask import Blueprint, request, render_template, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from website import db
from website.forms import MealForm, ProductForm
from website.models import Product, Meal

views = Blueprint("views", __name__)

@views.route("/", methods=['GET', 'POST'])
@login_required
def home():
    
    # products = Product.query.all()
    products = db.session.query(Product.category).all()
    # print(products)
    product_category = set()
    for categories in products:
        product_category.add(categories[0])
        # print(categories[0])
    # print(product_category)
    # product1 = products[1]
    # print(product1.category)
    product_form = ProductForm()
    # product_form.category.choices = [(product.category) for product in Product.query.all()]
    # print(set(product_form.category.choices))
    return render_template("home.html", product_form = product_form, product_category = product_category)


@views.route("/add-product", methods=['POST'])
@login_required
def addProduct():
    product_form = ProductForm()
    if request.method == 'POST':
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
        return redirect(url_for('views.home'))
    flash("Product could not be added. Please try again.", category='danger')
    return redirect(url_for('views.home'))


@views.route("/add-meal", methods=['POST'])
@login_required
def addMeal():
    # product = Product.query.filter_by(id=id).first()
    
    # form = MealForm()
    meal_type = request.form.get('meal_type')
    kat = request.form.get('category')
    prod = request.form.get('product')
    weight = request.form.get('weight')

    new_meal = Meal(meal_type = meal_type, product_id = prod, weight = weight, user_id = current_user.id)
    db.session.add(new_meal)
    db.session.commit()
    # print("posiłek", meal_type)
    # print("kategoria", kat)
    # print("id", prod)
    # print("weight", weight)
    flash("Meal added!", category='success')
    return redirect(url_for("views.home"))


# @views.route("/test")
# def test():
#     products = db.session.query(Product.category).all()
#     product_category = set()
#     for categories in products:
#         product_category.add(categories[0])
#     print(product_category)
#     product_form = ProductForm()
#     return render_template("test.html", product_form = product_form, product_category = product_category)


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
    