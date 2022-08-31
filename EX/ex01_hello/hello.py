"""Hello kood ex01."""
name = input("What is your name? ")   # asks for name
esimene = int(input("Hello, " + str(name) + "! Enter a random number: "))   # says name and asks for first number
print(esimene)
teine = int(input("Great! Now enter a second random number: "))    # asks for second number
print(teine)
print(str(esimene) + " + " + str(teine) + " " + "is " + str(esimene + teine))    # prints equation with answer
