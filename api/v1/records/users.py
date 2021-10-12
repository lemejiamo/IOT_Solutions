#!/usr/bin/python3

from flask import request, make_response, jsonify, render_template
from api.v1.records import app_records
from models.users import User

@app_records.route('/users/register', methods=['POST', 'GET'])
def new_user():
    if request.method == 'GET':
        return render_template("register.html")

    if request.method == 'POST':
        new_user = User(**request.form)
        new_user.save()
        return make_response(jsonify({'in progres': 'in progres'}), 201)

@app_records.route('/users/login', methods=['POST', 'GET'])
def session_maker():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return (email)

