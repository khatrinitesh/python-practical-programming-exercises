# student = {
#     "name": "Rahul Sharma",
#     "roll_number": 101,
#     "marks": 85,
#     "course": "Python Programming",
#     "attendance": 92.5
# }
# print('student record')
# print('------')
# print('name: ',student['name'])
# print('roll_number: ',student['roll_number'])
# print('marks: ',student['marks'])
# print('course: ',student['course'])
# print('attendance: ',student['attendance'])

# student = {
#     "name": input("Enter student name: "),
#     "roll_number": int(input("Enter roll number: ")),
#     "marks": float(input("Enter marks: ")),
#     "course": input("Enter course name: "),
#     "attendance": float(input("Enter attendance percentage: "))
# }
# print("\nStudent Record")
# print('---------------')
# for key,value in student.items():
#     print(key,value)
# student = {
#     "name": input("Enter student name: "),
#     "roll_number": int(input("Enter roll number: ")),
#     "marks": float(input("Enter marks: ")),
#     "course": input("Enter course name: "),
#     "attendance": float(input("Enter attendance percentage: "))
# }
# for key,value in student.items():
#     print(key.replace("_"," ").title(),":",value)

# Day 14: Mini Project — Menu-Driven Calculator
# Day 14: Mini Project — Menu-Driven Calculator

# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# def multiply(a, b):
#     return a * b


# def divide(a, b):
#     if b == 0:
#         return "Error: Cannot divide by zero."
#     return a / b


# def percentage(a, b):
#     return (a * b) / 100


# while True:
#     print("\n--- Calculator Menu ---")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Percentage")
#     print("6. Exit")

#     choice = input("Enter your choice (1-6): ")

#     if choice == "6":
#         print("Calculator closed.")
#         break

#     if choice not in ["1", "2", "3", "4", "5"]:
#         print("Invalid choice. Please select between 1 and 6.")
#         continue

#     number1 = float(input("Enter first number: "))
#     number2 = float(input("Enter second number: "))

#     if choice == "1":
#         print("Result:", add(number1, number2))

#     elif choice == "2":
#         print("Result:", subtract(number1, number2))

#     elif choice == "3":
#         print("Result:", multiply(number1, number2))

#     elif choice == "4":
#         print("Result:", divide(number1, number2))

#     elif choice == "5":
#         print(f"{number2}% of {number1} is:", percentage(number1, number2))

# api json 
# import requests

# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# if response.status_code == 200:
#     posts = response.json()

#     for post in posts:
#         print('userid: ',post['userId'])
#         print('title: ',post['title'])
#         print('body: ',post['body'])
#         print('-' * 50)

#     else:
#         print('failed to fetch posts')
#         print('status code:',response.status_code)

# import requests 

# response = requests.get('https://jsonplaceholder.typicode.com/posts',timeout=10)
    
# if response.status_code == 200:
#     posts = response.json()

#     for post in posts:
#         print('title: ',post['title'])
#         print('body: ',post['body'])
#         print('=' * 10)
# else:
#     print('Erro:',response.status_code)

# import requests 
# response = requests.get('https://jsonplaceholder.typicode.com/posts',timeout=5)
# if response.status_code == 200:
#     posts = response.json()

#     for post in posts:
#         print('Title: ',post['title'])
#         print('Body: ',post['body'])
#         print('-' * 20)
# else:
#     print('failed to fetch posts')
#     print('status code: ',response.status_code)

# Week 3 — Real-World Skills Day 15: File Handling -Create a text file, write five notes into it, and display all saved notes.
# file_name = 'notes.txt'
# notes = [
#     "Complete the Python assignment.",
#     "Practice file handling.",
#     "Read about functions.",
#     "Review dictionaries.",
#     "Prepare for tomorrow's class."
# ]

# # Write five notes into the text file
# with open(file_name,'w') as file:
#     for note in notes:
#         file.write(note + '\n')
# print('five notes saved successfully.\n')
# file_name = 'sales.xls'
# customerwise = [
#     'atharva diesel',
#     'balakrishna fuel injection service',
#     'diesel tech service',
#     'shriyan auto works',
#     'shriyan diesel',
#     'western automobile'
# ]
# with open(file_name,'w') as file:
#     for customer in customerwise:
#         file.write(customer + '\n') 
# print('customerwise saved successfully.\n')

# print(type(3.14))
# print(type('test'))
# print(type('asddad'))
# print(type(True))
# print(type(-11))
# print(type(11.5))
# print(type([12,55,66]))
# print(type((12,55,66)))
# print(type({12,55,66}))
