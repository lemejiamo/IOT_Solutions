#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import IOT_Model, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class User(IOT_Model, Base):
    """Representation of a user """
    __tablename__ = 'users'
    user_email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    campus = Column(String(128), nullable=True)
    company_id = Column(Integer)

    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)
