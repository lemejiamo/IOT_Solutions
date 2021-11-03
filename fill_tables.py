#!/usr/bin/python3
"""main to test basic work from models module"""

from models.devices import Device
from models.users import User
from models.companies import Company
from models.campus import Campus
from models import storage
import os

# test uno crear una compañia con datos fake
company_data = {'NIT': '8888',
                'name': 'Productora de Vinos',
                'telephone': '00000',
                'email': 'admin@vinos.com',
                'address': 'av evergreen',
                'id': '8888'
                }
# creacion de los models base
company = Company(**company_data)
company.save()


# dicionario para testear  el campus
campus = {'id': 'vin01',
          'company_id': '8888',
          'name': 'Viñedo chile'
        }

campus = Campus(**campus)
campus.save()

campus = {'id': 'vin02',
          'company_id': '8888',
          'name': 'Viñedo italia'
        }

campus = Campus(**campus)
campus.save()

print("ok1")
# dicionario para testear  el usuario
user = {'id': '8888',
        'user_id': '8888',
        'user_email': 'admin@vinos.com',
        'password': 'vinos',
        'rol': True,
        'telephone': '0000000',
        'campus_id': 'vin01',
        'company_id': '8888'
        }
user = User(**user)
user.save()

# dicionario para testear  el usuario
user = {'id': '008',
        'user_id': '008',
        'user_email': 'aux01@vinos.com',
        'password': 'vinos',
        'rol': False,
        'telephone': '0000000',
        'campus_id': 'vin01',
        'company_id': '8888'
        }
user = User(**user)
user.save()
print("ok2")

# dicionario para testear  el usuario
device = {'id': '001',
        'campus_id': 'vin01',
        'location': 'cava 1',
        'area': 'vinos tintos',
        }
device = Device(**device)
device.save()


device = {'id': '002',
        'campus_id': 'vin01',
        'location': 'cava 1',
        'area': 'vinos blancos',
        }
device = Device(**device)
device.save()


device = {'id': '003',
        'campus_id': 'vin01',
        'location': 'cava 1',
        'area': 'vinos rosas',
        }
device = Device(**device)
device.save()

print("ok3")
# dicionario para testear  el usuario
device = {'id': '004',
        'campus_id': 'vin02',
        'location': 'cava 1',
        'area': 'vinos tintos',
        }
device = Device(**device)
device.save()


device = {'id': '005',
        'campus_id': 'vin02',
        'location': 'cava 1',
        'area': 'vinos blancos',
        }
device = Device(**device)
device.save()


device = {'id': '006',
        'campus_id': 'vin02',
        'location': 'cava 1',
        'area': 'vinos rosas',
        }
device = Device(**device)
device.save()
print("ok4")
