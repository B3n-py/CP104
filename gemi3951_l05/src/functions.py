"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-10-23"
-------------------------------------------------------
"""


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    GRAVITY = 9.8
    weight = (mass * GRAVITY)
    message = "average"
    if weight > 1000:
        message = "heavy"
    elif weight < 10:
        message = "light"
    else:
        message = "average"
    return (weight, message)


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    if abs((target - v1)) <= abs((target - v2)):
        result = v1
    else:
        result = v2
    return result


def wind_speed(speed):
    '''
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    -----------------------------------------------------
    '''

    Category = "Breeze"
    if speed > 117:
        Category = "Hurricane"
    elif speed >= 89:
        Category = "Whole Gale"
    elif speed >= 62:
        Category = "Gale Winds"
    elif speed > 39:
        Category = "Strong Wind"
    elif speed < 0:
        Category = "Unknown"
    else:
        Category = "Breeze"
    return Category


def loan():
    '''
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    '''
    money = int(input("Salary"))
    years = int(input("years"))
    qualified = ''
    if years >= 5:
        if money >= 30000:
            qualified = True
    else:
        qualified = False
    return qualified


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    
    BURGER = 6
    WINGS = 8
    FRIES = 1.5
    SALAD = 2

    order = input("Order Burger (B) or Wings (W): ")
    if order == "B":
        cost = BURGER
    elif order == "W":
        cost = WINGS
    combo = input("Make it a combo? (Y/N): ")
    if combo == "Y":
        side = input("Select Fries (F) or salad (S): ")
        if side == "F":
            price = float(cost + FRIES)
            if side == "S":
                price = float(cost + SALAD)
        elif combo == "N":
            price = float(cost)
    return print(price)
price = fast_food()
print(cost)

    BURGER = 6
    WINGS = 8
    FRIES = 1.50
    SALAD = 2

    order = input("Order Burger (B) or Wings (W): ")
    if order == "B":
        cost = BURGER
    elif order == "W":
        cost = WINGS
    combo = input("Make it a combo? (Y/N): ")

    if combo == "Y":
        side = input("Select Fries (F) or salad (s): ")
        if side == "F":
            cost += FRIES
        elif side == "S":
            cost += SALAD

    return print(cost)
   
    BURGER = 6
    WINGS = 8
    FRIES = 1.5
    SALAD = 2
    order = input("Order Burger (B) or Wings (W): ")
    if order == "B":
        cost = BURGER
    else:
        cost = WINGS
        combo = input("Make it a combo? (Y/N): ")
        if combo == "Y":
            side = input("Select Fries (F) or salad (s): ")
            if side == "F":
                price = float(cost + FRIES)
            else:
                price = float(cost + SALAD)
        else:
            price = WINGS
    return print(f"{price}")
    
