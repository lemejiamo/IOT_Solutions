#!/usr/bin/python3

import models
from models.base_model import IOT_Model
from models.devices import Device
from models.users import User
from models.companies import Company
from models.campus import Campus


# test uno crear una compañia con datos fake
company_data = {'NIT': '860062847',
                'name': 'test_1',
                'telephone': '7564879',
                'email': 'test@email.com',
                'address': 'calle 693'
                }

# dicionario para testear  el usuario
data = {'company_id': '860062847',
        'user_id': '1022745078',
        'user_email': 'a@a',
        'password': 'pass',
        'rol': True,
        'telephone': '654987524',
        'campus_id': '1'
        }

# dicionario para testear  el campus
campus = {'campus_id': '1',
          'company_id': '860062847',
          'name': 'Bog_centro'
        }

device = {'campus_id': '1',
          'area': 'Cocina_principal',
          'location': 'nevera_1'
        }


#company = Company(**company_data)
#company.save()

#campus = Campus(**campus)
#campus.save()


#user = User(**data)
#user.save()

device = Device(**device)
device.save()

#print (user.__dict__)
#print (company.__dict__)
#print (campus.__dict__)
print (device.__dict__)
