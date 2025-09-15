# Python Built in Functions
def example1():
    number1 = -10
    absNum = abs(number1)
    return absNum
result1 = example1()
print('Result 1',result1)

def example2():
    number2 = 7 
    absNum = abs(number2) 
    return absNum
result2 = example2()
print('Result 2',result2)

def example3():
    number3 = -3.5
    absNum = abs(number3)
    return absNum
result3 = example3()
print('Result 3',result3)

def example4():
    values = [True, 1, "text", [1], 10]
    allValues = all(values)
    return allValues
result4 = example4()
print('Result 4:',result4)

def example5():
    values = [True, 1, 0, "text"]
    return values
result5 = example5()
print('Result 5:',result5)

def example6():
    numbers = [2, 4, 6, 8]
    all_even = all(n % 2 == 0 for n in numbers)
    return all_even
result6 = example6()
print('Result 6:',result6)

def example7():
    print(all([]))
result7 = example7()
print('Result 7:',result7)

def example8():
    values = [False,0,"",5]
    return values
result8 = example8()
print('Result 8:',result8)

def example9():
    values = [False, 0, "", None]
    return values
result9 = example9()
print('Result 9:',result9)

def example10():
    numbers = [1, 3, 5, 6]
    has_even = any(n % 2 == 0 for n in numbers)
    return has_even
result10 = example10()
print('Result 10:',result10)

def example11():
    result = bool(1)
    return result 
result11 = example11()
print('Result 11:',result11)

def example12():
    result = bool('nitesh')
    return result 
result12 = example12()
print('Resutl12:', result12)

def example13():
    result = bool([1,2,3])
    return result 
result13 = example13()
print('Result 13:',result13)

def example14():
    result = bool(0)
    return result 
result14 = example14()
print('Result14:',result14)

def example14():
    result = bool("")
    return result 
result15 = example14()
print('Result14:',result15)

def example15():
    result = bool([])
    return result 
result15 = example15()
print('Result15:',result15)

def example16():
    result = bool(None)
    return result 
result16 = example16()
print('Result 16:',result16)

def example17():
    expression = '3+5*2'
    result = eval(expression)
    return result
result17 = example17()
print('Result17:',result17)

def example18():
    x = 10 
    y = 5 
    return x + y 
result18 = example18()
print("Result18:",result18)

def example19(n):
    return n % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
result = filter(example19,numbers)
print(list(result))

def example20():
    x = 10 
    return x 
print('Result20:',float(10))

def example21():
    x = "7"
    return x 
print('Result 21:',float(10))

def example22():
    x = 10 
    return x/2
print('Result 22:',float(10/2))

def example23():
    firstname = 'nitesh'
    lastname = 'khatri'
    return firstname + " " + lastname 
fullname = example23()
print(fullname)

def example24(x, y): 
    return x *y + 10 
calculator = example24(30, 50)
print(calculator)

def example25(a,b):
    return a * b 
calculator = example25(20,30)
print(calculator)

def example26():
    name = 'nitesh'
    age = 30
    return 'My name is {} and my age is {}.'.format(name, age)
formatted_string = example26()
print(formatted_string)

def example27():
    number = 255
    return hex(number)
result27=example27()
print(result27)

def example28():
    return hex(10)
result28=example28()
print(result27)

def example29():
    a = 10 
    b = 20
    print("ID of a inside function:",id(a))
    return a + b 
example29()

def example30():
    a = 10
    b = 20
    return a 
print(example30())

def example31():
    name = input('enter your name:')
    return name
result31 = example31()
print('hello',result31)

def example32():
    num = 5.8 
    return num 
result32 = example32()
print(result32)

def example33():
    s = "123"
    return s 
result33 = example33()
print("result33:",result33)

def example34():
    my_list = [1, 2, 3]
    my_iterator = iter(my_list)
result34 = example34()
print(result34)

def example35():
    name = 'nitesh35'
    return len(name)
result35 = example35()
print(result35)

def example36():
    fruits = ["apple", "banana", "cherry"]
    return fruits
result36 = example36()
print(len(result36))

def example37():
    person = {"name": "Alice", "age": 30}
    return person
result37 = example37()
print(len(result37))



