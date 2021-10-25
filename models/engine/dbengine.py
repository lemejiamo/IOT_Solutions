#!/usr/bin/python3
""" Data Base engine for IOT_Solutions"""

from models.base_model import IOT_Model, Base
from models.companies import Company
from models.areas import Area
from models.campus import Campus
from models.users import User
from models.devices import Device
from models.records_humidity import Record_HUMIDITY
from models.records_temp import Record_TEMP
import sqlalchemy
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text

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
        CLOSE           --  call remove() method on the private session attribute
        __init_session  --  initialize a new session for the transaction
        close_session   --  finalize the current_session
        get_objects     --  Return a list of all objects in DB from given class

    """

    __engine = ""
    __session = ""

    def __init__(self):
        """
        Init connection with the database
        """
        self.__engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PASS,
                                             MYSQL_HOST,
                                             MYSQL_DBASE))

    def init_session(self):

        Session_factory = sessionmaker(self.__engine)
        session = scoped_session(Session_factory)
        self.__session = session

    def reload(self):
        Base.metadata.create_all(self.__engine)

    def save(self, obj):
        self.init_session()
        try:
            self.__session.add(obj)
            self.__session.commit()
        finally:
            self.close_session()

    def close_session(self):
        self.__session.remove()

    def get_objects(self, cls=None):
        from models.base_model import CLASS_MODELS
        self.init_session()
        obj_dict = {}
        if cls in CLASS_MODELS:
            if cls == 'User':
                objects = self.__session.query(User).all()
            if cls == 'Company':
                objects = self.__session.query(Company).all()
            if cls == 'Device':
                objects = self.__session.query(Device).all()
            if cls == 'Campus':
                objects = self.__session.query(Campus).all()
            if cls == 'Record_TEMP':
                objects = self.__session.query(Record_TEMP).all()
            if cls == 'Record_HUMIDITY':
                objects = self.__session.query(Record_HUMIDITY).all()

        else:
            self.close_session()
            return

        for obj in objects:
            key = obj.__class__.__name__ + '.' + obj.uuid_id
            obj_dict[key] = obj
        self.close_session()
        return (obj_dict)

    def get_one(self, cls, id):
        all_obj = self.get_objects(cls)
        for key, obj in all_obj.items():
            if int(obj.id) == id:
                print('\n\nobject find it, MATCH \n\n')
                return obj
        return None
