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

fh_in = open("wilde.txt", "r", encoding="utf-8")
fh_out = open("wilde_numbered.txt", "w", encoding="utf-8")

from functions import number_lines

number_lines(fh_in, fh_out)
