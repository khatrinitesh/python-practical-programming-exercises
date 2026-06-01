# print('hello it is very important to learn python')

# x = 10
# y = 20
# addition = 10 + 20
# subtraction = 20 - 10 
# multiply = 20 * 10 
# dividend = 20 / 10 
# percent = 20 % 10 
# print(addition)
# print(subtraction)
# print(multiply)
# print(dividend)
# print(percent)

# def calculate_grade(percentage):
#     if percentage >= 90:
#         return "A+"
#     elif percentage >= 80:
#         return "A"
#     elif percentage >= 70:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 50:
#         return "D"
#     else:
#         return "Fail"


# students = []

# number_of_students = int(input("Enter number of students: "))

# for i in range(number_of_students):
#     print(f"\nEnter details for student {i + 1}")

#     name = input("Enter student name: ")
#     roll_number = input("Enter roll number: ")

#     marks = []

#     for subject in range(5):
#         mark = float(input(f"Enter marks for subject {subject + 1}: "))
#         marks.append(mark)

#     total_marks = sum(marks)
#     percentage = total_marks / 5
#     grade = calculate_grade(percentage)

#     student = {
#         "name": name,
#         "roll_number": roll_number,
#         "marks": marks,
#         "total_marks": total_marks,
#         "percentage": percentage,
#         "grade": grade
#     }

#     students.append(student)


# print("\n========== Final Student Results ==========")

# for student in students:
#     print("\nStudent Result")
#     print(f"Name: {student['name']}")
#     print(f"Roll Number: {student['roll_number']}")
#     print(f"Marks: {student['marks']}")
#     print(f"Total Marks: {student['total_marks']}")
#     print(f"Percentage: {student['percentage']:.2f}%")
#     print(f"Grade: {student['grade']}")

# def calculate_grade(percentage):
#     if percentage >= 90:
#         return "A+"
#     elif percentage >= 80:
#         return "A"
#     elif percentage >= 70:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 50:
#         return "D"
#     else:
#         return "Fail"


# students = []

# number_of_students = int(input("Enter number of students: "))

# for i in range(number_of_students):
#     print(f"\nEnter details for student {i + 1}")

#     name = input("Enter student name: ")
#     roll_number = input("Enter roll number: ")

#     marks = []

#     for subject in range(5):
#         mark = float(input(f"Enter marks for subject {subject + 1}: "))
#         marks.append(mark)

#     total_marks = sum(marks)
#     percentage = total_marks / 5
#     grade = calculate_grade(percentage)

#     student = {
#         "name": name,
#         "roll_number": roll_number,
#         "marks": marks,
#         "total_marks": total_marks,
#         "percentage": percentage,
#         "grade": grade
#     }

#     students.append(student)


# print("\n========== Final Student Results ==========")

# for student in students:
#     print("\nStudent Result")
#     print(f"Name: {student['name']}")
#     print(f"Roll Number: {student['roll_number']}")
#     print(f"Marks: {student['marks']}")
#     print(f"Total Marks: {student['total_marks']}")
#     print(f"Percentage: {student['percentage']:.2f}%")
#     print(f"Grade: {student['grade']}")

# print('hello python')
# print('my name is test')
# print('i am learning python daily')

# variables
# name = 'test'
# age = 30 
# city = 'mumbai'
# print(f'my name is ${name}, my age is ${age}, my city is ${city}')

# user input ask user details and print them 
# name = input('enter your name:')
# city = input('enter your city:')
# print(f'hello, ${name}')
# print(f'city, ${city}')

# numbers and calculations create a simple calculator
# a = int(input('enter first number'))
# b = int(input('enter second number'))
# print('addition:',a+b)
# print('addition:',a-b)
# print('addition:',a*b)
# print('addition:',a/b)

# if else - check voting eligibility 
# age = int(input('enter your age: '))
# if age >= 18:
#     print('yes ')
# else:
#     print('no')

# loops - print numbers from 1 to 10 
# for i in range(1,11):
#     print(f'list {i}: i {i}x{i}={i * i}')
# for i in range(1,11):
#     for j in range(1,11):
#         print(f'list: {i} x {j} = {i * j}')
#         print()

# mini project - basic marks calculator take marks of 5 subjects, calculate total, percentage and grade
# m1 = int(input('subject 1: '))
# m2 = int(input('Subject 2: '))
# m3 = int(input('Subject 3: '))
# m4 = int(input('Subject 4: '))
# m5 = int(input('Subject 5: '))
# total = m1+m2+m3+m4+m5
# percentage = total / 5 
# print('Total:',total)
# print('Percentage:',percentage)

# if percentage >= 90:
#     print('Grade: A')
# elif percentage >= 75:
#     print('Grade: B')
# elif percentage >= 50:
#     print('Grade: C')
# else:
#     print('Grade: Fail')

# data structures - create a list of fruits 
# fruits = ["apple", "banana", "mango"]
# print(fruits)
# print(fruits[0])
# fruits.append('orange')
# print(fruits)
# numberwise = [44,66.77,85]
# print(numberwise)
# numberwise.append(786)
# print(numberwise)

# list loops print all items from a list 
# movies = ["KGF", "Leo", "Vikram", "Jailer"]
# for i in movies:
#     print(f'Movie: {i}')

# dictionaries - store user data 
# user = {
#     'name':'test',
#     'age':30,
#     'city':'mumbai'
# }
# print(user['name'])
# print(user['city'])

# functions - create a getting function create a function that adds two numbers
# def greet(name):
#     print('hello',name)
# greet('python')

# return values return calculation result 
# def add(a,b):
#     return a + b 
# def sub(a,b):
#     return a - b 
# def mul(a,b):
#     return a * b 
# def per(a,b):
#     return a / b
# def mod(a,b):
#     return a % b 
# result1 = add(10,20)
# result2 = sub(10,20)
# result3 = mul(10,20)
# result4 = per(10,20)
# result5 = mod(10,20)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)

# return values - return calculation result  create functions for subtract, multiply and divide
# def add(a,b):
#     return a + b 
# result = add(10,20)
# print(result)

# string practice - work with text - ask user name and print it in uppercase, lowercase and title case 
# text1 = 'python is easy'
# print(text1.upper())
# print(text1.capitalize())
# print(text1.replace('easy','powerful'))

# mini project - simple contact book - Add 3 contacts using repeated input.
# contacts = []

# name = input('enter name: ')
# phone = input('enter phone: ')

# contact = {
#     "name": name,
#     "phone":phone
# }

# contacts.append(contact)

# print('saved contact')
# print(contact)

# practical programs while loop keep asking until correct password
# password = ''
# while password != '1234':
#     password = input('enter password')
# print('access granted')

# number guessing game - guess a find number
# secret = 7
# guess = int(input('enter guess number: '))
# if secret == guess:
#     print('correct')
# else:
#     print('wrong')

# random module -  random number game 
# import random 
# secret = random.randint(1,10)
# guess = int(input('guess number between 1 and 10.'))
# if guess == secret:
#     print('correct')
# else:
#     print('wrong. number was', secret)  