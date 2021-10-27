from hashlib import new
from flask import request, make_response, jsonify, render_template, flash
from api.v1.views import views
from models.users import User
from models import storage
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash


@views.route("/home_user", methods=['GET', 'POST'])
@login_required
def home():
    print(current_user.__dict__)
    return jsonify("WELCOME")
