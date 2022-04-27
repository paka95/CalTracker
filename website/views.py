from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/", methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html")


@views.route("/test")
def test():
    return render_template("test.html")