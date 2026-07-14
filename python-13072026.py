# Week 2 — Logic Building 
# Day 8: For Loop Print the multiplication table of a number entered by the user.
# number = int(input('enter a number: '))
# print('multiplication table of {number}')
# for i in range(1,11):
#     result = number * i 
#     print(f'{number} x {i} = {result}')

# Day 9: While Loop - Create a countdown program from 10 to 1, followed by “Time’s up!”
# count = 10 
# while count>=1:
#  print(count)
#  count -= 1
# print("time's up")

# Day 10: Functions — Part 1 - Write separate functions for addition, subtraction, multiplication, and division.
# def add(a,b):
#     return a + b 
# print(add(50,40))
# def subtract(a,b):
#     return a - b 
# print(subtract(20,39))
# def divide(a,b):
#     if b == 0:
#         return 'cannot divide by zero.'
#     return a / b 
# def multiply(a,b):
#     return a * b 
# num1 = float(input('enter the first number: '))
# num2 = float(input('enter the second number: '))
# print('addition',add(num1,num2))
# print('subtraction',subtract(num1,num2))
# print('multiply',multiply(num1,num2))
# print('divide',divide(num1,num2))

# Day 11: Functions — Part 2 - Create a function that accepts a list of numbers and returns the highest, lowest, and average values.
# def analyze_numbers(numbers):
#     highest = max(numbers)
#     lowest = min(numbers)
#     average = sum(numbers) / len(numbers)
#     return highest , lowest, average  
# numbers = [10,25,54545,55,555]
# highest, lowest, average = analyze_numbers(numbers)
# print('highest value',highest)
# print('lowest value',lowest)
# print('average value',average)

# Day 12: Lists - Build a shopping-list program where users can add, view, and remove items.
shopping_list = []
while True:
    print("\nShopping List Menu")
    print("1. Add an item")
    print("2. View items")
    print("3. Remove an item")
    print("4. Exit")

    choice = input('enter your choice:')

    if choice == '1':
        item = input('enter the item to add')
        shopping_list.append(item)
        print(item,'has been added')

    elif choice == '2':
        if len(shopping_list) == 0:
            print('your shopping list is empty.')
        else:
            print('\n  your shopping list:')
            for index,item in enumerate(shopping_list,start=1):
                print(index,item)

    elif choice == '3':
        if len(shopping_list) == 0:
            print('your shopping list is empty ')
        else:
            item = input('enter the item to remove')

            if item in shopping_list:
                shopping_list.remove(item)
                print(item,'has been removed')
            else:
                print('item not found in the shopping list')

    elif choice == '4':
        print('shopping list program closed.')

    else:
        print('invalid choice. please enter a number from 1 to 4.')
                







