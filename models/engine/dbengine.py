#!/usr/bin/python3
""" Data Base engine for IOT_Solutions"""

from models.base_model import IOT_Model, Base
from models.companies import Company
from models.users import User
from models.devices import Device
from models.campus import Campus
from models.records_humidity import Record_HUMIDITY
from models.records_temp import Record_TEMP
import sqlalchemy
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

MYSQL_USER = 'IOT_DEV'
MYSQL_PASS = 'IOTDEV'
MYSQL_HOST = 'localhost'
MYSQL_DBASE = 'IOT_Solutions_dev'

class DbEngine():
    """Class to manage the procedures to get acces
        too Data Base
    Attributes:
        __engine        --  the engine
        __session       --  the session to use to access the DB

    Methods:
        CONSTRUCTOR     --  create a instance of DBengine and
                            initialize the connection to de DataBase
        NEW             --  add the object to the current database session
        SAVE            --  commit all changes of the current database session
        RELOAD          --  reload data from database
    """

    __engine = ""
    __session = ""

    def __init__(self):
        self.__engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PASS,
                                             MYSQL_HOST,
                                             MYSQL_DBASE))



    def save(self, obj):
        self.__session.add(obj)
        self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()