"""Hello code ex01 intro."""

name = input("What is your name? ")   # asks for name
first = int(input("Hello, " + str(name) + "! Enter a random number: "))   # says name and asks for first number
print(first)
second = int(input("Great! Now enter a second random number: "))    # asks for second number
print(second)
print(str(first) + " + " + str(second) + " " + "is " + str(first + second))    # prints equation with answer
