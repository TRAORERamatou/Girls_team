# ============================================================
#  AutoRent — Car Rental Management System
#  Member 4: Magic Methods and Decorators
# ============================================================


class Vehicle:
    def _init_(self, make, model, year, daily_rate):
        if not Vehicle.validate_year(year):
            raise ValueError("Invalid vehicle year.")

        self.make = make
        self.model = model
        self.year = int(year)
        self.daily_rate = float(daily_rate)
        self.available = True

    def _str_(self):
        return (
            f"{self.year} {self.make} {self.model} "
            f"- {self.daily_rate:,.0f} FCFA/day"
        )

    def _repr_(self):
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
    def _init_(self, make, model, year, daily_rate, doors, category):
        super()._init_(make, model, year, daily_rate)
        self.doors = doors
        self.category = category

    def _str_(self):
        return (
            f"{self.year} {self.make} {self.model} "
            f"({self.category}, {self.doors} doors) "
            f"- {self.daily_rate:,.0f} FCFA/day"
        )

    def _repr_(self):
        return (
            f"Car(make='{self.make}', model='{self.model}', year={self.year}, "
            f"daily_rate={self.daily_rate}, doors={self.doors}, "
            f"category='{self.category}')"
        )

    def _eq_(self, other):
        if not isinstance(other, Car):
            return False

        return self.daily_rate == other.daily_rate


class LuxuryCar(Car):
    def _init_(
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
        super()._init_(make, model, year, daily_rate, doors, category)
        self.luxury_features = luxury_features
        self.chauffeur_available = chauffeur_available

    def _str_(self):
        chauffeur = "chauffeur available" if self.chauffeur_available else "no chauffeur"
        return (
            f"{self.year} {self.make} {self.model} "
            f"({self.category}, {self.doors} doors, {chauffeur}) "
            f"- {self.daily_rate:,.0f} FCFA/day"
        )

    def _repr_(self):
        return (
            f"LuxuryCar(make='{self.make}', model='{self.model}', "
            f"year={self.year}, daily_rate={self.daily_rate}, "
            f"doors={self.doors}, category='{self.category}', "
            f"luxury_features='{self.luxury_features}', "
            f"chauffeur_available={self.chauffeur_available})"
        )