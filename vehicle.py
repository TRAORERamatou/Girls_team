class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Vehicle: {self.brand} {self.model} ({self.year})"

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model

    @staticmethod
    def validate_year(year):
        try:
            year = int(year)
            if 1900 <= year <= 2025:
                return True
            return False
        except ValueError:
            return False