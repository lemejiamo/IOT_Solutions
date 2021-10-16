#!/usr/bin/python3

from api.v1.views import app_views
from flask import Flask, render_template
from flask import request, jsonify, make_response
from flask_login import LoginManager
from models import storage
from models.users import User

# -------------------------FLASK SERVER SETUP---------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = '8rf5hETrkva_VbldXZikOP0BCpUbp5HimP2LUdBfJXaVjvKh-dFcSZNNpIT6aM_EkosyLTmFdT3_39vopJ9oYw'


# -------------------------BLUEPRINTS POINTS---------------------------
app.register_blueprint(app_views)


# -------------------------LOGIN MANAGER SETUP---------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ------------------------- METHODS ---------------------------

@login_manager.user_loader
def load_user(user_email):
    return User.get_user(user_email)

#@login_manager.user_login
#def user_login(user_obj):
#   return login_user(user_obj)


#@app.teardown_appcontext
#def close_db(error):
#   """ Close Storage """
#   storage.close_session()

@app.errorhandler(404)
def resource_not_found(e): #  Talk About it with the peers
    """page not found"""
    msg = {"error": "Not found"}
    return make_response(jsonify(msg), 404)


@app.route("/")
def home():
    """Home view"""
    return render_template('home.html')

# ------------------------- SERVER START ---------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
