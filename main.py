# main.py
# Member 2 — Main Program
# Project : Car Rental — PRG1406

from vehicle import Vehicle
from customer import Customer

print("=" * 45)
print("      CAR RENTAL AGENCY")
print("=" * 45)

# ── Vehicle information input ──────────────
print("\n--- Vehicle Registration ---")

make = input("Vehicle make: ")           # str
model = input("Vehicle model: ")         # str

while True:
    try:
        year = int(input("Year of manufacture: "))  # int
        if year < 1900 or year > 2026:
            print("Invalid year. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

while True:
    try:
        daily_rate = float(input("Daily rate (FCFA): "))  # float
        if daily_rate <= 0:
            print("The rate must be positive.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

available = input("Is the vehicle available? (yes/no): ").lower() == "yes"  # bool

vehicle = Vehicle(make, model, year, daily_rate, available)

# ── Customer information input ────────────────
print("\n--- Customer Registration ---")

nom = input("Customer full name: ")         # str

while True:
    try:
        age = int(input("Customer age: "))    # int
        if age < 18:
            print("Customer must be at least 18 years old.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

permis = input("Driver's license number: ")           # str

is_member = input("Is the customer a loyalty member? (yes/no): ").lower() == "yes"  # bool

customer = Customer(nom, age, permis, is_member)

# ── Rental duration input ───────────
while True:
    try:
        days = int(input("\nNumber of rental days: "))  # int
        if days <= 0:
            print("Number of days must be positive.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

# ── Arithmetic expressions ─────────────────────
base_cost = vehicle.calculate_cost(days)                     # rate × days
discount = base_cost * 0.15 if customer.is_member else 0.0  # 15% discount for members
final_cost = base_cost - discount                            # final cost

# ── Summary screen with f-strings ────────────
print("\n" + "=" * 45)
print("         RENTAL SUMMARY")
print("=" * 45)

print("\n>> Vehicle:")
vehicle.display_info()

print(f"\n>> Customer:")
print(f"  Name          : {customer.nom}")
print(f"  Age           : {customer.age} years old")
print(f"  License No.   : {customer.permis}")
print(f"  Member        : {customer.is_member}")

print(f"\n>> Financial Details:")
print(f"  Duration      : {days} day(s)")
print(f"  Rate/day      : {vehicle.daily_rate} FCFA")
print(f"  Base cost     : {base_cost} FCFA")
print(f"  Discount      : -{discount} FCFA")
print(f"  TOTAL TO PAY  : {final_cost} FCFA")

print("\n" + "=" * 45)
print("Thank you for your trust!")
print("=" * 45)
