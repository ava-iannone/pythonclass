class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    def __init__(self):
        self.beverages = [
            Beverage("Coke", 1.50),
            Beverage("Diet Coke", 1.25),
            Beverage("Water", 1.00),
            Beverage("Iced Coffee", 1.75),
            Beverage("Iced Tea", 1.50),
            Beverage("Energy Drink", 1.75)]

    def display_menu(self):
        print("\nWelcome to the Vending Machine")
        for idx, bev in enumerate(self.beverages, 1):
            print(f"{idx}. {bev.name} - ${bev.price:.2f}")
        print("Select a beverage by entering the number.")

    def vend(self, selection, money):
        if selection < 1 or selection > len(self.beverages):
            print("Invalid selection. Please try again.")
            return

        beverage = self.beverages[selection - 1]
        if money < beverage.price:
            print(f"Not enough money :( {beverage.name} costs ${beverage.price:.2f}. You inserted ${money:.2f}.")
            return

        change = money - beverage.price
        print(f"Vending {beverage.name}... Enjoy your drink! :)")
        if change > 0:
            print(f"Don't forget your change: ${change:.2f}")

machine = VendingMachine()

while True:
    machine.display_menu()
    try:
        selection = int(input("Enter selection (1-6): "))
        money = float(input("Insert money: $"))
        machine.vend(selection, money)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
