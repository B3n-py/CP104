"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-11-05"
-------------------------------------------------------
"""


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """

    total = 0

    for i in range(1, num + 1, 2):
        total = total + i
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    '''
    x = 1
    v = height - 1
    c = 0
    for i in range(1):
        while c < height:
            print(" " * v + char * x)
            c += 1
            v = v - 1
            x = x + 2
    return
    '''
    x = 1
    c = " "
    v = height - 1
    for i in range(1, height + 1):
        print(f"{c* v}{char*x}")
        x += 2
        v -= 1
    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(n, 1, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(
            f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
    print(f"1 bottle of beer on the wall, 1 bottle of beer")
    print(f"Take one down, pass it around, no more bottles of beer on the wall!")
    return


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print("AGE    SAlARY")
    print("-------------")
    AGE = age
    rate = increase / 100 + 1
    num = salary
    for i in range(age, 66):
        print(f"{AGE:<5d}{num:,.2f}")
        AGE += 1

        num = num * rate
    return


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """

    x = 0
    total = 0
    list = []
    list2 = []
    list3 = []
    greater = 0
    less = 0
    for i in range(1, n + 1):
        x = float(input("enter a number"))
        list.append(x)
        total += x
        average = total / n
        list2.append(x)
        list3.append(x)
        min = list3[0]
        for c in list2:
            if x > c:
                list2.remove(c)
                list.append(x)
                greater = x

        for i in range(1, len(list3)):
            if(list3[i] < min):
                min = list3[i]
                less = min
    return (less, greater, total, average)
