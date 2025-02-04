# int -> Integer
# float -> Float
# str -> String

#example of string
name = "Scooby"
weather = "rain"
# general print statement
print ("I have a puppy")
print ("I have a puppy named " +name +" that is in the " +weather)
# print with a placeholder
print ("The puppy, {}, was outside" .format(name))
print ("The puppy, {}, was outside in the {}" .format(name, weather))


# input from the user... String
color = input("What is your favorite color?\n")
print("My favorite color entered was " +color)

# input from the user... Integer
age = int(input("How old are you?\n"))
print("You are {} years old" .format(age))

# math in python
value1 = int(input("Please enter a number\n"))
value2 = int(input("Please enter another number\n"))

sum = value1 + value2
print("The sum is ",sum)