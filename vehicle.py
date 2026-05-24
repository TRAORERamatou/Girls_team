# ============================================================
#  AutoRent — Car Rental Management System
#  PRG1406 | Group Assignment 1
#  vehicle.py
# ============================================================


class Vehicle:
    def __init__(self, make, model, year, daily_rate):
        if not Vehicle.validate_year(year):
            raise ValueError("Invalid vehicle year.")

        self.make = make
        self.model = model
        self.year = int(year)
        self.daily_rate = float(daily_rate)
        self.available = True

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.daily_rate:,.0f} FCFA/day"

    def __repr__(self):
        return (
            f"Vehicle(make='{self.make}', model='{self.model}', "
            f"year={self.year}, daily_rate={self.daily_rate})"
        )

    @staticmethod
    def validate_year(year):
        # Static method is used because year validation does not need
        # access to a specific Vehicle object or to the Vehicle class itself.
        try:
            year = int(year)
            return 1900 <= year <= 2026
        except ValueError:
            return False


class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, num_doors, car_type):
        super().__init__(make, model, year, daily_rate)
        self.num_doors = int(num_doors)
        self.car_type = car_type

    def apply_discount(self, percent):
        """Applies a discount to the daily rate."""
        if 0 < percent < 100:
            self.daily_rate -= self.daily_rate * (percent / 100)

    def __str__(self):
        return f"{super().__str__()} ({self.car_type}, {self.num_doors} doors)"

    def __repr__(self):
        return (
            f"Car(make='{self.make}', model='{self.model}', year={self.year}, "
            f"daily_rate={self.daily_rate}, num_doors={self.num_doors}, "
            f"car_type='{self.car_type}')"
        )

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False

        return self.daily_rate == other.daily_rate


class LuxuryCar(Car):
    def __init__(
        self,
        make,
        model,
        year,
        daily_rate,
        num_doors,
        car_type,
        premium_features,
        chauffeur_available
    ):
        super().__init__(make, model, year, daily_rate, num_doors, car_type)
        self.premium_features = premium_features
        self.chauffeur_available = bool(chauffeur_available)

    def add_premium_service(self, service):
        """Adds a new premium service to the car."""
        if self.premium_features:
            self.premium_features += f", {service}"
        else:
            self.premium_features = service

    def __str__(self):
        chauffeur = "Chauffeur available" if self.chauffeur_available else "No chauffeur"
        return f"{super().__str__()} [Luxury: {self.premium_features}, {chauffeur}]"

    def __repr__(self):
        return (
            f"LuxuryCar(make='{self.make}', model='{self.model}', "
            f"year={self.year}, daily_rate={self.daily_rate}, "
            f"num_doors={self.num_doors}, car_type='{self.car_type}', "
            f"premium_features='{self.premium_features}', "
            f"chauffeur_available={self.chauffeur_available})"
        )