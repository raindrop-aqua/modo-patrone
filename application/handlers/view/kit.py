# -*- coding: utf-8 -*-

from flask import Module, render_template, redirect
from application.models import kit

kit_view = Module(__name__)

@kit_view.route("/kit")
@kit_view.route("/kit/search")
def kit_search():
    return render_template("/kit/index.html", kits=kit.search())


@kit_view.route("/kit/<kit_id>")
def kit_detail(kit_id):
    kit_data = kit.read(kit_id)
    if kit_data:
        return render_template("/kit/detail.html", kit=kit_data)
    else:
        return redirect("/kit")