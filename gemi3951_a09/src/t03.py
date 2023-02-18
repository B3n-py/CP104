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

fh = open("addresses.txt", "r", encoding="utf-8")
from functions import file_stats
print(file_stats(fh))
