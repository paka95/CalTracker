from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from website.forms import RegisterForm, LoginForm
from website.models import User
from website import bcrypt, db


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f"User {current_user.email} logged in!", category='success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('views.index'))
        else:
            flash('Wrong credentials. Please try again.', category='danger')
            return redirect(url_for('auth.login'))
    return render_template("login.html", form = form)


@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('User registered!', category='success')
        return redirect(url_for('auth.login'))
    return render_template("register.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out!', category='success')
    return redirect(url_for('auth.login'))