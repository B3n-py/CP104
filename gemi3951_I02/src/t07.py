"""
-------------------------------------------------------
[Lab 2, Task 7]
-------------------------------------------------------
Author:  Ben Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-09-23"
-------------------------------------------------------
"""

flyers = int(input("Number of flyers: "))
volunteers = int(input("Number of volunteers: "))

flyers_per = flyers // volunteers
flyers_left = flyers % volunteers

print("Flyers per volunteer: ", flyers_per)
print("Flyers left over: ", flyers_left)
