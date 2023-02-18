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


fh = open("words.txt", "r", encoding="utf-8")

from functions import find_longest

print(find_longest(fh))
