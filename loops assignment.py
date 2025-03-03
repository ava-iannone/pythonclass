def print_menu():
    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")
    print("1. Tacos - $5.00")
    print("2. Burritos - $6.00")
    print("3. Nachos - $4.50")
    print("4. Quesadilla - $4.00")
    print("5. Quit")

def get_price(selection):
    prices = {1: 5.00, 2: 6.00, 3: 4.50, 4: 4.00}
    return prices.get(selection, 0)

def main():
    menu_items = ["Tacos", "Burritos", "Nachos", "Quesadilla"]
    prices = [5.00, 6.00, 4.50, 4.00]
    order_list = []
    total_price = 0


    while True:
        print_menu()
        try:
            choice = int(input("Please enter your selection: "))
            if choice == 5:
                break
            elif 1 <= choice <= 4:
                item_name = menu_items[choice - 1]
                price = prices[choice - 1]

                order_list.append(item_name)
                total_price += price

                print("You have selected " + item_name + ". Your total is now $" + str(total_price) + "\n")
            else:
                print("Please choose a number between 1 and 5.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    print("\nYour order:")
    for item in order_list:
        print("- " + item)
    print("Total amount due: $" + str(total_price))
    print("Thank you for visiting Taco Palace! Have a great day!")

main()
