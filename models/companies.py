#!/usr/bin/python3
""" holds class company"""

import models
from models.base_model import IOT_Model, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Company(IOT_Model, Base):
    """Representation of a user """
    __tablename__ = 'companies'
    NIT = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    telephone = Column(Integer,  nullable=False)
    email = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    user = relationship('User')

    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)
