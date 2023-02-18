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

date1 = int(input("Please enter the date in format DDMMYYYY: "))

year = date1 % 10000
day = date1 // 1000000
month = (date1 - year) // 10000 % 100

print(f"The reformatted date: {year:04}/{month:02}/{day:02}")
