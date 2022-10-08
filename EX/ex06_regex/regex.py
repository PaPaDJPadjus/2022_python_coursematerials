"""Regex, yay."""
import re


def find_words(text: str) -> list:
    """
    Given string text, return all the words in that string.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string
     find words from
    :return: list of words found in given string
    """
    pattern = r"[A-^ZÜÕÖÄ][a-zõüöä]+"
    final = re.findall(pattern, text)
    return final


def find_words_with_vowels(text: str) -> list:
    """
    Given string text, return all the words in that string that start with a vowel.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string to find words from
    :return: list of words that start with a vowel found in given string
    """
    pattern = r"[A^E^O^U^I^Ü^Õ^Ö^Ä^][a-zõüöä]+"
    final = re.findall(pattern, text)
    return final


def find_sentences(text: str) -> list:
    """
    Given string text, return all sentences in that string.

    A sentence always starts with a capital letter and ends with punctuation (.!?).
    Note that a sentence may also contain all the typical symbols (like commas, colons, numbers, etc.).
    A sentence may also end in multiple punctuation (example: "Wait...").

    Sentences must be found using regex.

    :param text: given string to find sentences from
    :return: list of sentences found in given string
    """
    pattern = r"[A-^ZÜÕÖÄ][\wõüäö ,:-]+[(.!?)$]{1,4}"
    final = re.findall(pattern, text)
    return final


def find_words_from_sentence(sentence: str) -> list:
    """
    Given a sentence, return all words in that sentence.

    Here, a word is considered to be a normal word in a sentence,
    that is separated from other words by a whitespace (or commas, etc.).
    Note that numbers are also considered as words here, but commas, etc. are not
    a part of a word.

    Words must be found using regex.

    :param sentence: given sentence to find words from
    :return: list of words found in given sentence
    """
    pattern = r"[A-^ZÜÕÖÄa-züõäö\d][\wõüäö]*"
    final = re.findall(pattern, sentence)
    return final


def find_words_from_sentences_only(text: str) -> list:
    """
    Given string text, return all words in that string that are a part of a sentence in that string.

    A sentence is defined in function find_sentences().
    A word is defined in function find_words_from_sentence().

    :param text: given string to find words from
    :return: list of words found in sentences from given string
    """
    pattern = r"[A-^ZÜÕÖÄ][\d*a-züõäö ,:-]*"
    first = re.findall(pattern, text)
    first = " ".join(first)
    final = find_words_from_sentence(first)
    return final


def find_years(text: str) -> list:
    """
    Given string text, return a list of all 4-digit numbers (years) in that string.

    Only 4-digit numbers are considered years here.
    If there is a 5-digit number then that is not considered a year,
    nor will it give two years. So you can not split them up.

    Years must be found using regex.

    Hint: use lookbehind and lookahead to check what comes before and after the numbers.

    :param text: given string to find years from
    :return: list of years (integers) found in given string
    """
    pattern = r"(?<!\d)([\d+]{4})(?!\d)"
    final = []
    first = re.findall(pattern, text)
    for el in first:
        final.append(int(el))
    return final


def find_phone_numbers(text: str) -> dict:
    """
    Given string text, return a dictionary of all the phone numbers in that text.

    Phone number might be preceded by area code. Area code is a combination of plus sign and three numbers.
    The phone number itself is a combination of 7-8 numbers.
    The phone number might be separated from the area code with a whitespace, but not necessarily.

    The function must return a dictionary where keys are the area codes
    and values are lists of the phone numbers with the corresponding area number.
    If a phone number does not have an area code given, its area code would be empty string,
    so in dictionary it would be like that: {"": ["56332456"]}.

    Phone numbers must be found using regex.

    :param text: given string to find phone numbers from
    :return: dict containing the numbers
    """
    numbers_pattern = r"\+[\d]{3} [\d]{7,8}|\+[\d]{3}[\d]{7,8}|[\d]{7,8}"
    location_pattern = r"\+[\d]{3}"
    locations = re.findall(location_pattern, text)
    locations = set(locations)
    locations = list(locations)
    dictionary = {}
    numbers = []
    first_n = []
    extras = []
    i = 0
    legit_nr = re.findall(numbers_pattern, text)
    for nr in legit_nr:
        if nr[:4:] in locations:
            if nr[:4:] not in first_n:
                first_n.append(nr[:4:])
                numbers.append([nr[:4:]])
                index = first_n.index(nr[:4:])
                numbers[index].append([nr[4::]])
            else:
                index = first_n.index(nr[:4:])
                numbers[index][index + 1].append(nr[4::])
        else:
            extras.append(nr)
    if len(extras) >= 1:
        numbers.append([""])
        first_n.append("")
        numbers[len(first_n) - 1].append(extras)
    for loc in first_n:
        for el in numbers[i]:
            dictionary[loc] = el
        i += 1
    return dictionary


if __name__ == '__main__':
    print(find_phone_numbers("+372 56887364  +37256887364  +33359835647  56887364 +11 1234567 +327 1 11111111"))
    # {'+372': ['56887364', '56887364'], '+333': ['59835647'], '': ['56887364', '1234567', '11111111']}
