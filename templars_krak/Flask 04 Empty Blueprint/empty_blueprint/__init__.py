from flask import Blueprint


new_bp = Blueprint(
    "new_bp",
    __name__,
    static_folder="static",
    template_folder="templates"
)

from . import views
