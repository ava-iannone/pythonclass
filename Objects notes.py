'''class Car:
    color = "blue"
    make = "Toyota"
    year = 2020

myCar = Car()
print(myCar.year, myCar.color)'''

class Car:
    def __init__(self, make, year, color):
        self.make = make
        self.year = year
        self.color = color

raceCar = Car("Ferrari", 2025, "red")
dailyDriver = Car("Toyota", 2020, "blue")
vacationCar = Car("Lamborghini", 2019, "yellow")
