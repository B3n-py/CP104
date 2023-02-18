"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-11-04"
-------------------------------------------------------
"""


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """

    x = current
    y = target
    num = rate / 100 + 1
    count = 0
    while x < y:
        x = num * x
        count += 1
    return count


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    list = []
    total = 0
    avg = 0
    x = float(input("First positive value: "))
    list.append(x)
    if x >= 0:
        y = float(input("Next positive value: "))
        list.append(y)
        while y >= 0:
            y = float(input("Next positive value: "))
            list.append(y)
    for i in list:
        if i < 0:
            list.remove(i)
    for i in (list):
        total += i
    avg = total / len(list)
    print(min(list), max(list), total, avg)
    return


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    list = []
    total = 0
    status = ''
    x = float(input("Enter an Expense (0 to quit): "))
    list.append(x)
    if x != 0:
        y = float(input("Enter another Expense (0 to quit): "))
        list.append(y)
        while y != 0:
            y = float(input("Enter another Expense (0 to quit): "))
            list.append(y)
    for i in list:
        total += i
    remain = available - total
    if remain > 0:
        status = "surplus"
    elif remain < 0:
        status = "deficit"
    else:
        status = "balanced"
    return (total, remain, status)


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    x = float(input(f"Enter value between {low} and {high}: "))
    while x < low or x > high:
        if x > high:

            print("value entered is too high")
            x = float(input(f"Enter value between {low} and {high}: "))
        elif x < low:

            print("value entered is too low")
            x = float(input(f"Enter value between {low} and {high}: "))
        else:
            break
    return x


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    employeeID = int(input("Employee id: "))
    total = 0
    employees = 0
    OVERTIME = 40
    OVERTIME_RATE = 1.5
    TAX_RATE = 3.625
    while employeeID != 0:
        pay = 0
        wage = int(input("Hourly age rate: "))
        hours = int(input("Hours worked: "))
        if hours > OVERTIME:
            pay = (OVERTIME + (hours - OVERTIME) * OVERTIME_RATE) * wage
        else:
            pay = hours * wage
        pay -= (pay * (TAX_RATE / 100))
        total = total + pay
        employees += 1
        print(f"Net payment for employee {employeeID}: ${pay:,.2f}")
        employeeID = int(input("Employee id: "))
        average = total / employees
    return (total, average)
