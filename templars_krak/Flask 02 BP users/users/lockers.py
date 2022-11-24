from functools import wraps

from flask import request, current_app, abort

from flask_login import current_user
from flask_login.config import EXEMPT_METHODS


def roles_check(and_roles: list=[], or_roles:list =[]):
    """Same purpose as the 'roles_required' decorator,
    in a function verison"""
    if request.method in EXEMPT_METHODS or current_app.config.get("LOGIN_DISABLED"):
        pass
    elif not current_user.is_authenticated:
        abort(403)

    # roles checking
    print(current_user)
    print(current_user.roles.all())
    print(f"and: {and_roles}, or: {or_roles}")
    if and_roles:
        perms = [current_user.has_role(role) for role in and_roles]
        if not all(perms):
            abort(403)

    if or_roles:
        perms = [current_user.has_role(role) for role in or_roles]
        if not any(perms):
            abort(403)
    return True




def roles_required(and_roles: list=[], or_roles:list =[]):
    """
    Decorator, use it to lock views, roles are the keys:

    or_roles: if the user has one of this roles -> authorized
    and_roles: the user must have all this roles to be authorized

    """
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method in EXEMPT_METHODS or current_app.config.get("LOGIN_DISABLED"):
                pass
            elif not current_user.is_authenticated:
                abort(403)

            # roles checking
            if and_roles:
                perms = [current_user.has_role(role) for role in and_roles]
                if not all(perms):
                    abort(403)

            if or_roles:
                perms = [current_user.has_role(role) for role in or_roles]
                if not any(perms):
                    abort(403)

            # flask 1.x compatibility
            # current_app.ensure_sync is only available in Flask >= 2.0
            if callable(getattr(current_app, "ensure_sync", None)):
                return current_app.ensure_sync(func)(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper
    return deco
