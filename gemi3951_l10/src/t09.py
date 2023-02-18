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

fh = open("numbers.txt", "r", encoding="utf-8")
value = int(input("Value to count: "))

from functions import count_frequency_value

print(count_frequency_value(fh, value))
