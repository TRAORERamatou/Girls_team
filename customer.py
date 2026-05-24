# ============================================================
#  AutoRent — Car Rental Management System
#  Member 4: Magic Methods and Decorators
#  File: customer.py
# ============================================================

class Customer:
    def __init__(self, nom, age, permis, is_member):
        self.nom = nom
        self.age = age
        self.permis = permis
        self.is_member = is_member

    def __str__(self):
        # __str__ is used to display a clean, readable summary
        # when print(customer) is called — as seen in main.py
        member_status = "Member" if self.is_member else "Non-member"
        return (
            f"Customer    : {self.nom}\n"
            f"Age         : {self.age} years old\n"
            f"License No. : {self.permis}\n"
            f"Status      : {member_status}"
        )

    def __repr__(self):
        return (
            f"Customer(nom='{self.nom}', age={self.age}, "
            f"permis='{self.permis}', is_member={self.is_member})"
        )

    def __eq__(self, other):
        # Two customers are equal if they have the same license number
        if not isinstance(other, Customer):
            return False
        return self.permis == other.permis

