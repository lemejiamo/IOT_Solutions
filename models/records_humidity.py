#!/usr/bin/python3
""" holds class company"""

from sqlalchemy.sql.sqltypes import DateTime
import models
from models.base_model import IOT_Model, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Record_HUMIDITY(IOT_Model, Base):
    """Representation of a user """
    __tablename__ = 'records_HUMIDITY'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, default=1)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    measure = Column(Float, nullable=False)
    date = Column(DateTime, nullable=True)


    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)
