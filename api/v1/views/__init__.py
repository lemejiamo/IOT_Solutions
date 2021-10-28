#!/usr/bin/python3

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
views = Blueprint('views', __name__,)

from api.v1.views.signup import *
from api.v1.views.users import *
from api.v1.views.records import *
from api.v1.views.campus import *
from api.v1.views.companies import *
from api.v1.views.views import *

