"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""

Principal = float(input("principle"))
Interest = float(input("interest"))
years = int(input("years"))
compound = int(input("compound"))

A = Principal * ((1 + (Interest / compound))**(compound * years))


print(f"{A}")
