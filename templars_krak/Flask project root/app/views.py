#! /usr/bin/env python3
# -*- coding : utf-8 -*-

from flask import request, render_template, redirect, flash, url_for
from werkzeug.urls import url_parse

from app import app
from flask_login import current_user, login_required
from app.users.models import User


@app.route("/")
@login_required
def index():
    return render_template("index.html")
