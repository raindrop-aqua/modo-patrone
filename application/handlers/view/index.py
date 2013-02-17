# -*- coding: utf-8 -*-

from flask import Module, render_template

index_view = Module(__name__)


@index_view.route("/")
def index():
    return render_template("index.html")
