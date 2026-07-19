# Section A if statement

#  Question 1
# A program that checks if a lab equipment ID is valid based on a specific prefix.
equipment_id = input("Enter Lab Equipment ID: ")

if equipment_id.startswith("FCP"):
    print("Valid ID")
 

# Question 2
# A program that checks if the temperature is above a certain threshold and prints an alert message.
temperature = float(input("Enter Temperature: "))

if temperature > 35:
    print("High Temperature Alert")


# Question 3
# A program that checks if three numbers are equal and prints a message accordingly.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 == num3:
    print("All Equal")

# Section B if....else

# Question 4
# A program that checks if the entered username is "admin" and prints a welcome message.
username = input("Enter Username: ")

if username == "admin":
    print("Welcome Admin")


# Question 5
# A program that checks the number of computers in a lab and categorizes it as a large or small lab.
computers = int(input("Enter number of computers: "))

if computers > 20:
    print("Large Lab")
else:
    print("Small Lab")


# Question 6
# A program that checks if a student's CGPA is above a certain threshold and prints the corresponding class.
cgpa = float(input("Enter CGPA: "))

if cgpa >= 3.5:
    print("First Class")
else:
    print("Not First Class")


# Question 7
# A program that checks if the monthly income is below a certain threshold and categorizes it as low or good income.
income = float(input("Enter Monthly Income: "))

if income < 100000:
    print("Low Income")
else:
    print("Good Income")

# Section C if....elif.....else

# Question 8
# A program that takes a month number as input and prints the corresponding month name.
month = int(input("Enter Month Number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid Month")


# Question 9
# A program that checks the pH value and categorizes it as acidic, neutral, or basic.
ph = float(input("Enter pH Value: "))

if ph < 7:
    print("Acidic")
elif ph == 7:
    print("Neutral")
else:
    print("Basic")


# Question 10
# A program that takes a student's score as input and prints the corresponding grade based on predefined ranges.
score = int(input("Enter Student Score: "))

if score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Section D for loop
# Question 11
# A program that prints all even numbers from 2 to 50 using a for loop.
print("Even Numbers:")

for i in range(2, 51, 2):
    print(i)


# Question 12
# A program that takes a number as input and prints its multiplication table from 1 to 12 using a for loop.
n = int(input("Enter Number: "))

for i in range(1, 13):
    print(f"{n} x {i} = {n*i}")


# Question 13
# A program that calculates the sum of all numbers from 1 to 100 using a for loop.
total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)


# Question 14
# A program that prints a list of lab equipment and their availability status using a for loop.
equipment = [
    "Microscope",
    "Computer",
    "Projector",
    "Printer",
    "Router"
]

for item in equipment:
    print(item, "- Available")


# Question 15
# A program that counts the number of students with scores above 50 using a for loop.
count = 0

for i in range(5):
    score = int(input(f"Enter Score {i+1}: "))

    if score > 50:
        count += 1

print("Students above 50 =", count)

# Section E while lop

# Question 16
# A program that prompts the user to enter a password and grants access only if the correct password is entered.
password = ""

while password != "lab2025":
    password = input("Enter Password: ")

print("Access Granted")


# Question 17
# A program that prints numbers from 10 to 1 in descending order using a while loop.
num = 10

while num >= 1:
    print(num)
    num -= 1


# Question 18
# A program that continuously prompts the user to enter numbers and calculates the total until the user enters 0.
total = 0

number = int(input("Enter Number (0 to stop): "))

while number != 0:
    total += number
    number = int(input("Enter Number (0 to stop): "))

print("Total =", total)


# Question 19
# A program that calculates the factorial of a given number using a while loop.
number = int(input("Enter Number: "))

factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial =", factorial)


# Question 20
# A program that counts the number of students in a class using a while loop.
count = 0

name = input("Enter Student Name (stop to finish): ")

while name.lower() != "stop":
    count += 1
    name = input("Enter Student Name (stop to finish): ")

print("Total Students =", count)