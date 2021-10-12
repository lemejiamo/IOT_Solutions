#!/usr/bin/python3
""" holds class company"""

import models
from models.base_model import IOT_Model, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Device(IOT_Model, Base):
    """Representation of a user """
    __tablename__ = 'devices'
    device_id = Column(Integer, primary_key=True, autoincrement=True)
    campus_id = Column(Integer, ForeignKey('campus.campus_id'), nullable=False)
    area = Column(String(50), nullable=False)
    location = Column(String(50), nullable=False)
    TEMP = relationship('Record_TEMP',
                        backref='devices')
    HUMIDITY = relationship('Record_HUMIDITY',
                            backref='devices')


    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)
