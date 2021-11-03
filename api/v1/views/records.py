#!/usr/bin/python3
"""Module to mannage RECORDS endpoints """


from flask import request, make_response, jsonify, render_template, flash
from flask.helpers import make_response
from flask.json import jsonify
from models.devices import Device
from models.records_humidity import Record_HUMIDITY
from models.records_temp import Record_TEMP
from api.v1.views import app_views, views
from models.base_model import CLASS_MODELS
from models import storage
from flask_login import current_user

# |------------------------- REGISTER A NEW DEVICE ------------------------|
@views.route('/sign-up/device', methods=['GET', 'POST'])
def registry_device():
    """method to create new device-object in DB"""
    # |------------------- POST -------------------|
    if request.method == 'POST':
        data = request.form
        id = data.get("id")
        campus_id = data.get("campus_id")

        if len(id) < 1:
            flash('Please put an Id!', category="error")
        elif len(campus_id) < 1:
            flash('Please put a campus id!', category="error")
        elif storage.get_one("Device", id) is not None:
            flash('Device id already exists!', category="error")
        elif storage.get_one("Campus", campus_id) is None:
            flash('Campus doesn\'t exists!', category="error")
        else:
            device = Device(**data)
            device.save()
            flash('New device created!', category="succes")
            #return make_response(jsonify({'Succes ': 'Device created in DB'}), 201)
    return render_template("device_signup.html", user=current_user)

# |------------------------- RECORD A TEMP MEASURE ------------------------|
@app_views.route('/records/temp', methods=['POST'])
def record_temp():
    """Saves a Record in DB"""

    if not request.get_json():
        return (make_response(jsonify({'bad_request': 'not a json'})))

    json = request.get_json()
    # mandatory json Keys are 'device_id' and 'measure'
    # date key is not configured yet

    if 'device_id' not in json:
        return (make_response(jsonify({'bad_request': 'not device id'})))

    elif storage.get_one('Device', int(json['device_id'])) is None:
        return (make_response(jsonify({'bad_request': 'Device not exists'})))

    elif 'measure' not in json:
        return (make_response(jsonify({'bad_request': 'not Measure Report'})))

    record = Record_TEMP(**json)
    response = ''
    if record.alert(record):
        response  = (make_response(jsonify({'succes': 'record save in DB', 'alert':'Measure over average'})))
    else:
        response = (make_response(jsonify({'succes': 'record save in DB'})))

    record.save()
    return (response)

# |------------------------- RECORD A HUMIDITY MEASURE ------------------------|
@app_views.route('/records/humidity', methods=['POST'])
def record_humidity():
    """Saves a Record in DB"""

    if not request.get_json():
        return (make_response(jsonify({'bad_request': 'not a json'})))

    json = request.get_json()
    # mandatory json Keys are 'device_id' and 'measure'
    # date key is not configured yet

    if 'device_id' not in json:
        return (make_response(jsonify({'bad_request': 'not device id'})))

    elif storage.get_one('Device', int(json['device_id'])) is None:
        return (make_response(jsonify({'bad_request': 'Device not exists'})))

    elif 'measure' not in json:
        return (make_response(jsonify({'bad_request': 'not Measure Report'})))

    record = Record_TEMP(**json)
    response = ''
    if record.alert(record):
        response  = (make_response(jsonify({'succes': 'record save in DB', 'alert':'Measure over average'})))
    else:
        response = (make_response(jsonify({'succes': 'record save in DB'})))

    record.save()
    return (response)
