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

