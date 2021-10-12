#!/usr/bin/python3

from api.v1.records import app_records
from flask import Flask, render_template
from flask import request, jsonify, make_response
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.register_blueprint(app_records)

# login_manager = LoginManager(app)

@app.errorhandler(404)
def resource_not_found(e): #  Talk About it with the peers
    """page not found"""
    msg = {"error": "Not found"}
    return make_response(jsonify(msg), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
