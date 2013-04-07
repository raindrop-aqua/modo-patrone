# -*- coding: utf-8 -*-

from application.forms.author import CreateForm
from flask import Module, render_template

author_view = Module(__name__)

@author_view.route("/author")
def author_index():
    return render_template("/author/index.html")

@author_view.route("/author/<author_id>")
def author_detail(author_id):
    return author_id

@author_view.route("/author/signin", methods=["POST"])
def author_signin():
    return "YES"

@author_view.route("/author/create", methods=["GET"])
def get_create_author():
    form = CreateForm(csrf_enabled=False)
    return render_template("/author/create.html", form=form)

@author_view.route("/author/create", methods=["POST"])
def post_create_author():
    return render_template("author/create.html")

