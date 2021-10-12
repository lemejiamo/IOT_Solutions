#!/usr/bin/python3
""" holds class campus"""

from models.base_model import IOT_Model, Base
import models
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Campus(IOT_Model, Base):
    """Representation of a campus """

    __tablename__ = 'campus'
    campus_id = Column(Integer, primary_key=True, unique=True)
    company_id = Column(Integer, ForeignKey('companies.NIT'), nullable=False)
    name = Column(String(128), nullable=False)
    users = relationship("User",
                         backref='campus')
    users = relationship("Device",
                         backref='campus')


    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)
