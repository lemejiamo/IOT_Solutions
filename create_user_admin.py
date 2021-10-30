#!/usr/bin/python3
"""main to test basic work from models module"""

from models.devices import Device
from models.users import User
from models.companies import Company
from models.campus import Campus
from models import storage
import os

# test uno crear una compañia con datos fake
company_data = {'NIT': '001',
                'name': 'IoT-Solutions',
                'telephone': '00000',
                'email': 'admin@iotsolutions.com',
                'address': 'av evergreen',
                'id': '001'
                }

# dicionario para testear  el usuario
user = {'id': '999',
        'user_id': '999',
        'user_email': 'admin@iotsolutions.com',
        'password': os.getenv('ADMIN_PASS'),
        'rol': True,
        'telephone': '0000000',
        'campus_id': '999',
        'company_id': '001'
        }
# dicionario para testear  el campus
campus = {'id': '999',
          'company_id': '001',
          'name': 'IoT-solutions'
        }


# creacion de los models base
company = Company(**company_data)
company.save()

campus = Campus(**campus)
campus.save()

user = User(**user)
user.save()
