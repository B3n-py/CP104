"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-10-09"
-------------------------------------------------------
"""

flength = float(input("Enter foundation length (m): "))
fwidth = float(input("Enter foundation width (m): "))
fheight = float(input("Enter foundation height (m): "))
wheight = float(input("Enter wall height (m): "))
concretecost = float(input("Enter the cost of concrete ($/m^3): "))
brickcost = float(input("Enter the cost of bricks ($/m^2): "))

fvolume = fwidth * flength * fheight
ccostcalc = fvolume * concretecost
wsurfacearea = 2 * (fwidth * wheight) + 2 * (flength * wheight)
bcostcalc = wsurfacearea * brickcost
totalcost = ccostcalc + bcostcalc

print(f"Concrete needed for foundation (m^3): {fvolume:,.2f}")
print(f"Cost of concrete: {ccostcalc:,.2f}")
print(f"Bricks needed for walls (m^2): {wsurfacearea:,.2f}")
print(f"Cost of bricks: {bcostcalc:,.2f}")
print(f"Total cost: ${totalcost:,.2f}")
