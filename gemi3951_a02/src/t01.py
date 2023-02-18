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
sales = float(input("Total sales"))
TAX = float(input("Annual tax"))

total = sales * (TAX / 100)
print(f"Tax: {total}")
