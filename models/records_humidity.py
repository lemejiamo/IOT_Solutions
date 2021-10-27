#!/usr/bin/python3
""" holds class Record_HUMIDITY"""

from sqlalchemy.sql.sqltypes import DateTime
import models
from models.base_model import IOT_Model, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Record_HUMIDITY(IOT_Model, Base):
    """Representation of a user """
    __tablename__ = 'records_HUMIDITY'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, default=1)
    user_id = Column(String(128), ForeignKey('users.id'))
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    measure = Column(Float, nullable=False)
    date = Column(DateTime, nullable=True)

    __average = 1.5
    __limit = 0.99


    def __init__(self, **kwargs):
        """initializes user"""
        super().__init__(**kwargs)


    @staticmethod
    def alert(obj):
        diference =  float(obj.measure) - Record_HUMIDITY.__average
        if  diference > Record_HUMIDITY.__limit:
            try:
                origin_email =  'IOTSolutionsHolbi@gmail.com'
                password = 'AZ2hQnYZhKfMP9S'

                user_id = int(obj.user_id)
                destiny_email = models.storage.get_one('User', int(obj.user_id)).__dict__['user_email']
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
