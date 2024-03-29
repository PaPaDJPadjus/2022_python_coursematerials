"""KT0."""


def add_char_into_pos(char: str, pos: int, string: str) -> str:
    """
    Return a string where a given character is added into a given position in a string.

    In the case of empty string and position 1, return the given character.

    add_char_into_pos("a", 2, "kheksa") -> "kaheksa"
    add_char_into_pos("t", 8, "kaheksa") -> "kaheksat"
    add_char_into_pos("a", 1, "mps") -> "amps"
    add_char_into_pos("a", 1, "") -> "a"
    add_char_into_pos("k", 10, "kalla") -> "kalla"

    """
    if 0 > pos:
        return string
    if pos == len(string) + 1:
        return string + char
    if pos > len(string) + 1:
        return string
    else:
        letters_list = list(string)
        letters_list.insert(pos - 1, char)
        final_word = "".join(letters_list)
        return final_word


def nr_of_common_characters(string1: str, string2: str):
    """
    Return a number of common characters of string1 and string2.

    Do not take into account repeated characters.

    common_characters("iva", "avis") -> 3 # 'a', 'i', 'v' are common
    common_characters("saali", "pall") -> 2  # 'a', 'l' are common
    common_characters("memm", "taat") -> 0
    common_characters("memm", "") -> 0

    """
    if string1 == "" or string2 == "":
        return 0
    letters1 = []
    letters2 = []
    common_chars = 0

    for letter in string1:
        letters1.append(letter)
    letters1 = sorted(list(set(letters1)))

    for letter in string2:
        letters2.append(letter)
    letters2 = sorted(list(set(letters2)))

    for letter in letters2:
        if letter in letters1:
            common_chars += 1
    return common_chars


def nr_into_num_list(nr: int, num_list: list) -> list:
    """
    Return a list of numbers where the "nr" is added into the "num_list" so that the list keep going to be sorted.

    Built-in sort methods are not allowed.

    nr_into_num_list(5, []) -> [5]
    nr_into_num_list(5, [1,2,3,4]) -> [1,2,3,4,5]
    nr_into_num_list(5, [1,2,3,4,5,6]) -> [1,2,3,4,5,5,6]
    nr_into_num_list(0, [1,2,3,4,5]) -> [0,1,2,3,4,5,]

    """
    if not num_list:
        num_list.append(nr)
        return num_list
    if nr == 0:
        num_list.insert(nr, 0)
    for number in num_list:
        if number >= nr:
            num_list.insert(num_list.index(number), nr)
            break
    if nr not in num_list:
        num_list.append(nr)
    return num_list


def symbol_average_position_in_words(words):
    """
    Find the average position for each symbol.

    For the given text (list of words) the function has to find
    the average position for each symbol.

    If the list is: ["hello", "world"]
    then the positions for the symbols are:
    h: 0 (in the first word only)
    e: 1
    l: 2, 3, 3 (2, 3 in the first word, 3 in the second)
    o: 4, 1
    w: 0
    r: 2
    d: 4

    The average positions:
    h: 0
    e: 1
    l: 2.67
    o: 2.5
    w: 0
    r: 2
    d: 4
    Positions should be rounded to 2 places after the decimal point.

    The order of the keys in the dictionary is not important.

    symbol_average_position_in_words(["hello", "world"]) =>
    {'h': 0.0, 'e': 1.0, 'l': 2.67, 'o': 2.5, 'w': 0.0, 'r': 2.0, 'd': 4.0}

    symbol_average_position_in_words(["abc", "a", "bc", ""]) =>
    {'a': 0.0, 'b': 0.5, 'c': 1.5}

    symbol_average_position_in_words(["1", "a", "A"]) =>
    {'1': 0.0, 'a': 0.0, 'A': 0.0}

    :param words: list of words
    :return: dictionary with symbol average positions
    """
    dictionary_letters = {}
    letters = []
    for word in words:
        for letter in word:
            letters.append(letter)

    for word in words:
        index_letter = 0
        for letter in word:
            dictionary_letters[letter] = dictionary_letters.get(letter, 0) + index_letter
            index_letter += 1

    for key in dictionary_letters:
        dictionary_letters[key] = dictionary_letters[key] / letters.count(key)
    return dictionary_letters


print(symbol_average_position_in_words(["hello", "world"]))
