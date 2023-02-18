"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-12-19"
-------------------------------------------------------
"""
import time


def spinning_donut():
    characters = ['\\', '|', '/', '-']
    while True:
        for character in characters:
            print(f'\r|{character}|', end='', flush=True)
            time.sleep(0.1)


spinning_donut()
