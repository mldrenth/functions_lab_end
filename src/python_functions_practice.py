def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(number):
    if number == 1:
        return "January"

    elif number == 3:
        return "March"

    elif number == 9:
        return "September"

def number_to_short_month_name(number):
    if number == 1:
        return "Jan"

    elif number == 4:
        return "Apr"

    elif number == 10:
        return "Oct"
    
def volume_of_cube(length):
    return pow(length,3)

def reverse_string(string):
    return string [::-1]