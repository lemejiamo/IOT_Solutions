 #!/usr/bin/python3

from hashlib import new
from flask import request, make_response, jsonify, render_template, flash
from api.v1.views import app_views
from models.users import User
from api.v1.app import load_user
from models import storage

@app_views.route('/sign-up', methods=['POST', 'GET'])
def new_user():
    if request.method == 'GET':
        return render_template("register.html")

    if request.method == 'POST':
        print("\n\n\n",request.form,"\n\n\n")
        data = request.form
        role = data.get('role')
        user_email = data.get('user_email')
        password = data.get('password')
        password2 = data.get('password2')
        telephone = data.get('telephone')
        campus_id = data.get("campus_id")
        company_id = data.get("company_id")
        if role not in ['1', '0']:
            flash('Invalid Role!', category="error")
        elif len(user_email) < 3 or User.get_user(user_email) is not None:
            flash('email too short or the email already exists!', category="error")
        elif password != password2 :
            flash('email doesn\'t match!', category="error")
        elif len(password) < 4:
            flash('password too short!', category="error")
        elif len(telephone) < 10:
            flash('Telephone number too short!', category="error")
        elif storage.get_one("Company", company_id) is None:
            flash('Company NIT/id doesn\'t exists!', category="error")
        elif storage.get_one("Campus", campus_id) is None:
            flash('Campus id doesn\'t exists!', category="error")
        else:
            new_user = User(**request.form)
            new_user.save()
            flash('New user acount created!', category="succes")
            return render_template("register.html")
            # make_response(jsonify({'in progres': 'in progres'}), 201)
        return render_template("register.html")

@app_views.route('/login', methods=['POST', 'GET'])
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

