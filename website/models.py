from . import db
from datetime import date, datetime
from flask_login import UserMixin
from flask import current_app
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    meal = db.relationship('Meal', backref='user', lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    maker = db.Column(db.String(50), nullable = True)
    proteins = db.Column(db.Float, nullable = False)
    fats = db.Column(db.Float, nullable = False)
    carbohydrates = db.Column(db.Float, nullable = False)
    kcal = db.Column(db.Float, nullable = False)
    # of_meal = db.Column(db.Integer, db.ForeignKey('meal.id', ondelete="CASCADE"), nullable = False)
    of_meal = db.relationship('Meal', backref='product', lazy=True)


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_type = db.Column(db.String(20), nullable = False)
    weight = db.Column(db.Float, nullable = False)
    date_added = db.Column(db.DateTime(timezone=True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    # product = db.relationship('Product', backref='meal', lazy=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete="CASCADE"), nullable=False)
