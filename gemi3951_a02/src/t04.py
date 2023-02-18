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

numcake = int(input("Number of pieces of cake: "))
numpeople = int(input("Number of party-goers "))

received = numcake // numpeople
remainder = numcake % numpeople

print(f"Everyone got {received} pieces of cake with {remainder} pieces left")
