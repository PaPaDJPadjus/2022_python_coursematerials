"""EX03 ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """
    id_code = ""
    numbers = "0123456789"
    length = 0
    for el in text:
        if el in numbers:
            id_code += str(el)
        else:
            continue

    for el in id_code:
        length += 1
    if length == 11:
        return id_code
    if length > 11:
        return "Too many numbers!"
    if length < 11:
        return "Not enough numbers!"


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    control_id_code = ""
    controlled_weight = 0
    length = 0
    numbers = "0123456789"
    i = 1

    for el in text:
        if el in numbers:
            control_id_code += str(el)
        else:
            continue

    for el in control_id_code:
        length += 1
    if length > 11 or length < 11:
        return "Incorrect ID code!"

    for el in control_id_code:
        if i < 10:
            controlled_number = int(el) * i
            controlled_weight += controlled_number
            i += 1
        else:
            i = 1
            controlled_number = int(el) * i
            controlled_weight += controlled_number
            break

    controlled_weight %= 11

    if controlled_weight < 10 and int(controlled_weight) == int(control_id_code[-1:]):
        return control_id_code
    if controlled_weight >= 10:
        return "Needs the second algorithm!"
    if int(controlled_weight) != int(control_id_code[-1:]):
        return "Incorrect ID code!"


def is_valid_year_number(year_number: int):
    """Check if given value is correct for year number in ID code."""
    if year_number < 0:
        return False
    if year_number > 99:
        return False
    else:
        return True


def is_valid_month_number(month_number: int):
    """Check if given value is correct for month number in ID code."""
    if month_number <= 0:
        return False
    if month_number > 12:
        return False
    else:
        return True


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    if birth_number <= 0:
        return False
    if birth_number > 999:
        return False
    else:
        return True


def is_valid_gender_number(first_nr: int):
    """Check if gender number is valid."""
    if first_nr == 0 or first_nr > 6:
        return False
    else:
        return True


def get_gender(first_nr: int):
    """Check if is male or female."""
    if first_nr == 0 or first_nr > 6:
        return False
    if first_nr == 1 or first_nr == 3 or first_nr == 5:
        return "male"
    if first_nr == 2 or first_nr == 4 or first_nr == 6:
        return "female"


def is_leap_year(year: int):
    """Check if given year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    birth_year = 0
    if gender_number == 1 or gender_number == 2:
        birth_year = 1800 + year_number
    if gender_number == 3 or gender_number == 4:
        birth_year = 1900 + year_number
    if gender_number == 5 or gender_number == 6:
        birth_year = 2000 + year_number
    return birth_year


def get_birth_place(birth_number: int):
    """Find the place where the person was born."""
    if is_valid_birth_number(birth_number) is False:
        return "Wrong input!"
    else:
        if birth_number <= 10:
            return "Kuressaare"
        if birth_number <= 20:
            return "Tartu"
        if birth_number <= 220:
            return "Tallinn"
        if birth_number <= 270:
            return "Kohtla-Järve"
        if birth_number <= 370:
            return "Tartu"
        if birth_number <= 420:
            return "Narva"
        if birth_number <= 470:
            return "Pärnu"
        if birth_number <= 710:
            return "Tallinn"
        else:
            return "undefined"


def is_valid_control_number(id_code: str):
    """Check if given value is correct for control number in ID code."""
    answer = the_first_control_number_algorithm(id_code)
    number = 3
    number_two = 1
    controlled_weight = 0
    if answer == id_code:
        return True
    if answer == "Needs the second algorithm!":
        for el in id_code:
            if number < 10:
                controlled_number = int(el) * number
                controlled_weight += controlled_number
                number += 1
            else:
                if number_two < 4:
                    controlled_number = int(el) * number_two
                    controlled_weight += controlled_number
                    number_two += 1
        controlled_weight %= 11
    if int(controlled_weight) == int(id_code[-1:]):
        return True
    if controlled_weight == 10:
        return True
    else:
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int):
    """Check if given value is correct for day number in ID code."""
    if day_number == 0 or month_number == 0:
        return False
    if month_number == 2 and day_number > 29:
        return False
    year = get_full_year(gender_number, year_number)
    if is_leap_year(year) is True:
        days = 29
    if is_leap_year(year) is False:
        days = 28
    if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 6 or month_number == 8:
        days = 31
    if month_number == 10 or month_number == 12:
        days = 31
    else:
        days = 30

    if days < day_number:
        return False
    else:
        return True


def is_id_valid(id_code: str):
    """Check if given ID code is valid and return the result (True or False)."""

    is_valid_control_number(id_code)
    is_valid_day_number(id_code)


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person."""
    # Write your code here


if __name__ == '__main__':
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(is_valid_day_number(4, 96, 2, 30))  # False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)

    #print("\nOverall ID check::")
    #print(is_id_valid("49808270244"))  # -> True
    #print(is_id_valid("12345678901"))  # -> False

    #print("\nFull message:")
    #print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    #print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
