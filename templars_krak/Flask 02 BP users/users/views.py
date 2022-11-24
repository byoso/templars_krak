from datetime import datetime

from flask import request, render_template, redirect, flash, url_for
from werkzeug.urls import url_parse

from app import db
from .forms import LoginForm, SignInForm
from app import app
from flask_login import current_user, login_user, logout_user
from .models import User

from . import users


@users.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('users.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    context = {
        "form": form,
    }
    return render_template("users/login.html", **context)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@users.route("/sign_in", methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignInForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data
            )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successfully done.")
        return redirect(url_for('users.login'))
    return render_template("users/sign_in.html", title="Sign in", form=form)
