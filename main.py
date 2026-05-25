# ============================================================
#  AutoRent — Car Rental Management System
#  PRG1406 | Group Assignment 1
#  Member 1: main.py — Entry point, menu, inputs, and summary
# ============================================================

from vehicle import Car, LuxuryCar
from customer import Customer
from rental import Rental


# ── Validated Input Functions ─────────────────────────────────

def get_text_input(message):
    """Prompts for a non-empty string."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("  Error: This field cannot be empty. Please try again.")


def get_int_input(message, minimum, maximum):
    """Prompts for an integer between minimum and maximum."""
    while True:
        try:
            value = int(input(message))
            if minimum <= value <= maximum:
                return value
            print(f"  Error: Please enter a number between {minimum} and {maximum}.")
        except ValueError:
            print("  Error: Please enter a valid integer.")


def get_float_input(message, minimum, maximum):
    """Prompts for a float between minimum and maximum."""
    while True:
        try:
            value = float(input(message))
            if minimum <= value <= maximum:
                return value
            print(f"  Error: Please enter a value between {minimum} and {maximum}.")
        except ValueError:
            print("  Error: Please enter a valid number, for example 25000.5.")


def get_bool_input(message):
    """Prompts for yes/no and returns a boolean."""
    while True:
        answer = input(message).strip().lower()

        if answer == "yes":
            return True
        if answer == "no":
            return False

        print("  Error: Please answer with 'yes' or 'no'.")


# ── Vehicle Catalog ───────────────────────────────────────────

def create_catalog():
    """Returns the list of available vehicles."""
    return [
        Car("Toyota", "Corolla", 2020, 15000.0, 4, "Economy"),
        Car("Honda", "CR-V", 2021, 25000.0, 4, "SUV"),
        Car("Peugeot", "508", 2022, 20000.0, 4, "Sedan"),
        LuxuryCar(
            "Mercedes",
            "E-Class",
            2023,
            50000.0,
            4,
            "Luxury",
            "Leather, panoramic roof, GPS",
            True
        ),
    ]


def display_catalog(catalog):
    """Displays all available vehicles."""
    print("\n" + "=" * 50)
    print("        AVAILABLE VEHICLES")
    print("=" * 50)

    for index, car in enumerate(catalog, start=1):
        status = "Available" if car.available else "Rented"
        print(f"  {index}. {car}")
        print(f"     Status: {status}")

    print("=" * 50)


# ── Booking Workflow ──────────────────────────────────────────

def make_booking(catalog):
    """Collects customer information, creates a rental, and prints a summary."""
    print("\nCUSTOMER INFORMATION\n")

    # 1. Last Name (str)
    last_name = get_text_input("  Your last name        : ")

    # 2. First Name (str)
    first_name = get_text_input("  Your first name       : ")

    # 3. Age (int)
    age = get_int_input("  Your age              : ", 18, 80)

    # 4. License Number (str)
    license_num = get_text_input("  Driver's license No.  : ")

    # 5. Loyalty Member (bool)
    is_member = get_bool_input("  Loyalty member? (yes/no): ")

    # 6. Nationality (str)
    nationality = get_text_input("  Nationality           : ")

    # 7. Phone Number (str)
    phone_number = get_text_input("  Phone number          : ")

    # 8. Rental Budget (float)
    budget = get_float_input("  Rental budget (FCFA)  : ", 0.0, 10000000.0)

    customer = Customer(f"{first_name} {last_name}", age, license_num, is_member)

    display_catalog(catalog)

    # 9. Vehicle Choice (int)
    choice = get_int_input(
        f"\n  Choose a vehicle (1-{len(catalog)}): ",
        1,
        len(catalog)
    )

    selected_car = catalog[choice - 1]

    if not selected_car.available:
        print("  Error: This vehicle is currently unavailable.")
        return

    # 10. Rental Duration (int)
    days = get_int_input("  Rental duration (days, 1-30): ", 1, 30)

    # 11. Insurance Option (bool)
    insurance = get_bool_input("  Add insurance? (yes/no): ")

    # 12. Driver Option (bool)
    driver = get_bool_input("  Add a driver? (yes/no): ")

    booking = Rental(customer, selected_car, days)

    base_cost = selected_car.calculate_cost(days)
    rental_cost = booking.total_cost()
    discount = base_cost - rental_cost
    insurance_cost = 2500.0 * days if insurance else 0.0
    driver_cost = 10000.0 * days if driver else 0.0
    total_cost = rental_cost + insurance_cost + driver_cost

    selected_car.available = False
    
    print("\n" + "=" * 50)
    print("           BOOKING SUMMARY")
    print("=" * 50)
    print(f"  Customer       : {customer.name}")
    print(f"  Nationality    : {nationality}")
    print(f"  Phone Number   : {phone_number}")
    print(f"  Age            : {age} years old")
    print(f"  License No.    : {license_num}")
    print(f"  Member         : {'Yes' if is_member else 'No'}")
    print(f"  Budget         : {budget:>10,.0f} FCFA")
    print("-" * 50)
    print(f"  Vehicle        : {selected_car.make} {selected_car.model}")
    print(f"  Year           : {selected_car.year}")
    print(f"  Duration       : {days} day(s)")
    print(f"  Daily Rate     : {selected_car.daily_rate:>10,.0f} FCFA")
    print("-" * 50)
    print(f"  Base Cost      : {base_cost:>10,.0f} FCFA")
    print(f"  Member Discount: {discount:>10,.0f} FCFA")
    print(f"  Insurance      : {insurance_cost:>10,.0f} FCFA")
    print(f"  Driver Fee     : {driver_cost:>10,.0f} FCFA")
    print("-" * 50)
    print(f"  TOTAL TO PAY   : {total_cost:>10,.0f} FCFA")

    if total_cost > budget:
        print("  Warning        : Total cost is above your budget.")
    else:
        print("  Budget Status  : Total cost is within your budget.")

    print("=" * 50)
    print("\n  Booking confirmed! Thank you for choosing AutoRent.")
    print("=" * 50 + "\n")


# ── Main Program ──────────────────────────────────────────────

def main():
    catalog = create_catalog()
    running = True

    while running:
        print("\n" + "=" * 50)
        print("       AUTORENT — CAR RENTAL SYSTEM")
        print("       Burkina Institute of Technology")
        print("=" * 50)
        print("  1. Make a booking")
        print("  2. View available vehicles")
        print("  3. Exit")
        print("=" * 50)

        menu_choice = get_int_input("  Choose an option (1-3): ", 1, 3)

        if menu_choice == 1:
            make_booking(catalog)
        elif menu_choice == 2:
            display_catalog(catalog)
        elif menu_choice == 3:
            running = False
            print("\n  Thank you for using AutoRent. Goodbye!\n")


if __name__ == "__main__":
    main()