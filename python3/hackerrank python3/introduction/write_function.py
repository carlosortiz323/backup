#answer to "Python > Introduction > Write a function"
#language: Python3

def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        leap = True

    if year % 100 == 0:
        if year % 400 == 0:
            return leap
        else:
            leap = False





    return leap
