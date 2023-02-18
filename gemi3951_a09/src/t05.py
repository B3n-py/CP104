"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""

fh = open("students.txt", "r", encoding="utf-8")
from functions import student_info
print(student_info(fh))
