# main.py
# Membre 5 — Tests d'intégration complets
# Vérifie que tous les fichiers s'importent et fonctionnent ensemble

from customer import Customer
from vehicle import Vehicle, Car, LuxuryCar
from rental import Rental


def main():
    print("=== Système de Location de Véhicules ===\n")

    # --- Validation d'année (staticmethod M4) ---
    print("-- Test validate_year() --")
    print(f"  2020 valide ? {Vehicle.validate_year(2020)}")
    print(f"  1800 valide ? {Vehicle.validate_year(1800)}\n")

    # --- Test 1 : Client membre + voiture standard ---
    client_membre = Customer(name="Alice Dupont", age=30, permis=True, is_member=True)
    voiture = Car(make="Toyota", model="Corolla", year=2020,
                  daily_rate=50.0, available=True,
                  num_doors=4, car_type="Berline")
    location1 = Rental(customer=client_membre, vehicle=voiture, duration_days=5)

    print(location1)
    print(f"  → total_cost() : {location1.total_cost():.2f} €\n")

    # --- Test 2 : Client non-membre + voiture de luxe ---
    client_normal = Customer(name="Bob Martin", age=45, permis=True, is_member=False)
    luxe = LuxuryCar(make="BMW", model="Série 7", year=2023,
                     daily_rate=200.0, available=True,
                     num_doors=4, car_type="Berline",
                     premium_features="Cuir, Toit panoramique",
                     chauffeur_available=True)
    location2 = Rental(customer=client_normal, vehicle=luxe, duration_days=3)

    print(location2)
    print(f"  → total_cost() : {location2.total_cost():.2f} €\n")

    # --- Test 3 : __eq__ sur Car (M4) ---
    print("-- Test __eq__ entre deux Car --")
    car_a = Car(make="Renault", model="Clio", year=2021,
                daily_rate=35.0, available=True, num_doors=5, car_type="Citadine")
    car_b = Car(make="Peugeot", model="208", year=2022,
                daily_rate=35.0, available=True, num_doors=5, car_type="Citadine")
    print(f"  car_a == car_b (même tarif 35€) ? {car_a == car_b}\n")

    # --- Test 4 : apply_discount (M3) ---
    print("-- Test apply_discount(20%) sur Car --")
    car_a.apply_discount(20)
    print(f"  Nouveau tarif de car_a après remise 20% : {car_a.daily_rate:.2f} €\n")

    # --- Test 5 : Client sans permis ---
    print("-- Test client sans permis --")
    sans_permis = Customer(name="Charlie Léon", age=17, permis=False, is_member=False)
    print(f"  {sans_permis}\n")

    # --- Récapitulatif final f-string (M1 style) ---
    print("========== BILAN DES LOCATIONS ==========")
    for i, loc in enumerate([location1, location2], 1):
        print(f"  Location {i} : {loc.customer.name} — {loc.total_cost():.2f} €")
    print("=========================================")


if __name__ == "__main__":
    main()
