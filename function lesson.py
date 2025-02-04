#example of nested if statement

age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter the concert")
    else:
        print("You need a ticket to enter the concert")
else:
    print("You must be at least 18 years old to enter the concert")



#functions

def printMe(team, points):
    print("Welcome to the Superbowl. KC VS Eagles")
    print("I hope the " + team + " win" + " by", points)

team_name = "Chiefs"
printMe(team_name, 10)


def doubleMyValue(number):
    answer = number * 2
    return answer

number = doubleMyValue(12)
print("When I call the function it returned", number)
