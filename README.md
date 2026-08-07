# Girls_team
python_projet
# 🚗 AutoRent — Car Rental System

Projet Group Assignment 1 — PRG1406 Advanced Programming  
Burkina Institute of Technology | Mai 2026

## Description
A Python console application that simulates a car rental agency.
The user enters their details, selects a vehicle, and receives a complete
summary of their booking.
## Classes
| Classe | Fichier | Rôle |
|---|---|---|
| `Vehicle` | vehicle.py | Parent class — common attributes |
| `Car` | vehicle.py | Child of Vehicle — standard car |
| `LuxuryCar` | vehicle.py | Child of Car — premium vehicle|
| `Customer` | customer.py | Customer data |
| `Rental` | rental.py | Booking (customer + vehicle + duration) |

## How to Run the Program
```bash
python main.py
```

## Membres du groupe
- Traore Ramatou — main.py
- Ouedraogo Aminata— vehicle.py, customer.py
-Kabore Oceanne — héritage Car, LuxuryCar
- Roamba Sarifatou— magic methods, décorateurs
- Yougbare Eunice — rental.py, intégration

Requirements
Python 3.10 or newer
No external libraries required
How to Run the Program
1.Open a terminal.

2.Go to the project folder:
cd Girls_team
3.Run the program:
python main.py or py main.py


If python does not work, try:
python3 main.py

Features
Main menu with loop
Validated user inputs using while, try, and except
More than 10 input() calls
Uses Python data types: str, int, float, and bool
Uses inheritance: Vehicle, Car, LuxuryCar
Uses magic methods: __str__, __repr__, __eq__
Uses @staticmethod
Calculates total rental cost with member discount
Displays a final summary using f-strings

Group Members
Member 1 — main.py: entry point, menu, inputs, final summary
Member 2 — vehicle.py, customer.py: parent class and customer class
Member 3 — vehicle.py: inheritance with Car and LuxuryCar
Member 4 — vehicle.py, customer.py: magic methods and decorators
Member 5 — rental.py, README.md: rental class, integration, final documentation


Petite correction importante : au début, évite d’avoir :

```markdown
# Girls_team
python_projet
# 🚗 AutoRent — Car Rental System

Ça fait deux titres et ça paraît moins propre. Garde seulement :
# AutoRent — Car Rental System
