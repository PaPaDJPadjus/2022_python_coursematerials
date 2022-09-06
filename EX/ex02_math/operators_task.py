"""Math operators."""
from math import floor


def add(x: int, y: int) -> int:
    """Add x to y."""
    return x + y


def sub(x: int, y: int) -> int:
    """Subtract y from x."""
    return x - y


def multiply(x: int, y: int) -> int:
    """Multiply x by y."""
    return x * y


def div(x: int, y: int) -> int:
    """Divide x by y."""
    return round(x / y)


def modulus(x: int, y: int) -> int:
    """Divide x by y and return remainder. Use an arithmetic operator."""
    return x % y


def floor_div(x: int, y: int) -> int:
    """Divide x by y and floor the value. Use an arithmetic operator."""
    return floor(x / y)


def exponent(x: int, y: int) -> int:
    """Calculate x raised to the power of y."""
    return x ** y


def first_greater_or_equal(x: int, y: int) -> str:
    """If x is greater or equal than y then return True. If not then return False."""
    if x >= y:
        print("True")
    else:
        return "False"


def second_less_or_equal(x: int, y: int) -> str:
    """If y is less or equal than x then return True. If not then return False."""
    if y <= x:
        print("True")
    else:
        return "False"


def x_is_y(x: int, y: int) -> str:
    """If x value is the same as y value then return True. If not then return False."""
    if x == y:
        print("True")
    else:
        return "False"


def x_is_not_y(x: int, y: int) -> str:
    """If x value is not the same as y value then return True. If not then return False."""
    if x == y:
        print("False")
    else:
        return "True"


def if_else(a: int, b: int, c: int, d: int) -> int:
    """
    Create a program that has 4 numeric parameters.

    Multiply parameters 1-2 (multiply a by b) by each other and divide parameters 3-4 (divide c by d) by each other.
    Next check and return the greater value. If both values are the same then return 0 (number zero).
    """
    parameters_ab = multiply(a, b)
    parameters_cd = div(c, d)
    if parameters_ab > parameters_cd:
        print(f"{parameters_ab} is greater")
    elif parameters_ab < parameters_cd:
        print(f"{parameters_cd} is greater")
    elif parameters_ab == parameters_cd:
        return 0


def surface(length: int, width: int) -> int:
    """Missing parameters + surface."""
    return length * width


def volume(length: int, width: int, height: int) -> int:
    """Add the missing parameters to calculate the volume of a cuboid. Calculate and return the value of the volume."""
    return length * width * height


def calculate(a: int, x: int, y: int) -> int:
    """Takes input from user and picks the equation and numbers."""
    if a == 0:
        print(add(x, y))
    elif a == 1:
        print(sub(x, y))
    elif a == 2:
        print(multiply(x, y))
    elif a == 3:
        return div(x, y)


print(f"Possible equations:\n 0. Add\n 1. Subtract\n 2. Multiply\n 3. Divide")
a = input("Enter which equation: ")
x = input("Enter the first number: ")
y = input("Enter the second number: ")

print(calculate(int(a), int(x), int(y)))
