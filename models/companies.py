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
    NIT = Column(String(128), primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    telephone = Column(String(128),  nullable=False)
    email = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    id = Column(String(128), unique=True)
    users = relationship("User",
                          backref="companies")
    campus = relationship("Campus",
                          backref="companies")

    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)

