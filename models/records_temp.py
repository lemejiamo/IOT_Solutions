#!/usr/bin/python3
""" holds class company"""

from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import DateTime
import models
from models.base_model import IOT_Model, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from datetime import datetime


class Record_TEMP(IOT_Model, Base):
    """Representation of a user """

    __tablename__ = 'records_TEMP'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    measure = Column(Float, nullable=False)
    date = Column(DateTime, nullable=True, default=datetime.now)


    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)
