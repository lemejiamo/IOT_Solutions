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
    'User': ['uuid_id', 'created_at', 'id', 'user_email', 'password', 'company_id', 'campus_id', 'telephone', 'rol'],
    'Campus': ['uuid_id', 'created_at', 'id', 'company_id', 'name'],
    'Area': ['uuid_id', 'created_at', 'id', 'name'],
    'Device': ['uuid_id', 'created_at', 'id', 'campus_id', 'location', 'area'],
    'Record_HUMIDITY': ['uuid_id', 'created_at', 'measure', 'date', 'device_id', 'user_id'],
    'Record_TEMP': ['uuid_id', 'created_at', 'measure', 'date', 'device_id', 'user_id']
}
class IOT_Model:
    uuid_id = Column(String(128),  unique=True)
    created_at = Column(DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        """
            CONSTRUCTOR FOR BASE MODEL
        """
        uuid_id = uuid.uuid4()
        uuid_id = str(uuid_id)
        setattr(self, 'uuid_id', uuid_id)
        self._to_dict = {}
        __class = self.__class__.__name__

        if __class in CLASS_MODELS:
            attributes = CLASS_MODELS[__class]
            for key, value  in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
                    if key != 'password':
                        self._to_dict[key] = value
            print(self._to_dict)

    def save(self):
        models.storage.save(self)

