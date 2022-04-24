from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/register")
def register():
    return render_template("register.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out!', category='success')
    return redirect(url_for('auth.login'))