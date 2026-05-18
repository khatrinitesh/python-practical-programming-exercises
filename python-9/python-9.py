
# day 1 - print and variables
# print('hello world')
# name = 'nitesh'
# age = 25 
# print('my name is', name, 'and i am', age, 'years old')
# practical example: user profile
# name = 'nitesh'
# city = 'mumbai'
# job = 'developer'
# print('name',name)
# print('city',city)
# print('job',job)
# concepts learned
# print()
# variables 
# strings 
# numbers

# day 2 - input from user 
# name = input('what is your name?')
# print('welcome',name)
# practical example:age calculator
# birth_year = int(input('what is your birth year'))
# current_year = 2026 
# age = current_year - birth_year 
# print('your age is',age)
# concepts learned 
# - input() 
# - int 
# - user interaction 

# day 3 - conditions (if, else)
# practical examples: voting eligibility 
# age = int(input('enter your age'))
# if age >= 18:
#     print('you are eligible to vote')
# else:   
#     print('you cannot vote')
# practical examples:even or odd 
# number = int(input('enter a number'))
# if number % 2 == 0:
#     print('the number is even')
# else:
#     print('the number is odd')
# concepts learned 
# - if 
# - else 
# - comparison operators 

# day 4 - loops for loop example 
# for i in range(1,5):
#     print('iteration',i)
# practical example: multiplication table 
# num = int(input('enter a number'))
# for i in range(1,11): 
#     print(num,'x',i,'=',num*i)
# while loop
# count = 1 
# while count <= 5: 
#     print('count is',count)
#     count += 1
# concepts learned
# - for 
# - while 
# - range()

# day 5 - functions 
# practical example: calculator function 
# def add(a,b): 
#     return a + b 
# result = add(10,20)
# print('the sum is',result)
# def add(a,b):
#     print(a+b) 
# result = add(10,20)
# practical example: greeting app 
def greet(name):
    print('hello',name)
greet('nitesh')