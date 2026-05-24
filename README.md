# Girls_team
python_projet
# 🚗 AutoRent — Système de Location de Voitures

Projet Group Assignment 1 — PRG1406 Advanced Programming  
Burkina Institute of Technology | Mai 2026

## Description
Application console Python qui simule une agence de location de voitures.
L'utilisateur saisit ses informations, choisit un véhicule, et obtient
un récapitulatif complet de sa réservation.

## Classes
| Classe | Fichier | Rôle |
|---|---|---|
| `Vehicle` | vehicle.py | Classe parente — attributs communs |
| `Car` | vehicle.py | Enfant de Vehicle — voiture standard |
| `LuxuryCar` | vehicle.py | Enfant de Car — véhicule premium |
| `Customer` | customer.py | Données du client |
| `Rental` | rental.py | Réservation (client + véhicule + durée) |

## Comment lancer le programme
```bash
python main.py
```

## Membres du groupe
- Membre 1 — main.py
- Membre 2 — vehicle.py, customer.py
- Membre 3 — héritage Car, LuxuryCar
- Membre 4 — magic methods, décorateurs
- Membre 5 — rental.py, intégration
