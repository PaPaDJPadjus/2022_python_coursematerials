"""KT2."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    if 4 > len(s):
        return s[::-1]
    return s[-2:] + s[2:len(s) - 2] + s[:2]


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    take_partial("Hello world", 3, 3) => "lo ld"
    """
    if not text:
        return ""
    new_text = ""
    counter = 0
    if take_count == 0:
        return ""

    for el in text[leave_count:]:
        if take_count > len(text[leave_count:]):
            take_count = len(text[leave_count:])
        new_text += el
        counter += 1
        if counter == take_count:
            if len(text[leave_count + counter:]) >= take_count:
                return new_text + take_partial(text[leave_count + counter:], leave_count, take_count)
            else:
                return new_text


def min_diff(nums: list) -> int:
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    if len(nums) == 2:
        if nums[0] - nums[1] > nums[1] - nums[0]:
            return nums[0] - nums[1]
        return nums[1] - nums[0]

    for el in nums:
        if nums.count(el) >= 2:
            return 0

    nums = sorted(nums)
    diffs = []
    for el in nums:
        for el2 in nums:
            if 0 >= el2 - el:
                continue
            diffs.append(el2 - el)
    return min(diffs)


def get_symbols_by_occurrences(text: str) -> dict:
    """
    Return dict where key is the occurrence count and value is a list of corresponding symbols.

    The order of the counts and the symbols is not important.

    get_symbols_by_occurrences("hello") => {1: ['e', 'o', 'h'], 2: ['l']}
    get_symbols_by_occurrences("abcaba") => {2: ['b'], 1: ['c'], 3: ['a']}
    """
    pass


if __name__ == '__main__':
    print(switch_lasts_and_firsts("ambulance"))  # => "cebulanam"
    print(switch_lasts_and_firsts("firetruck"))  # => "ckretrufi"
    print(switch_lasts_and_firsts("car"))  # => "rac"

    print(take_partial("abcdef", 2, 3))  # => "cde"
    print(take_partial("whatever sentence?", 0, 1))  # => "abcdef"
    print(take_partial("abcdef", 1, 0))  # => ""
    print(take_partial("AWGeag aweJKBWEG KBaWEGKBxd asega", 3, 3))  # => "lo ld"

    print(min_diff([1, 2, 3]))  # => 1
    print(min_diff([1, 9, 17]))  # => 8
    print(min_diff([100, 90]))  # => 10
    print(min_diff([1, 100, 1000, 1]))  # => 0

    print(get_symbols_by_occurrences("hello"))  # => {1: ['e', 'o', 'h'], 2: ['l']}
    print(get_symbols_by_occurrences("abcaba"))  # => {2: ['b'], 1: ['c'], 3: ['a']}
