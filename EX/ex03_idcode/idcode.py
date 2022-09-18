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
    if year_number < 00:
        return False
    if year_number > 99:
        return False
    else:
        return True


def is_valid_month_number(month_number: int):
    """Check if given value is correct for month number in ID code."""
    if month_number < 00:
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
        return "Male"
    if first_nr == 2 or first_nr == 4 or first_nr == 6:
        return "Female"


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> True

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True
