#!/usr/bin/python3

import models
from datetime import datetime
from os import getenv
import sqlalchemy
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import uuid
# |-------------------------- '' --------------------------|

# |-------------------------- PRIVATE DATA LISTS --------------------------|


Base = declarative_base()

DATA_MODELS = {
    'Company': ['uuid_id', 'created_at', 'NIT', 'name', 'telephone', 'email', 'address'],
    'User': ['uuid_id', 'created_at', 'user_id', 'user_email', 'password', 'company_id', 'campus_id', 'telephone'],  #  rol es un booleano, en caso de verdadero es gerente en caso de falgo es usuario estandar campus_id foreging key from campus
    'Campus': ['uuid_id', 'created_at', 'campus_id', 'company_id', 'name'], #  company foreging key from companies restaurante 1
    #'areas': ['uuid_id', 'created_at', 'campus_id', 'area_id', 'name'], # area cocina
    #'locations': ['uuid_id', 'created_at', 'area_id', 'location_id', 'location_name'], #  numero de nevera company foreging key from companies
    'Device': ['uuid_id', 'created_at', 'device_id', 'campus_id', 'area', 'location'],
    'Records_HUMIDITY': ['uuid_id', 'created_at', 'measure', 'date', 'device_id'], #  device:id foreging key from devices
    'Records_TEMP': ['uuid_id', 'created_at', 'measure', 'date', 'device_id'] #  device:id foreging key from devices
}
class IOT_Model:
    uuid_id = Column(String(128), primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        """
            CONSTRUCTOR FOR BASE MODEL
        """

        __class = self.__class__.__name__
        print (__class)
        if __class in DATA_MODELS:
            attributes = DATA_MODELS[__class]
            for key, value  in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def save(self):
        models.storage.save(self)
