#!/usr/bin/python3

from flask import Blueprint

app_records = Blueprint('app_records', __name__, url_prefix='/api/v1/')

from api.v1.records.users import *

