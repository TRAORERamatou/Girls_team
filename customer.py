# customer.py
# Project: Car Rental — PRG1406

class Customer:
    def __init__(self, nom, age, permis, is_member):
        self.nom = nom              # str
        self.age = age              # int
        self.permis = permis        # str
        self.is_member = is_member  # bool
