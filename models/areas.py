#!/usr/bin/python3
""" Model to Locations table"""


import models
from models.base_model import IOT_Model, Base
from sqlalchemy.sql.sqltypes import DateTime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Area(IOT_Model, Base):
    """Representation of a Location"""
    
    __tablename__ = 'areas'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(30), nullable=False)
    devices = relationship('Device',
                            backref='areas')
    
    def __init__(self, **kwargs):
        """initializes location"""
        super().__init__(**kwargs)

