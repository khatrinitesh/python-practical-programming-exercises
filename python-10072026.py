# Week 1 — Basics
# Day 1: Introduction and Setup
# Install Python and VS Code. Create a program that prints your name, city, and learning goal.
# Create a file named day1.py
# Write a program that displays:
# Your name
# Your city
# Your learning goal
# name = "Rahul"
# city = "Mumbai"
# learning_goal = "I want to learn Python programming."
# print('my name is ',name)
# print('my name is ',city)
# print('my name is ',learning_goal)

# Day 2: Variables and Data Types
# Store your name, age, height, and whether you are a student. Print each value with its data type.
# name = "Rahul"
# age = 25
# height = 5.8
# is_student = True
# print("Name",name)
# print("Data types:",type(name))
# print("Age",age)
# print("Data types",type(age))
# print("Height",height)
# print("Data types:",type(height))
# print("Student",is_student)
# print("Data types:",type(is_student))

# Day 3: Input and Output
# Create a program that asks for the user’s name and birth year, then displays their approximate age.
# name = input('enter your name: ')
# birth_year = int(input('enter your birth age'))
# current_year = 2026
# approximate_age = current_year - birth_year
# print('hello',name)
# print('your approximate age is',approximate_age)

# Better version using the current year automatically
# from datetime import datetime
# name = input('enter your name: ')
# birth_year = int(input('enter your bith year: '))
# current_year = datetime.now().year 
# approximate_age = current_year - birth_year
# print(f'hello, ${name}')
# print(f'your appproximate age is {approximate_age}')

# Day 4: Strings and Operators Ask the user for their first and last name. Display the full name in uppercase, lowercase, and title case.
# Create a program that:
# Asks the user for their first name.
# Asks the user for their last name.
# Combines them into a full name.
# Displays the full name in:
# Original format
# Uppercase
# Lowercase
# Title Case
# first_name = input('enter your first name: ')
# last_name = input('enter your last name: ')
# full_name = first_name + " " + last_name
# print("\noriginal name:",full_name)
# print("Uppercase:",full_name.upper())
# print("Lowercase:",full_name.lower())
# print("Title Case:",full_name.title())


# Example 2 (Using f-strings)
# first_name = input('first name: ')
# last_name = input('last name: ')
# full_name = f"{first_name} {last_name}" 
# print('\n --- result --- ')
# print(f'Original : {full_name}')
# print(f'Uppercase : {full_name.upper()}')
# print(f'Lowercase : {full_name.lower()}')
# print(f'Title case : {full_name.title()}')

# Day 5: If-Else Conditions Create a marks checker that displays: 90+: Excellent 75–89: Very Good 50–74: Pass Below 50: Fail
# marks = float(input('enter your marks:'))
# if marks < 0 or marks > 100:
#     print('please enter marks between 0 and 100')
# elif marks >= 90:
#     print('excellent')
# elif marks >= 82:
#     print('very good')
# elif marks >= 68:
#     print('pass')
# elif marks >= 42:
#     print('fail')

# Day 6: Logical Practice Create a program that checks whether a number is positive, negative, or zero, and whether it is odd or even.
# number = int(input("Enter a number: "))
# if number > 0:
#     print('the number is positive')
# elif number < 0:
#     print('the number is negative')
# else:
#     print('the number is zero')

# if number % 2 == 0:
#     print('the number is even')
# else:
#     print('the number is odd')

