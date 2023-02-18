"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-12-03"
-------------------------------------------------------
"""
import string
import random


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []
    for x in range(rows):
        cols_elements = []
        for y in range(cols):
            cols_elements.append(0)
        matrix.append(cols_elements)
    return matrix


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    count = 0
    matrix = []
    if (value_type == "float"):
        for x in range(rows):
            matrix.append([])
            for y in range(cols):
                matrix[count].append(random.uniform(low, high))
            count += 1
    if (value_type == "int"):
        for x in range(rows):
            matrix.append([])
            for y in range(cols):
                matrix[count].append(random.uniform(low, high))
            count += int(1)
    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """

    print(" ", end="")

    for i in range(len(matrix[0])):
        print(f'{i:>8}', end="")

    print()

    for i in range(len(matrix)):
        print(f'{i}', end="")

        for j in range(len(matrix[i])):
            char = matrix[i][j]
            print(f"{char:8.2f}", end="")

        print()

    return


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    x = random.choice(string.ascii_letters)
    print(" ", end="")

    for i in range(len(matrix[0])):
        print(f'{i:>8}', end="")

    print()

    for i in range(len(matrix)):
        print(f'{i}', end="")

        for j in range(len(matrix[i])):
            x = random.choice(string.ascii_letters)
            char = matrix[i][j]
            matrix[i][j] = x
            print(f"{x:>8s}", end="")

        print()

    return


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    list = []
    for i in matrix:
        print(max(i))
        if max(i) == true:
            list = []
            max = i.index(max[i])
            list.append(max)
    return
