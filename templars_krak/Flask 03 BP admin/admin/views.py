from flask import request, url_for, redirect, flash
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView
from flask_login import current_user

from . import admin
from app import app, db
from app.users.models import User, Role


class AdminView(ModelView):
    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        return current_user.has_role("admin")
        # return True

    def inaccessible_callback(self, *args, **kwargs):
        flash("You are not allowed to access admin mode.")
        return redirect(url_for("users.login"))


class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        return current_user.has_role("admin")
        # return True

    def inaccessible_callback(self, *args, **kwargs):
        flash("You are not allowed to access admin mode.")
        return redirect(url_for("users.login"))



admin = Admin(app, index_view=CustomAdminIndexView())
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))
