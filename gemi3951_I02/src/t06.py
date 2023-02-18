"""
-------------------------------------------------------
[Lab 1, Task 6]
-------------------------------------------------------
Author:  Ben Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-09-23"
-------------------------------------------------------
"""

CONSTANT = 1

principal = float(input("Morgage principal ($): "))
years = int(input("Number of years: "))
interest = float(input("Yearly interest rate (%): "))

interest = (interest / 12) / 100
years = years * 12
monthly = principal * (((interest * ((CONSTANT + interest)
                                     ** years)) / (((CONSTANT + interest)**years) - CONSTANT)))
print("The monthly payments are: $", monthly)
