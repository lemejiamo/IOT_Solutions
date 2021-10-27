 #!/usr/bin/python3

from flask import request, url_for, render_template, flash, redirect
from api.v1.views import app_views, views
from models.users import User
from models import storage
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash

@app_views.route('/sign-up/user', methods=['POST', 'GET'])
def new_user():
    if request.method == 'POST':
        print("\n\n\n",request.form,"\n\n\n")
        data = request.form
        role = data.get('role')
        id = data.get('id')
        user_email = data.get('user_email')
        password = data.get('password')
        password2 = data.get('password2')
        telephone = data.get('telephone')
        campus_id = data.get("campus_id")
        company_id = data.get("company_id")
        if role not in ['1', '0']:
            flash('Invalid Role!', category="error")
        elif len(id) < 1 or storage.get_one("User", id) is not None:
            flash('Id too short or the id already exists!', category="error")
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
            # make_response(jsonify({'in progres': 'in progres'}), 201)
    return render_template("user_signup.html", user=current_user)

@app_views.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.get_user(email)
        if user:
            if User.verify_user(email, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Email does not exists!', category="error")
    return render_template("login.html", user=current_user)

@app_views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("app_views.login"))
