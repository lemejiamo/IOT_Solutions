#!/usr/bin/python3

from models import storage

print(storage.get_objects("Company"))
print(storage.get_objects("User"))
print(storage.get_objects("Device"))
print(storage.get_objects("Campus"))
print(storage.get_one("Company", 860062847))
