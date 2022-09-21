"""Example TK."""


def workday_count(days: int):
    """
    Given number of days.

    Return how many of these days are workdays.
    Workdays are first five days of the weeks, last two are not.
    Always start from the start of the week.

    workday_count(9) => 7
    workday_count(3) => 3
    workday_count(7) => 5
    workday_count(15) => 11

    :param days: given number of days
    :return: workdays in given days
    """
    workday = 0
    counter = 0
    wk_break = 0
    while counter != days:
        workday += 1
        counter += 1
        wk_break += 1
        if wk_break == 5:
            counter += 2
            wk_break = 0
    return workday

print(workday_count(15))

def sorta_sum(a: int, b: int) -> int:
    """
    Given 2 ints, a and b, return their sum.

    However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

    sorta_sum(3, 4) → 7
    sorta_sum(9, 4) → 20
    sorta_sum(10, 11) → 21

    :param a: Integer
    :param b: Integer
    :return: Sum or 20
    """
    sum_of = a + b
    if sum_of in range(10, 20):
        return 20
    else:
        return sum_of


def extra_end(s: str) -> str:
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.

    The string length will be at least 2.

    extra_end('Hello') → 'lololo'
    extra_end('ab') → 'ababab'
    extra_end('Hi') → 'HiHiHi'

    :param s: Input string
    :return: 3 copies of last 2 chars.
    """
    for el in s:
        if len(s) < 2:
            return "Not enough characters!"
    else:
        return s[-2:] * 3


def last_indices_elements_sum(nums: list) -> int:
    """
    Return sum of elements at indices of last two elements.

    Take element at the index of the last element value
    and take element at the index of the previous element value.
    Return the sum of those two elements.

    If the index for an element is out of the list, use 0 instead.

    The list contains at least 2 elements.

    last_indices_elements_sum([0, 1, 2, 0]) => 2 (0 + 2)
    last_indices_elements_sum([0, 1, 1, 7]) => 1 (just 1)
    last_indices_elements_sum([0, 1, 7, 2]) => 7 (just 7)
    last_indices_elements_sum([0, 1, 7, 8]) => 0 (indices too large, 0 + 0)

    :param nums: List of non-negative integers.
    :return: Sum of elements at indices of last two elements.
    """
    first_nr_el = int(nums[-1])
    sec_nr_el = int(nums[-2])
    if first_nr_el >= len(nums):
        first_nr = 0
    else:
        first_nr = nums[first_nr_el]

    if sec_nr_el >= len(nums):
        sec_nr = 0
    else:
        sec_nr = nums[sec_nr_el]
    return first_nr + sec_nr


def divisions(numbers: list) -> int:
    """
    You are given a list of unique integers.

    Find how many pairs of numbers there are in that list, such that for each pair, one of its members is divisible by
    the other.

    Note that "n and m" is considered the same pair as "m and n".

    divisions([]) => 0
    divisions([5]) => 0

    divisions([3, 14, 12, 6]) => 3 (The pairs are {3, 12}, {3, 6} and {12, 6})
    divisions([2, 3, 8]) => 1 (The only valid pair is {2, 8})
    divisions([25, 22, 4, 400, 50]) => 4 (The pairs are {25, 400}, {25, 50}, {4, 400} and {400, 50})

    divisions([5, 7, 1]) => 2 (The pairs are {5, 1} and {7, 1})

    :param numbers: List of integers
    :return: Amount of pairs
    """
    print(len(numbers))
    i = 1
    pairs = 0
    if len(numbers) == 0 or len(numbers) == 1:
        return 0

    for el in numbers:
        if numbers[i] // el and numbers[i] % el == 0:
            pairs += 1
            i += 1

    return pairs


print(divisions([2, 3, 8]))
