#!/usr/bin/python3
"""main to test basic work from models module"""

from models.devices import Device
from models.users import User
from models.companies import Company
from models.campus import Campus
from models import storage

# dicionario para testear  el usuario
data = {'id': '860062848',
        'user_id': '123456789',
        'user_email': 'luismejia69@gmail.com',
        'password': 'user_1',
        'rol': True,
        'telephone': '654987524',
        'campus_id': '1',
        'company_id': '860062847'
        }


data1 = {'id': '860062845',
        'user_id': '1234567890',
        'user_email': 'luismejia69@outlook.com',
        'password': 'user_1',
        'rol': True,
        'telephone': '654987524',
        'campus_id': '1',
        'company_id': '860062847'
        }


data2 = {'id': '860062844',
        'user_id': '123987456',
        'user_email': 'iotsolutionsholbi@gmail.com',
        'password': 'user_1',
        'rol': False,
        'telephone': '654987524',
        'campus_id': '1',
        'company_id': '860062847'
        }

data3 = {'id': '860062843',
        'user_id': '987654321',
        'user_email': '2956@holbertonschool.com',
        'password': 'user_1',
        'rol': True,
        'telephone': '654987524',
        'campus_id': '1',
        'company_id': '860062847'
        }



user = User(**data)
user.save()

user1 = User(**data1)
user1.save()

user2 = User(**data2)
user2.save()

user3 = User(**data3)
user3.save()

# print de la representacion en dicionario de las instancias
print(storage.get_objects("User"))
