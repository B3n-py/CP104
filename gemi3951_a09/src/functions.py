"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Geminiuc
ID:      169033951
Email:   gemi3951@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""


def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """

    # read the content of the file opened
    read = fh.readlines()

    count = 0

    while count != linecount:
        for i in range(linecount):
            print(read[i])
            count += 1
    return


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    numbers = []
    for i in fh:
        line = i.strip().split(',')
        for c in line:
            if c.isdigit() and int(c) > 0:
                numbers.append(int(c))
    return numbers


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    for i in fh:
        for c in i:
            if c.isupper() == True:
                ucount += 1
            elif c.islower() == True:
                lcount += 1
            elif c.isdigit() == True:
                dcount += 1
            elif c == " ":
                wcount += 1
    return ucount, lcount, dcount, wcount


def number_lines(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """

    Lines = fh_in.readlines()
    count = 0

    for line in Lines:
        count += 1

        print(f"[{count}] {line}")

    return


fh = open("students.txt", "r", encoding="utf-8")


def student_info(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_info(students)
    -------------------------------------------------------
    Parameters:
        students - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """

    low_grade = float('inf')
    l_id = -1
    high_grade = float('-inf')
    h_id = -1
    total = 0
    count = 0

    for line in students.readlines():
        info = line.split(",")
        total += float(info[-1])
        count += 1
    if(float(info[-1]) < low_grade):
        low_grade = float(info[-1])
        l_id = info[-2]

    if(float(info[-1]) > high_grade):
        high_grade = float(info[-1])
        h_id = info[-2]

    avg = round(total / count, 2)
    return l_id, h_id, avg
