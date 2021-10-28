#!/usr/bin/python3
""" Module campus: campus views"""

from flask import request, make_response, jsonify, render_template, flash
from flask.helpers import make_response
from flask.json import jsonify
from api.v1.views import app_views
from models.base_model import CLASS_MODELS
from models import storage
from models.campus import Campus
from flask_login import current_user

@app_views.route("/sign-up/campus", methods=['GET', 'POST'])
def signUpcampus():
    """method to create new campus-object in DB"""
    # |------------------- POST -------------------|
    if request.method == 'POST':
        data = request.form
        id = data.get("id")
        company_id = data.get("company_id")
        if len(id) < 1:
            flash('Please put an Id!', category="error")
        elif len(company_id) < 1:
            flash('Please put a company id!', category="error")
        elif storage.get_one("Campus", id) is not None:
            flash('Campus id already exists!', category="error")
        elif storage.get_one("Company", company_id) is None:
            flash('Company NIT/id doesn\'t exists!', category="error")
        else:
            campus = Campus(**data)
            campus.save()
            flash('New campus created!', category="succes")
    return render_template("campus_signup.html", user=current_user)
