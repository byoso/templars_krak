from flask import render_template, request, url_for, redirect, flash
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from flask_admin import Admin, AdminIndexView

from app import app
from app.users.models import User
from app import db
from . import admin


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, *args, **kwargs):
        flash("You are not allowed to access admin mode.")
        return redirect(url_for("users.login"))


class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, *args, **kwargs):
        flash("You are not allowed to access admin mode.")
        return redirect(url_for("users.login"))



admin = Admin(app, index_view=CustomAdminIndexView())
admin.add_view(AdminView(User, db.session))
