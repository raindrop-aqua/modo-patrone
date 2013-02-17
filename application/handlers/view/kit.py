# -*- coding: utf-8 -*-

from application.models import kit
from flask import Module, render_template


kit_view = Module(__name__)

@kit_view.route("/kit")
@kit_view.route("/kit/search")
def kit_search():
    return render_template("/kit/search.html", kits=kit.search())


@kit_view.route("/kit/<kit_id>")
def kit_detail(kit_id):
    return render_template("/kit/detail.html")