#!/usr/bin/python3

import models
from models.base_model import IOT_Model
from models.users import User
from models.companies import Company

company_data = {'NIT': '86006487',
                'name': 'company',
                'telephone': '7564879',
                'email': 'test@email.com',
                'address': 'calle 693'}

data = {'user_email': 'a@a',
        'password': 'pass',
        'campus': 'Bogota',
        'company_id': '86006487'
        }
company = Company(**company_data)
print(type(company))
print (company.__dict__)
print (company.email)
print (company.NIT)
print (company.telephone)
print (company.address)
print(company.name)
company.save()

models.storage.reload()
user = User(**data)
print (user.__dict__)
user.save()
