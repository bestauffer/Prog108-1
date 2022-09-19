# LAB ACTIVITY 1
from datetime import date
# Write a program that does the following:

# include a three line comment at the top of the program that says PROG 108 Lab Activity 1, today's date, and your name 
# example output - none this is just a comment
a = date.today()
print("PROG 108 Lab Activity 1")
print(a)
print("Blake Stauffer")
# output Hello, World! to the screen
# example output
# Hello, World!
print("Hello, World!")
# add two numbers together and outputs the math equation and the total to the screen (no need to create variables for this one) 
# example output
# 10 + 55 = 65
print("200 + 5 = 205")
# create a variable named firstName and stores your first name to it and print out the variable
# example output
# Tony
firstName = "Blake"
print(firstName)

# create a variable named lastName and stores your last name to it and print out the variable
# example output
# Stark
lastName = "Stauffer"
print(lastName)
# outputs the message "My name is " and the string value of the firstName and lastName variables. Tip: Be sure there is a space between the is and your first and last name. Include a period at the end of the sentence.
# example output
# My name is Tony Stark.
print("My name is", firstName, lastName + ".")

# create a variable named num1 and stores the number 22 to it. Print the variable value to the screen.
# example output
# 22
num1 = 22
print(num1)
# create a variable named num2 and stores the number 2022 to it. Print the variable value to the screen.
# example output
# 2022
num2 = 2022
print(num2)

# output the math equation sentence using the variables num1 and num2 and display the value of num1 multiplied by num2 to the screen
# example output
# 22 x 2022 = 44484
print(num1, "x", num2, "=", num1*num2)


# experiment with a line or two of code of your own for further Python practice (perhaps more math, or an input statement?) 
num3 = int(input('Enter a number: '))
num4 = int(input('Enter another number: '))
print(num3, "/", num4, "=", num3/num4)