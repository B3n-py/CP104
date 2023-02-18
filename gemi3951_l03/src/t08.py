"""
-------------------------------------------------------
Lab 3, Task 8
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-10-01"
-------------------------------------------------------
"""

Dirt = float(input("Enter amount of dirt (m^3): "))
Gravel = float(input("Enter amount of gravel (m^3): "))
Sand = float(input("Enter amount of Sand (m^3): "))

Total = Dirt + Sand + Gravel

print("Material Cubic Metres")
print(f"Dirt{Dirt:>11.1f}")
print(f"Gravel{Gravel:>9.1f}")
print(f"Sand{Sand:>11.1f}")
print(f"Total{Total:>10.1f}")
