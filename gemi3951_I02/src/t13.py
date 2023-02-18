"""
-------------------------------------------------------
[Lab 2, Task 13]
-------------------------------------------------------
Author:  Ben Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-09-23"
-------------------------------------------------------
"""

Midterm_mark = float(input("Midterm mark (%): "))
Exam_mark = float(input("Exam mark (%): "))

MIDTERM = .35
EXAM = .65

Final = ((MIDTERM * Midterm_mark) + (EXAM * Exam_mark))

print("Final Grade (%): ", Final)
