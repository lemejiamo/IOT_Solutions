#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import IOT_Model, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
import hashlib


class User(IOT_Model, Base):
    """Representation of a user """

    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.NIT'), nullable=False)
    campus_id = Column(Integer, ForeignKey('campus.campus_id'), nullable=False)
    user_email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    telephone = Column(Integer, nullable=False)
    #rol = Column(Boolean, default=False)

    def __init__(self, **kwargs):
        """initializes user"""
        hasher = hashlib.sha256()
        hash =  kwargs['password']
        hasher.update(hash.encode())
        kwargs['password'] = hasher.hexdigest()

        super().__init__(**kwargs)
