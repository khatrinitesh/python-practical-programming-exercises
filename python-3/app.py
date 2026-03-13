print("Hello Python")

# abs
number = -25
result = abs(number)
print(result)
print(abs(-10))
print(abs(5))

# all
numbers1 = [ 1,2,3,4]
result1 = all(numbers1)
print(result1)
numbers2 = [1, 2, 0, 4]
result2 = all(numbers2)
print(result2)

# any
numbers1 = [0,0,5,0]
result1 = any(numbers1)
print('result1 numbers1',result1)

numbers2 = [0, 0, 0]
result2 = any(numbers2)
print('result2 numbers2',result2)

# ascii
text = 'Hello ñ'
print('Ascii text',ascii(text))

name = "नितेश"
print('Ascii name',ascii(name))

# bin
number = 10222
binary_value = bin(number)
print("Decimal ",number)
print("Binary ",binary_value)

# bool
value1 = 10
value2 = 0 
value3 = ""
value4= 'hello'
result1 = bool(value1)
result2 = bool(value2)
result3 = bool(value3)
result4 = bool(value4)
print('Boolean 1',result1)
print('Boolean 2',result2)
print('Boolean 3',result3)
print('Boolean 4',result4)

# bytearray
value1 = [65, 66, 67, 68]
value2 = [65, 66, 67]
result1 = bytearray(value1)
result2 = value2[1] = 90
print('Value1 bytearray',result1)
print('Value2 bytearray',result2)

# bytes
value1 = [65, 66, 67]
result1 = bytes(value1)
print('Result1',result1)
data = bytes([65,66,67])
print(data)

def greet():
    print('hello')
number = 10
print(callable(greet))
print(callable(number))
def example():
    print('hi how are you')
print(callable(example))
def add(a,b):
    print(a+b)
resultMath = add(5,3)
print('Math calculator',resultMath)

# chr returns a character from a unicode number
value1 = 65
result1 = chr(value1)
print(result1)
value2 = 97
value3 = 8364
print(chr(value2))
print(chr(value3))

# classmethod() Converts a method into a class method (works with the class instead of instance).
class Student:
    school = "ABC School"
    @classmethod
    def get_school(cls):
        return cls.school

print(Student.get_school())

# compile Converts Python code into an executable object.
value1 = "print('Hello Python')"
result1 = compile(value1,'test','exec')
exec(result1)
value2 = "print('Hello nitesh')"
result2 = compile(value2,'test','exec')
exec(result2)
value3 = "print('welcome')"
result3 = compile(value3,'test','exec')
exec(result3)

# complex Creates a complex number.
value1 = complex(3,4)
print(value1)
value2 = complex(5)
print(value2)

# delattr Deletes an attribute from an object.
class Person:
    name = 'test'
    age = 30
p = Person()
delattr(Person,'age')
print(p.name)


class Person2:
    name = 'sameet'
    age = 44
    location = 'Chicago, USA'
p = Person2()
delattr(Person2,'location')
print(p.name,p.age)

#  dict() creates a dictionary object (key-value pairs).
data = dict()
print(data)
print(type(data))

value2 = dict(name='test',age=25,city='mumbai')
print(value2)

value3 = dict([('a',1),('b',2),('c',3)])
print(value3)

# dir() shows all available functions for that object.
print(dir(list))

# divmod(a,b) returns (quotient, remainder).
value1 = divmod(20,2)
value2 = divmod(24,3)
value3 = divmod(25,5)
value4 = divmod(81,9)
print(value1)
print(value2)
print(value3)
print(value4)

# enumerate() Takes a collection (list, tuple, etc.) and returns an enumerate object with index and value.
fruits = ["Apple", "Banana", "Orange"]
value1 = enumerate(fruits)
friendwise = ['pawan','prathmesh','koushik']
value2 = enumerate(friendwise)
print(list(value1))
print(list(value2))
for index,value in enumerate(friendwise):
    print(index,value)
for index,value in enumerate(fruits):
    print(index,value)

for index,value in enumerate(fruits,start=1):
    print(index,value)

# eval() Evaluates and executes a Python expression.
    x = 10
    y= 5
    value1 = eval('x+y')
    print(value1)
    a = 20
    b = 30
    value2 = eval("a*b")
    print(value2)
    value3 = eval("5+6*10")
    print(value3)
x
# exec Executes Python code dynamically.
value1 = """
for i in range(3):
    print("Hello Python")
"""
exec(value1)
value2 = """
for i in range(5):
    print('hi nitesh')
"""
exec(value2)
eval('print(55+55)')
eval('print(56+55*666)')

# filter Uses a function to filter elements from an iterable (list, tuple, etc.).
numbers = [1,2,3,4,5,6]
def even(num):
    return num % 2 == 0
result  = filter(even,numbers)
print(list(result)) 
numbers2 = [405,66,67788,888,115]
def even2(num):
    return num % 2 == 0
result2 = filter(even2,numbers2)
print(list(result2))

numbers3 = [10,15,20,25]
result3 = filter(lambda x:x>15,numbers3)
print(list(result3))

# float Converts a number or string into a floating-point number.
value1 = 10
result1 = float(value1)
print(result1)
print(type(result1))

value2 = 5.666
result2 = float(value2)
print(result2)

# format Formats a value into a specified format. "b" converts number to binary.
val1 = 50
result1 = format(val1,'b')
print(result1)

val2 = 123.45556
result2 = format(val2,'.2f')
print(result2)

# frozenset Creates an immutable (unchangeable) set.
val1 = [1, 2, 3, 4]
fs = frozenset(val1)
print(fs)

class Person:
    name = 'text'
    age = 25
p = Person()
result1 = getattr(p,'age')
print(result1)


# globals Returns a dictionary containing all global variables and functions.
x = 10
y = 20
print(globals())

# hasattr()	Returns True if the specified object has the specified attribute (property/method)
class Person:
    name='test'
    age=24
p = Person()
print(hasattr(p,'name'))
print(hasattr(p,'age'))
print(hasattr(p,'city'))
text = "Hello World"
print(hasattr(text,'upper'))
print(hasattr(text,'append'))

class Car:
    brand = 'toyota'
car = Car()
print(hasattr(car,'brand'))
print(hasattr(car,'age'))


num1 = 255
num2 = 256
num3 = 455
num4 = -422
print('hex1',hex(num1))
print('hex2',hex(num2))
print('hex3',hex(num3))
print('hex4',hex(num4))

# id()	Returns the id of an object
x = 10
y = 20
value1 = 110
value2 = [1,2,3,5,5]
print(id(x))
print(id(y))
print(id(value1))
print(id(value2))

# input()	Allowing user input
# name = input("Enter your name: ")
# print('hello',name)
# name2 = input('please type your name');
# print('hieee',name2)
# age = input('what is your age?')
# print('your age is ',age)

# num1 = int(input('enter first number: '))
# num2 = int(input('enter second number: '))
# sum = num1 + num2 
# print("Sum = ",sum)


# num3 = int(input('enter your first number: '))
# num4 = int(input('enter your second number: '))
# sum = num3 * num4
# print('Sum = ',sum)

# price = float(input("Enter price: "))
# print(price)

x = 10
word = 'hello'
print(isinstance(x,int))
print(isinstance(x,str))
print(isinstance(word,int))
print(isinstance(word,str))
print(isinstance(x,(int,float)))

class Person:
    pass 
p = Person()
print(isinstance(p,Person))

class Animal:
    pass

class Dog(Animal):
    pass
print(issubclass(Dog,Animal))

class A:
    pass

class B:
    pass
print(issubclass(B,A))

numberswise = [10,203,4,555]
resultWise = iter(numberswise)
print(next(resultWise))
print(next(resultWise))
print(next(resultWise))
print(next(resultWise))

numberWiseOne = [55,203,44,55,66,77,66868]
it = iter(numberWiseOne)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

