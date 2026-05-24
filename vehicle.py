# vehicle.py

class Vehicle:
    def __init__(self, make, model, year, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.available = True

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.daily_rate:,.0f} FCFA/day"


class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, num_doors, car_type):
        super().__init__(make, model, year, daily_rate)
        self.num_doors = num_doors
        self.car_type = car_type

    def apply_discount(self, percent):
        """Applies a discount to the daily rate."""
        if 0 < percent < 100:
            self.daily_rate -= self.daily_rate * (percent / 100)

    def __str__(self):
        return f"{super().__str__()} ({self.car_type}, {self.num_doors} doors)"


class LuxuryCar(Car):
    def __init__(self, make, model, year, daily_rate, num_doors, car_type, premium_features, chauffeur_available):
        super().__init__(make, model, year, daily_rate, num_doors, car_type)
        self.premium_features = premium_features
        self.chauffeur_available = chauffeur_available

    def add_premium_service(self, service):
        """Adds a new premium service to the car."""
        if self.premium_features:
            self.premium_features += f", {service}"
        else:
            self.premium_features = service

    def __str__(self):
        chauffeur = "Chauffeur available" if self.chauffeur_available else "No chauffeur"
        return f"{super().__str__()} [Luxury: {self.premium_features}, {chauffeur}]"
