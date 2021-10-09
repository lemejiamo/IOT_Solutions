#!/usr/bin/python3

import models
from datetime import datetime
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
# |-------------------------- '' --------------------------|

# |-------------------------- PRIVATE DATA LISTS --------------------------|


Base = declarative_base()

DATA_MODELS = {
    'Company': ['uuid_id', 'created_at', 'NIT', 'name', 'telephone', 'email', 'address'],
    'locations': ['uuid_id', 'created_at', 'locations'],
    'devices': ['uuid_id', 'created_at', 'device_id', 'company_id', 'sede', 'area', 'locations', 'magnitude'],
    'User': ['uuid_id', 'created_at', 'user_email', 'password', 'company_id', 'campus'],
    'records': ['uuid_id', 'created_at', 'measure', 'date', 'id', 'identifier']
}
class IOT_Model:
    uuid_id = Column(String(128), primary_key=True, default=uuid.uuid4())
    created_at = Column(DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        """
            CONSTRUCTOR FOR BASE MODEL
        """

        __class = self.__class__.__name__
        if __class in DATA_MODELS:
            attributes = DATA_MODELS[__class]
            for key, value  in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def save(self):
        models.storage.save(self)
