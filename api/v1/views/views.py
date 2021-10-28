from hashlib import new
from flask import request, make_response, jsonify, render_template, flash
from api.v1.views import views
from models.users import User
from models import storage
from flask_login import login_required, current_user


@views.route("/user_home", methods=['GET', 'POST'])
@login_required
def home():
    print("EMAIL", current_user.user_email)
    campus = storage.get_one("Campus", current_user.campus_id)
    if request.method == 'POST':
        pass

    return render_template("user_home.html", user=current_user, devices=campus.devices, campus=campus)
