# rental.py
# Membre 5 - Branche: feature/rental-integration-readme

from customer import Customer
from vehicle import Vehicle


class Rental:
    """
    Classe Rental : relie un Customer à un Vehicle pour une durée donnée.
    Gère le calcul du coût total avec remise membre (10%).
    """

    MEMBER_DISCOUNT_RATE = 0.10  # 10% de remise pour les membres

    def __init__(self, customer: Customer, vehicle: Vehicle, duration_days: int):
        """
        Initialise une location.

        Args:
            customer (Customer): Le client qui loue le véhicule.
            vehicle (Vehicle): Le véhicule loué (Vehicle, Car ou LuxuryCar).
            duration_days (int): La durée de la location en jours.
        """
        self.customer = customer
        self.vehicle = vehicle
        self.duration_days = duration_days

    def total_cost(self) -> float:
        """
        Calcule le coût total de la location.
        Utilise calculate_cost(days) de Vehicle, puis applique la remise membre.

        3ème expression arithmétique :
            coût_base = vehicle.calculate_cost(duration_days)
            remise    = coût_base * MEMBER_DISCOUNT_RATE  (si is_member)
            total     = coût_base - remise

        Returns:
            float: Le montant total à payer.
        """
        base_cost = self.vehicle.calculate_cost(self.duration_days)
        discount = base_cost * Rental.MEMBER_DISCOUNT_RATE if self.customer.is_member else 0
        total = base_cost - discount
        return total

    def __str__(self) -> str:
        """
        Retourne un récapitulatif lisible de la location (magic method - Part 3).
        """
        base_cost = self.vehicle.calculate_cost(self.duration_days)
        discount = base_cost * Rental.MEMBER_DISCOUNT_RATE if self.customer.is_member else 0
        total = base_cost - discount

        member_status = "Oui (remise 10% appliquée)" if self.customer.is_member else "Non"

        # Détection du type de véhicule pour affichage enrichi
        vehicle_type = type(self.vehicle).__name__  # "Vehicle", "Car" ou "LuxuryCar"

        return (
            f"========== RÉCAPITULATIF DE LOCATION ==========\n"
            f"  Client        : {self.customer.name}\n"
            f"  Âge           : {self.customer.age} ans\n"
            f"  Permis        : {'Oui' if self.customer.permis else 'Non'}\n"
            f"  Membre        : {member_status}\n"
            f"  Véhicule      : {self.vehicle.make} {self.vehicle.model} ({self.vehicle.year})\n"
            f"  Type          : {vehicle_type}\n"
            f"  Disponible    : {'Oui' if self.vehicle.available else 'Non'}\n"
            f"  Durée         : {self.duration_days} jour(s)\n"
            f"  Tarif/jour    : {self.vehicle.daily_rate:.2f} €\n"
            f"  Coût de base  : {base_cost:.2f} €\n"
            f"  Remise        : -{discount:.2f} €\n"
            f"  TOTAL À PAYER : {total:.2f} €\n"
            f"================================================"
        )
