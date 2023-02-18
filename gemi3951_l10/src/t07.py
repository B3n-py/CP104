"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-11-25"
-------------------------------------------------------
"""

fh = open("numbers.txt", "r+", encoding="utf-8")

from functions import append_max_num

num = append_max_num(fh)


print(f"{num} is appended")
