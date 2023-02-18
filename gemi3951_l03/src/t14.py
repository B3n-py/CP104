"""
-------------------------------------------------------
Lab 3, Task 14
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-10-01"
-------------------------------------------------------
"""

Minutes = int(input("Enter number of minutes "))

Days = Minutes / 1440

Min = Minutes % 1440

hours = Min / 60

Days = int(Days)
hours = int(hours)


Mins = Minutes - (Days * 1440) - (hours * 60)


print(
    f"There are {Days:d} days, {hours:d} hours, and {Mins:d} minutes in {Minutes:d} minutes")
