"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-11-23"
-------------------------------------------------------
"""
fh = open("customers.txt", "r", encoding="utf-8")
id_number = int(input("Enter a number: "))

from functions import customer_by_id

print(customer_by_id(fh, id_number))
