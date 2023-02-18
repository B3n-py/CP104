"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-11-18"
-------------------------------------------------------
"""


def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    set = ''
    if url[-3:] == "com":
        set = 'business'
    elif url[-3:] == "org":
        set = 'non-profit'
    else:
        set = 'other'
    return set


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:10]
    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    something = 0
    for hello in product_code:
        if product_code.isupper():
            something += 1
    if something >= 3:
        category = True
    else:
        category = False
    somethingelse = 0
    for nathan in product_code:
        if product_code.isdigit():
            somethingelse += 1
    if somethingelse >= 4:
        digits = True
    else:
        digits = False
    final = 0
    for i in product_code:
        if product_code[7:10].isupper():
            final += 1
    if final == 1:
        qualifiers = True
    else:
        qualifiers = False
    return category, digits, qualifiers


print(validate_code('BFG9000x7'))


def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards. Case is ignored.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    list = []
    c = s.lower()
    list.append(c)
    p = c[::-1]
    value = ''
    if p == c:
        value = True
    else:
        value = False
    return value


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    for i in range(len(txt)):
        if txt[i].isupper() == True:
            uppr += 1
        elif txt[i].isalpha() == True and txt[i].isupper() == False:
            lowr += 1
        elif txt[i].isdigit() == True:
            dgts += 1
        elif txt[i].isspace() == True:
            whtspc += 1
    return uppr, lowr, dgts, whtspc
