from flask import render_template

from . import new_bp


@new_bp.route("/some_route")
def some_view():
    return render_template("new_bp/some_html.html")
