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
    if length > 11 or length < 11:
        return "Incorrect ID code!"
    if controlled_weight == 0 or controlled_weight > 10:
        return "Incorrect ID code!"
    if controlled_weight < 10 and int(controlled_weight) == int(control_id_code[-1:]):
        return control_id_code
    if int(controlled_weight) != int(control_id_code[-1:]):
        return "Needs the second algorithm!"



if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print(the_first_control_number_algorithm(""))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("12345678912"))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm("ID code is: 49403136526"))  # -> "49403136526"
    print(the_first_control_number_algorithm("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"
    print(the_first_control_number_algorithm("51201166313"))  # -> "2nd"
    print(the_first_control_number_algorithm("Peeter's ID is 50205160274"))  # -> "Needs
    # the second algorithm!"
