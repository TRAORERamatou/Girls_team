# ============================================================
#  AutoRent — Car Rental Management System
#  Member 4: Magic Methods and Decorators
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
        return (
            f"{self.year} {self.make} {self.model} "
            f"- {self.daily_rate:,.0f} FCFA/day"
        )

    def __repr__(self):
        return (
            f"Vehicle(make='{self.make}', model='{self.model}', "
            f"year={self.year}, daily_rate={self.daily_rate})"
        )

    @staticmethod
    def validate_year(year):
        try:
            year = int(year)
            return 1900 <= year <= 2026
        except ValueError:
            return False


class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, doors, category):
        super().__init__(make, model, year, daily_rate)
        self.doors = doors
        self.category = category

    def __str__(self):
        return (
            f"{self.year} {self.make} {self.model} "
            f"({self.category}, {self.doors} doors) "
            f"- {self.daily_rate:,.0f} FCFA/day"
        )

    def __repr__(self):
        return (
            f"Car(make='{self.make}', model='{self.model}', year={self.year}, "
            f"daily_rate={self.daily_rate}, doors={self.doors}, "
            f"category='{self.category}')"
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
        doors,
        category,
        luxury_features,
        chauffeur_available
    ):
        super().__init__(make, model, year, daily_rate, doors, category)
        self.luxury_features = luxury_features
        self.chauffeur_available = chauffeur_available

    def __str__(self):
        chauffeur = "chauffeur available" if self.chauffeur_available else "no chauffeur"
        return (
            f"{self.year} {self.make} {self.model} "
            f"({self.category}, {self.doors} doors, {chauffeur}) "
            f"- {self.daily_rate:,.0f} FCFA/day"
        )

    def __repr__(self):
        return (
            f"LuxuryCar(make='{self.make}', model='{self.model}', "
            f"year={self.year}, daily_rate={self.daily_rate}, "
            f"doors={self.doors}, category='{self.category}', "
            f"luxury_features='{self.luxury_features}', "
            f"chauffeur_available={self.chauffeur_available})"
        )