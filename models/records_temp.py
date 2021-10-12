#!/usr/bin/python3
""" holds class company"""

from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import DateTime
import models
from models.base_model import IOT_Model, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Record_TEMP(IOT_Model, Base):
    """Representation of a user """
    __tablename__ = 'records_TEMP'
    device_id = Column(Integer, ForeignKey('devices.device_id'), nullable=False)
    measure = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=True)


    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)
