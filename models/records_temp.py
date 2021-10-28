#!/usr/bin/python3
""" holds class company"""


from sqlalchemy.sql.sqltypes import DateTime
import models
from models.base_model import IOT_Model, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from datetime import datetime
import smtplib


class Record_TEMP(IOT_Model, Base):
    """Representation of a user """

# |---------------- CLASS ATTRIBUTE ----------------|

    __tablename__ = 'records_TEMP'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    measure = Column(Float, nullable=False)
    date = Column(DateTime, nullable=True, default=datetime.now)

# |---------------- CLASS METHODS ----------------|
    __average = 1.5
    __limit = 0.99

    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)

    @staticmethod
    def alert(obj):
        diference =  float(obj.measure) - Record_TEMP.__average
        if  diference > Record_TEMP.__limit:
            try:
                origin_email =  'IOTSolutionsHolbi@gmail.com'
                password = 'AZ2hQnYZhKfMP9S'

                user_id = obj.user_id
                destiny_email = models.storage.get_one('User', obj.user_id).__dict__['user_email']
                print('sending email to \n\n')
                print('\t\t {}'.format(destiny_email))

                msg = 'Correo de prueba IOT Solutions'
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                server.login(origin_email, password)
                server.sendmail(origin_email, destiny_email, msg)
                server.quit()
                return (True)
            except:
                print ('no se pudo enviar el mensaje')
                return (True)
        else:
            print('No alert Generated')
            return (False)
