# ============================================================
#  AutoRent — Car Rental Management System
#  PRG1406 | Group Assignment 1
#  Member 5: Rental class, integration, and README support
# ============================================================

from customer import Customer
from vehicle import Vehicle


class Rental:
    """
    Rental links a Customer to a Vehicle for a selected number of days.
    It calculates the total rental cost with a 10% member discount.
    """

    MEMBER_DISCOUNT_RATE = 0.10

    def __init__(self, customer: Customer, vehicle: Vehicle, duration_days: int):
        self.customer = customer
        self.vehicle = vehicle
        self.duration_days = duration_days

    def total_cost(self) -> float:
        """Calculates total cost after member discount."""
        base_cost = self.vehicle.daily_rate * self.duration_days
        discount = base_cost * Rental.MEMBER_DISCOUNT_RATE if self.customer.is_member else 0.0
        total = base_cost - discount

        return total

    def __str__(self) -> str:
        """Returns a readable rental summary using f-strings."""
        base_cost = self.vehicle.daily_rate * self.duration_days
        discount = base_cost * Rental.MEMBER_DISCOUNT_RATE if self.customer.is_member else 0.0
        total = self.total_cost()
        member_status = "Yes, 10% discount applied" if self.customer.is_member else "No"
        vehicle_type = type(self.vehicle).__name__

        return (
            f"========== RENTAL SUMMARY ==========\n"
            f"  Customer      : {self.customer.name}\n"
            f"  Age           : {self.customer.age} years old\n"
            f"  License No.   : {self.customer.license_num}\n"
            f"  Member        : {member_status}\n"
            f"  Vehicle       : {self.vehicle.make} {self.vehicle.model} ({self.vehicle.year})\n"
            f"  Type          : {vehicle_type}\n"
            f"  Available     : {'Yes' if self.vehicle.available else 'No'}\n"
            f"  Duration      : {self.duration_days} day(s)\n"
            f"  Daily Rate    : {self.vehicle.daily_rate:.2f} FCFA\n"
            f"  Base Cost     : {base_cost:.2f} FCFA\n"
            f"  Discount      : -{discount:.2f} FCFA\n"
            f"  Total To Pay  : {total:.2f} FCFA\n"
            f"===================================="
        )