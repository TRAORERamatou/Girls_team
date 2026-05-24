# 🚗 Système de Location de Véhicules

Projet Python collaboratif — 5 membres | POO, Héritage, Magic Methods, Décorateurs

---

## 📁 Structure du projet

```
vehicule_location/
│
├── main.py        # Membre 1  — Point d'entrée, menu, inputs validés
├── vehicle.py     # Membres 2, 3, 4 — Classes Vehicle, Car, LuxuryCar
├── customer.py    # Membres 2, 4 — Classe Customer
└── rental.py      # Membre 5  — Classe Rental (intégration)
```

---

## 📦 Classes

### `Vehicle` (vehicle.py — M2 + M4)

| Attribut         | Type    | Description                        |
|------------------|---------|------------------------------------|
| `make`           | `str`   | Marque du véhicule                 |
| `model`          | `str`   | Modèle du véhicule                 |
| `year`           | `int`   | Année de fabrication               |
| `daily_rate`     | `float` | Tarif journalier en euros (€)      |
| `available`      | `bool`  | Disponibilité du véhicule          |

**Méthodes :**
- `calculate_cost(days)` → `float` : `daily_rate × days`
- `display_info()` → affiche les infos avec f-string
- `__str__()` → représentation lisible (M4)
- `__repr__()` → représentation technique (M4)
- `@staticmethod validate_year(year)` → valide l'année (M4)

---

### `Car(Vehicle)` (vehicle.py — M3)

| Attribut         | Type    | Description                        |
|------------------|---------|------------------------------------|
| `num_doors`      | `int`   | Nombre de portes                   |
| `car_type`       | `str`   | Type (Berline, SUV, Citadine…)     |

**Méthodes :**
- `apply_discount(percent)` → réduit `daily_rate` d'un pourcentage
- `__eq__(other)` → compare les tarifs (M4)

---

### `LuxuryCar(Car)` (vehicle.py — M3)

| Attribut              | Type    | Description                    |
|-----------------------|---------|--------------------------------|
| `premium_features`    | `str`   | Options premium (ex: Cuir…)    |
| `chauffeur_available` | `bool`  | Chauffeur disponible           |

**Méthodes :**
- `add_premium_service()` → ajoute un service premium

---

### `Customer` (customer.py — M2 + M4)

| Attribut     | Type    | Description                        |
|--------------|---------|------------------------------------|
| `name`       | `str`   | Nom complet du client              |
| `age`        | `int`   | Âge du client                      |
| `permis`     | `bool`  | Possession du permis de conduire   |
| `is_member`  | `bool`  | Statut membre (remise 10%)         |

**Méthodes :**
- `__str__()` → représentation lisible (M4)

---

### `Rental` (rental.py — M5)

| Attribut        | Type       | Description                        |
|-----------------|------------|------------------------------------|
| `customer`      | `Customer` | Le client qui loue                 |
| `vehicle`       | `Vehicle`  | Le véhicule loué (ou Car/LuxuryCar)|
| `duration_days` | `int`      | Durée de la location en jours      |

**Méthodes :**

**`total_cost() → float`** — 3ème expression arithmétique :
```
base_cost = vehicle.calculate_cost(duration_days)
remise    = base_cost × 0.10   (si is_member == True)
total     = base_cost - remise
```

**`__str__() → str`** — Récapitulatif complet de la location.

---

## ▶️ Instructions d'exécution

### Prérequis
- Python 3.8 ou supérieur
- Aucune bibliothèque externe requise

### Lancer le programme

```bash
python main.py
```

---

## 📋 Exemple de sortie

```
=== Système de Location de Véhicules ===

-- Test validate_year() --
  2020 valide ? True
  1800 valide ? False

========== RÉCAPITULATIF DE LOCATION ==========
  Client        : Alice Dupont
  Âge           : 30 ans
  Permis        : Oui
  Membre        : Oui (remise 10% appliquée)
  Véhicule      : Toyota Corolla (2020)
  Type          : Car
  Disponible    : Oui
  Durée         : 5 jour(s)
  Tarif/jour    : 50.00 €
  Coût de base  : 250.00 €
  Remise        : -25.00 €
  TOTAL À PAYER : 225.00 €
================================================
  → total_cost() : 225.00 €
```

---

## 👥 Répartition des membres

| Membre   | Fichier(s)                    | Branche Git                            |
|----------|-------------------------------|----------------------------------------|
| Membre 1 | `main.py`, `README.md` ébauche| `feature/main-and-inputs`              |
| Membre 2 | `vehicle.py`, `customer.py`   | `feature/vehicle-customer-classes`     |
| Membre 3 | `vehicle.py` (Car, LuxuryCar) | `feature/inheritance-car-luxury`       |
| Membre 4 | `vehicle.py`, `customer.py`   | `feature/magic-methods-decorator`      |
| Membre 5 | `rental.py`, `README.md` final| `feature/rental-integration-readme`    |

---

## 🔗 Commandes Git — Membre 5

```bash
# Se placer sur la bonne branche
git checkout -b feature/rental-integration-readme

# Après avoir récupéré les branches des autres
git merge feature/vehicle-customer-classes
git merge feature/inheritance-car-luxury
git merge feature/magic-methods-decorator

# Ajouter ses fichiers
git add rental.py README.md main.py
git commit -m "feat: add Rental class, integration tests and final README"
git push origin feature/rental-integration-readme
```
