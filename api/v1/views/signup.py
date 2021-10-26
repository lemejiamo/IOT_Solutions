from flask import request, make_response, jsonify, render_template, flash
from flask.helpers import make_response
from flask.json import jsonify
from api.v1.views import app_views

@app_views.route("/signup")
def signUp():
    "return SingUp page"
    return (render_template('signup.html'))
