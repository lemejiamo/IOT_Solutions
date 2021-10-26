#!/usr/bin/python3
""" Module campus: campus views"""

from flask import request, make_response, jsonify, render_template, flash
from flask.helpers import make_response
from flask.json import jsonify
from api.v1.views import app_views
from models.base_model import CLASS_MODELS
from models import storage
from models.campus import Campus

@app_views.route("/sign-up/campus", methods=['GET', 'POST'])
def signUpcampus():
    """method to create new campus-object in DB"""
    # |------------------- GET -------------------|
    if request.method == 'GET':
        return (render_template('campus_signup.html'))

    # |------------------- POST -------------------|
    if request.method == 'POST':
        campus = Campus(**request.form)
        campus.save()
        return make_response(jsonify({'Succes ': 'Campus created in DB'}), 201)
