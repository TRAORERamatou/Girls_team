# rental.py
# Member 5 - Branch: feature/rental-integration-readme

from customer import Customer
from vehicle import Vehicle


class Rental:
    """
    Rental class: links a Customer to a Vehicle for a given duration.
    Handles total cost calculation with member discount.
    """

    MEMBER_DISCOUNT_RATE = 0.10  # 10% discount for members

    def __init__(self, customer: Customer, vehicle: Vehicle, duration_days: int):
        """
        Initializes a rental.

        Args:
            customer (Customer): The customer renting the vehicle.
            vehicle (Vehicle): The rented vehicle.
            duration_days (int): The rental duration in days.
        """
        self.customer = customer
        self.vehicle = vehicle
        self.duration_days = duration_days

    def total_cost(self) -> float:
        """
        Calculates the total rental cost.
        Applies a 10% discount if the customer is a member.

        3rd arithmetic expression:
            base_cost = vehicle.calculate_cost(duration_days)
            discount  = base_cost * MEMBER_DISCOUNT_RATE  (if is_member)
            total     = base_cost - discount

        Returns:
            float: The total amount to pay.
        """
        base_cost = self.vehicle.calculate_cost(self.duration_days)
        discount = base_cost * Rental.MEMBER_DISCOUNT_RATE if self.customer.is_member else 0
        total = base_cost - discount
        return total

    def __str__(self) -> str:
        """
        Returns a readable summary of the rental.
        """
        base_cost = self.vehicle.calculate_cost(self.duration_days)
        discount = base_cost * Rental.MEMBER_DISCOUNT_RATE if self.customer.is_member else 0
        total = base_cost - discount

        member_status = "Yes (10% discount applied)" if self.customer.is_member else "No"
        vehicle_type = type(self.vehicle).__name__

        return (
            f"========== RENTAL SUMMARY ==========\n"
            f"  Customer      : {self.customer.name}\n"
            f"  Age           : {self.customer.age}\n"
            f"  License       : {'Yes' if self.customer.permis else 'No'}\n"
            f"  Member        : {member_status}\n"
            f"  Vehicle       : {self.vehicle.make} {self.vehicle.model} ({self.vehicle.year})\n"
            f"  Type          : {vehicle_type}\n"
            f"  Available     : {'Yes' if self.vehicle.available else 'No'}\n"
            f"  Duration      : {self.duration_days} day(s)\n"
            f"  Daily rate    : ${self.vehicle.daily_rate:.2f}\n"
            f"  Base cost     : ${base_cost:.2f}\n"
            f"  Discount      : -${discount:.2f}\n"
            f"  TOTAL         : ${total:.2f}\n"
            f"====================================="
        )
