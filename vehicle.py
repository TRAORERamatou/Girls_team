# vehicle.py
# Project: Car Rental — PRG1406

class Vehicle:
    def __init__(self, make, model, year, daily_rate, available):
        self.make = make              # str
        self.model = model            # str
        self.year = year              # int
        self.daily_rate = daily_rate  # float
        self.available = available    # bool

    def calculate_cost(self, days):
        return self.daily_rate * days  # rate × days

    def display_info(self):
        print(f"Make      : {self.make}")
        print(f"Model     : {self.model}")
        print(f"Year      : {self.year}")
        print(f"Rate/day  : {self.daily_rate} FCFA")
        print(f"Available : {self.available}")
