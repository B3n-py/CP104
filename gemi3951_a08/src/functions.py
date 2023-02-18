"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-11-28"
-------------------------------------------------------
"""


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    list = []
    list.append(string)
    new_string = ''
    space = " "
    for i in list:
        for c in range(len(i)):
            new_string += i[c]
            if i[c].islower() == True and i[c + 1].isupper() == True:
                new_string += space

    return new_string


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    if string.endswith("sh") or string.endswith("ch") or string.endswith("s"):
        plural = string + "es"
    elif string.endswith("y") and not string.endswith("oy") or string.endswith("ay"):
        plural = string[:-1] + "ies"
    else:
        plural = string + "s"
    return plural


def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    common = ''
    while not string1.endswith(string2):
        string2 = string2[1:]
    common = string2
    return common


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = False
    if len(isbn) == 17:
        dashes_count = isbn.index("-")
        if dashes_count == 3:
            if isbn.replace('-', '').isdigit():
                if isbn[-2] == "-":
                    if isbn[0:3] == "978" or isbn[0:3] == "979":
                        valid = True

    return valid


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = True
    word = word_list[0]
    for i in range(1, len(word_list)):
        if word[-1] != word_list[i][0]:
            word_chain = False
        word = word_list[i]
    return word_chain
