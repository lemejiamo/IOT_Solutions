#!/usr/bin/python3
"""main to test basic work from models module"""

from models.devices import Device
from models.areas import Area
from models.users import User
from models.companies import Company
from models.campus import Campus
from models import storage


# test uno crear una compañia con datos fake
company_data = {'NIT': '860062847',
                'name': 'test_1',
                'telephone': '7564879',
                'email': 'test@email.com',
                'address': 'calle 693',
                'id': '860062847'
                }

# dicionario para testear  el usuario
data = {'id': '8600628479',
        'user_id': '1022745078',
        'user_email': 'user_1@email.com',
        'password': 'user_1',
        'rol': True,
        'telephone': '654987524',
        'campus_id': '1',
        'company_id': '860062847'
        }

# dicionario para testear  el campus
campus = {'id': '1',
          'company_id': '860062847',
          'name': 'Bog_centro'
        }

# diccionario para testear el device
device = {'campus_id': '1',
          'area': 'Cocina',
          'location': 'nevera_1'
        }



# creacion de los models base
company = Company(**company_data)
company.save()

campus = Campus(**campus)
campus.save()


user = User(**data)
user.save()

device = Device(**device)
device.save()

# print de la representacion en dicionario de las instancias
print (user.__dict__)
print (company.__dict__)
print (campus.__dict__)
print (device.__dict__)

print("OBJECTS:\n\n")
print(storage.get_objects("User"))
