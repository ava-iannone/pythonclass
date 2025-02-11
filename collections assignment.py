name = str(input("What is your name?\n"))

grade1 = float(input("Enter grade 1\n"))
grade2 = float(input("Enter grade 2\n"))
grade3 = float(input("Enter grade 3\n"))
grade4 = float(input("Enter grade 4\n"))
grade5 = float(input("Enter grade 5\n"))

gradeList = [grade1, grade2, grade3, grade4, grade5]

sum = sum(gradeList)
average = sum / 5

if average >= 89:
    letterGrade = "A"
elif average >= 79:
    letterGrade = "B"
elif average >= 69:
    letterGrade = "C"
elif average >= 59:
    letterGrade = "D"
else:
    letterGrade = "F"

print(name)
print(gradeList)
print("Average:", average)
print("Letter Grade:", letterGrade)

print("\nAva Iannone")