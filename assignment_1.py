# Question 01
print("""Twinkle, twinkle, little star
        How I wonder what you are!
                    Up above the world so high,
                    Like a diamond in the sky.
Twinkle, twinkle, little star
        How I wonder what you are!

""")

# Question 02

import sys 
print(sys.version)

# Question 03

from datetime import datetime
now = datetime.now()
print(now)

# Question 04

import math 
radius = input("Enter the radius of the circle")
area = math.pi * radius ** 2
print("The area of the circle is:", area)

# Question 05

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

print(lastName + " " + firstName)

# Question 06

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print("The sum is:", sum)

# Question 07

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("\nTotal Marks:", total)
print("Average:", average)
print("Percentage:", percentage)
print("Grade:", grade)

# Question 08

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The entered number is even", num)

else:
    print("The entered number is odd", num)
    
    
    
