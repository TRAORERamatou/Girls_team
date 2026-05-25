# ============================================================
#  AutoRent — Car Rental Management System
#  PRG1406 | Group Assignment 1
#  customer.py
# ============================================================


class Customer:
    def __init__(self, name, age, license_num, is_member):
        self.name = str(name)
        self.age = int(age)
        self.license_num = str(license_num)
        self.permis = self.license_num
        self.is_member = bool(is_member)

    def __str__(self):
        return (
            f"Customer: {self.name}, {self.age} years old, "
            f"License No.: {self.license_num}, "
            f"Member: {'Yes' if self.is_member else 'No'}"
        )

    def __repr__(self):
        return (
            f"Customer(name='{self.name}', age={self.age}, "
            f"license_num='{self.license_num}', is_member={self.is_member})"
        )

    def display_info(self):
        """Returns customer information using f-strings."""
        return (
            f"Customer Name : {self.name}\n"
            f"Age           : {self.age}\n"
            f"License No.   : {self.license_num}\n"
            f"Member        : {'Yes' if self.is_member else 'No'}"
        )