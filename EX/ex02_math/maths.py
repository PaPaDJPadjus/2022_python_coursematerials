def average(a: int, b: int, c: int, d: int) -> float:
    """
    Implement a function that has 4 numeric parameters.

    Each parameter must be multiplied by number of its position in the function (x, y, z = 1, 2, 3).
    Calculate and return the average.

    Examples:
    average(0, 0, 0, 4) === 4
    average(1, 2, 3, 4) == 7.5
    average(5, 0, 5, 1) == 6
    """
    b *= 2
    c *= 3
    d *= 4
    return (a + b + c + d) / 4


def school_pressure(ects: int, weeks: int):
    """
    Implement a function to know how many hours are needed per week if each ECTS is 26 hours.

    If it's not possible in time then return -1.

    Examples:
    school_pressure(30, 12) == 65
    school_pressure(1, 1) == 26
    school_pressure(1, 0) == -1
    """
    weeks_hours = weeks * 168
    ects_hours = ects * 26
    pressure = ects_hours / weeks
    if ects == 0 and weeks == 0:
        return 0
    if ects == 0:
        return 0
    if weeks == 0:
        return -1
    if ects_hours > weeks_hours:
        return -1
    else:
        return pressure


def add_fractions(a: int, b: int, c: int, d: int):
    """
    Implement a function that takes 4 parameters.

    Parameters a and b denote the first fraction like a/b.
    Parameters c and d denote the second fraction like c/d.

    Find and return a fraction in string format that is the sum of a/b and c/d.

    NB! the fraction does not have to be in the simplest form.
    NB! the answer should not contain any commas.

    Examples:
    add_fractions(1, 3, 1, 3) # 1/3 + 1/3 => there are many correct answers like "2/3" and "6/9"
    add_fractions(2, 5, 1, 5) # 2/5 + 1/5 => there are many correct answers like "3/5" and "15/25"
    """
    bottom_fraction = b * d
    first_top_fraction = a * d
    second_top_fraction = c * b
    sum_fractions = first_top_fraction + second_top_fraction
    return str(sum_fractions) + "/" + str(bottom_fraction)
