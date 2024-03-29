"""TK1."""


def format_time(minutes: int) -> str:
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    Correct format would be '{hours}h {minutes}min'.
    However, if there is not enough minutes to form an hour, show only minutes.
    In that case the format would be '{minutes}min'.
    But when there are no remaining minutes, show only hours.
    In that case the format would be '{hours}h'.
    One hour contains of 60 minutes.

    Examples:
    1) given 112 minutes, return '1h 52min'.
    2) given 23 minutes, return '23min'.
    3) given 180 minutes, return '3h'.

    :param minutes: given minutes
    :return: formatted time in hours and minutes
    """
    if minutes < 60:
        time = str(minutes) + "min"
        return time

    if minutes % 60 == 0:
        time = str(minutes // 60) + "h"
        return time

    hours = minutes // 60
    left_min = minutes % 60
    time = str(hours) + "h " + str(left_min) + "min"
    return time


def caught_speeding(speed, is_birthday):
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if speed <= 60:
        return 0
    if speed <= 65 and is_birthday is True:
        return 0
    if 80 >= speed >= 61:
        return 1
    if 85 >= speed >= 66 and is_birthday is True:
        return 1
    if speed >= 81:
        return 2
    if speed <= 86 and is_birthday is True:
        return 1


def first_half(text: str) -> str:
    """
    Return the first half of an string.

    The length of the string is even.

    first_half('HaaHoo') => 'Haa'
    first_half('HelloThere') => 'Hello'
    first_half('abcdef') => 'abc'
    """
    index = int((len(text) / 2))
    return text[0:index]


def num_as_index(nums: list) -> int:
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2 (1 is smaller, use it as index)
    num_as_index([4, 5, 6]) => 4 (4 is smaller, but cannot be used as index)
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    el_one = int(nums[0])
    last = len(nums) - 1
    el_two = int(nums[last])
    if el_one < el_two:
        if el_one > last:
            return el_one
        return nums[el_one]

    if el_two > last:
        return el_two
    return nums[el_two]


def remove_in_middle(text, to_remove):
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA"

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    last_el = to_remove[-1:]
    full_text = ""
    last_el_p = last_el + " "
    text_replace = text.replace(last_el, last_el_p)
    text_split = text_replace.split()
    print(text_split)
    if to_remove not in text_split:
        return text
    while text_split.count(to_remove) >= 3:
        text_split.remove(to_remove)
    for el in text_split:
        full_text += el
    return full_text
