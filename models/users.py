#!/usr/bin/python3
""" holds class User"""

from sqlalchemy.orm import relationship
from models.base_model import IOT_Model, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
import hashlib


class User(IOT_Model, Base, UserMixin):
    """Representation of a user """

    __tablename__ = 'users'
    id = Column(String(128), primary_key=True, unique=True)
    company_id = Column(String(128), ForeignKey('companies.NIT'), nullable=False)
    campus_id = Column(String(128), ForeignKey('campus.id'), nullable=False)
    user_email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    telephone = Column(String(128), nullable=False)
    rol = Column(Boolean, default=0)
    # records_TEMP = relationship('Record_TEMP',
    #                             backref='users')
    # records_HUMIDITY = relationship('Record_HUMIDITY',
    #                                 backref='users')

    def __init__(self, **kwargs):
        """initializes user"""
        hash = User.set_passwd(kwargs['password'])
        kwargs['password'] = hash
        super().__init__(**kwargs)


    @staticmethod
    def set_passwd(password):
        hasher = hashlib.sha256()
        hash =  password
        hasher.update(hash.encode())
        password = hasher.hexdigest()
        return password


    @staticmethod
    def get_user(email):
        """ obtain a user from DB"""
        """returns the user object from given email in the DB"""
        from models import storage
        dict_objects = storage.get_objects('User')
        for key, value in dict_objects.items():
            obj = value
            obj_email = obj.__dict__['user_email']
            if obj_email == email:
                return (obj)
        return None

    @staticmethod
    def verify_user(user_email: str, password: str):
        """ veriffica si el usuario existe y si el pass es correcto"""
        user = User.get_user(user_email)
        if user:
            obj_dict = user.__dict__
            passwd = User.set_passwd(password)
            if passwd == obj_dict['password']:
                return user
        else:
            return None
