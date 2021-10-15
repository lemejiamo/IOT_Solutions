 #!/usr/bin/python3

from flask import request, make_response, jsonify, render_template
from api.v1.views import app_views
from models.users import User
from api.v1.app import load_user

@app_views.route('/users/register', methods=['POST', 'GET'])
def new_user():
    if request.method == 'GET':
        return render_template("register.html")

    if request.method == 'POST':
        new_user = User(**request.form)
        new_user.save()
        return make_response(jsonify({'in progres': 'in progres'}), 201)

@app_views.route('/users/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        # verificar  el contenido del al peticion
        # si existe el formulario
        # retorna error, redirecciona a pagina de error

        email = request.form['email']
        password = request.form['password']

        user = User.verify_user(email, password)
        if user:
            # user_login(user)
            return ("Welcome") #redireccionar a la pagina correspondiente
        else:
            return ("User or Password Invalid")

