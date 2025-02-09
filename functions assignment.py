import math

def circlearea(radius):
    return math.pi * radius ** 2

radius = float(input("What is the radius of your circle?\n"))
area = circlearea(radius)
print("The area of your circle is", area)


def totaldue(money, tax):
    return money + (money * (tax * 0.01))

money = float(input("\nHow much money do you owe?\n"))
tax = float(input("What is the tax rate percentage?\n"))
owed = totaldue(money, tax)
print("You owe", owed, ":(")


def celcius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

fahrenheit = float(input("\nWhat is the temperature in Fahrenheit?\n"))
temp = celcius(fahrenheit)
print("The temperature is", temp, "degrees Celcius")
if fahrenheit <= 70:
    print("Brrrr!")

print("\nAva Iannone")