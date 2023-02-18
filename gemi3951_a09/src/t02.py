"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-12-04"
-------------------------------------------------------
"""

fh = open("numbers.txt", "r", encoding="utf-8")
from functions import file_integers

print(file_integers(fh))
