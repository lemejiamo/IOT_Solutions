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

CLASS_MODELS = {
    'Company': ['uuid_id', 'created_at', 'NIT', 'name', 'telephone', 'email', 'address', 'id'],
    'User': ['uuid_id', 'created_at', 'id', 'user_email', 'password', 'company_id', 'campus_id', 'telephone'],  #  rol es un booleano, en caso de verdadero es gerente en caso de falgo es usuario estandar campus_id foreging key from campus
    'Campus': ['uuid_id', 'created_at', 'id', 'company_id', 'name'], #  company foreging key from companies restaurante 1
    'Location': ['uuid_id', 'created_at', 'id', 'name'], #  numero de nevera company foreging key from companies
    'Device': ['uuid_id', 'created_at', 'id', 'campus_id', 'location', 'machine'],
    'Record_HUMIDITY': ['uuid_id', 'created_at', 'measure', 'date', 'device_id'], #  device:id foreging key from devices
    'Record_TEMP': ['uuid_id', 'created_at', 'measure', 'date', 'device_id'] #  device:id foreging key from devices
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
        if __class in CLASS_MODELS:
            attributes = CLASS_MODELS[__class]
            for key, value  in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def save(self):
        models.storage.save(self)
