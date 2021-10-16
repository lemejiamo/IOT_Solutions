#!/usr/bin/python3
"""Module to mannage RECORDS endpoints """


from flask import request, make_response, jsonify, render_template, flash
from flask.helpers import make_response
from flask.json import jsonify
from models.devices import Device
from models.records_humidity import Record_HUMIDITY
from models.records_temp import Record_TEMP
from api.v1.views import app_views
from models.base_model import CLASS_MODELS
from models import storage

# |------------------------- REGISTER A NEW DEVICE ------------------------|
@app_views.route('/device/register', methods=['GET', 'POST'])
def registry_device():
    """method to create new device-object in DB"""
    # |------------------- GET -------------------|
    if request.method == 'GET':
        return (render_template('register_device.html'))

    # |------------------- POST -------------------|
    if request.method == 'POST':
        device = Device(**request.form)
        device.save()
        return make_response(jsonify({'Succes ': 'Device created in DB'}), 201)

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
    elif storage.get_one('Device', json['device_id']) is None:
        return (make_response(jsonify({'bad_request': 'Device not exists'})))
    elif 'measure' not in json:
        return (make_response(jsonify({'bad_request': 'not Measure Report'})))

    record = Record_TEMP(**json)
    record.save()

    return (make_response(jsonify({'succes': 'record save in DB'})))


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
        return (make_response(jsonify({'bad_request': 'not device id report'})))
    elif storage.get_one('Device', json['device_id']) is None:
        return (make_response(jsonify({'bad_request': 'Device not exists'})))
    elif 'measure' not in json:
        return (make_response(jsonify({'bad_request': 'not measure report'})))

    record = Record_HUMIDITY(**json)
    record.save()

    return (make_response(jsonify({'succes': 'record save in DB'})))

