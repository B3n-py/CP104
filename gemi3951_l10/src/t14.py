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

n = int(input("Number of lines to copy: "))
fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open("new_words.txt", "w", encoding="utf-8")

from functions import file_copy_n

print(file_copy_n(fh_1, fh_2, n))
