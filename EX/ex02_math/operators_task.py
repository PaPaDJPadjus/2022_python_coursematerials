"""Math operators."""
from math import floor

def add(x: int, y: int):
    """Add x to y."""
    return x + y


def sub(x: int, y: int):
    """Subtract y from x."""
    negate = x - y
    pass


def multiply(x: int, y: int):
    """Multiply x by y."""
    multiplication = x * y
    pass


def div(x: int, y: int):
    """Divide x by y."""
    division = x / y
    pass


def modulus(x: int, y: int):
    """Divide x by y and return remainder. Use an arithmetic operator."""
    remaining = x % y
    pass

def floor_div(x: int, y: int):
    """Divide x by y and floor the value. Use an arithmetic operator."""
    div_floor = floor(x / y)
    pass


def exponent(x: int, y: int):
    """Calculate x raised to the power of y."""
    power = x ** y
    pass


def first_greater_or_equal(x: int, y: int):
    """If x is greater or equal than y then return True. If not then return False."""
    if x >= y:
        print("True")
    else:
        print("False")
    pass


def second_less_or_equal(x: int, y: int):
    """If y is less or equal than x then return True. If not then return False."""
    if y >= x:
        print("True")
    else:
        print("False")
    pass


def x_is_y(x: int, y: int):
    """If x value is the same as y value then return True. If not then return False."""
    if x == y:
        print("True")
    else:
        print("False")
    pass


def x_is_not_y(x: int, y: int):
    """If x value is not the same as y value then return True. If not then return False."""
    if x == y:
        print("False")
    else:
        print("True")
    pass


def if_else(a: int, b: int, c: int, d: int):
    """
    Create a program that has 4 numeric parameters.

    Multiply parameters 1-2 (multiply a by b) by each other and divide parameters 3-4 (divide c by d) by each other.
    Next check and return the greater value. If both values are the same then return 0 (number zero).
    """
    parametersab = multiply(a, b)
    parameterscd = div(c, d)
    if parametersab > parameterscd:
        print(f"{parametersab} is greater")
    elif parametersab < parameterscd:
        print(f"{parameterscd} is greater")
    elif parametersab == parameterscd:
        print("0")
    pass

def surface(length: int, width: int):
    """Add the missing parameters to calculate the surface of a rectangle. Calculate and return the value of the surface."""
    rectangle_surface = length * width
    pass


def volume(length: int, width: int, height: int):
    """Add the missing parameters to calculate the volume of a cuboid. Calculate and return the value of the volume."""
    cuboid_volume = length * width * height
    pass

def calculate(a: int, x: int, y: int):
    """Takes input from user and picks the equation and numbers."""
    if a == 0:
        print(add(x, y))
    elif a == 1:
        print(sub(x, y))
    elif a == 2:
        print(multiply(x, y))
    elif a == 3:
        print(div(x, y))

print(f"Possible equations: \n0. Add\n1. Subtract\n2. Multiply\n3. Divide")
a = input("Enter which equation: ")
x = input("Enter the first number: ")
y = input("Enter the second number: ")

print(calculate(a, x, y))
