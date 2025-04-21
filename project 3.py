def display_seats(seats):
    print("\nSeat Map:")
    count = 0
    while count < len(seats):
        display_row = ""
        inner_count = 0
        while inner_count < 5:
            if seats[count]:
                display_row += "X "
            else:
                display_row += str(count + 1) + " "
            count += 1
            inner_count += 1
        print(display_row.strip())
    print("X = Taken seat")


def is_emergency_seat(seat_num):
    return 6 <= seat_num <= 15


def is_first_class_seat(seat_num):
    return 1 <= seat_num <= 5


def main():
    seats = [False] * 20
    total_cost = 0

    print("Welcome to the Airplane Seat Reservation System!")
    display_seats(seats)

    while True:
        seat_input = input("\nEnter seat numbers to purchase (comma separated), or 'c' to confirm and purchase your seats: ")
        if seat_input.lower() == 'c':
            break

        seat_strs = seat_input.split(',')
        seat_numbers = []
        for s in seat_strs:
            s = s.strip()
            if s.isdigit():
                seat_numbers.append(int(s))
            else:
                print(f"'{s}' is not a valid number.")

        for seat in seat_numbers:
            if seat < 1 or seat > 20:
                print(f"Seat {seat} is invalid. Please choose between 1 and 20.")
                continue

            if seats[seat - 1]:
                print(f"Seat {seat} is already taken.")
                continue

            if is_emergency_seat(seat):
                confirm = input(f"Seat {seat} is an emergency exit row seat. Do you accept responsibility in case of emergency? (yes/no): ")
                if confirm.lower() != "yes":
                    print(f"Seat {seat} not reserved because you did not accept emergency responsibility.")
                    continue

            seat_price = 100
            if is_first_class_seat(seat):
                print(f"Seat {seat} is a first-class seat. An additional $40 fee applies.")
                seat_price += 40

            total_cost += seat_price
            seats[seat - 1] = True
            print(f"Seat {seat} reserved. Price: ${seat_price}")

        display_seats(seats)

    print(f"\nReservation complete. Total fee: ${total_cost}")
    print("Thank you for flying with us!")


if __name__ == "__main__":
    main()
