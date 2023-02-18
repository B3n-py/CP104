"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-10-09"
-------------------------------------------------------
"""

num = int(input("Enter a 2 digit number "))

digit = num % 10
value = num // 10

product = digit * value

print(f"The product of the digits of {num} is {product}")
