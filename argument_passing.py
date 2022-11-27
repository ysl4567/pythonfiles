import pandas as py

def xvalue():
    x = 3
    y = [4,5]
    return (x,y)

print (xvalue())
print (xvalue()[1])


#*args
def twovalues(*args):
    print (args, type(args))
twovalues(2,3)

#*args - numbers - addition
def addition(*numbers):
    total = 0
    for values in numbers:
        total = total + values
    return (total) #return

print (addition(2,3,4,5))


#*args - numbers - multiuplication
def multiplication(*numbers):
    product = 1
    for values in numbers:
        product = product * values
    return (product) #return

print (multiplication(2,3,4))
print (multiplication(2,3,4,5,6))

#*args - keyword - meats
def meats(*keyword):
    for types in keyword:
        print ("Today, we are selling", types) #print
print (meats("Veal", "Beef", "Pork", "Chicken"))



meats2 = ["Veal", "Beef", "Pork", "Chicken"]
for meat in meats2:
    print("Today, we are selling" , meat)
    
def total_fruits(**kwargs):
    return (kwargs, type(kwargs))
print(total_fruits(banana=5, mango=7, apple=8))

#**kwargs - KEYWORD ARGUMENTS
# no for for loops to print all values
def meatsandprices(**mandp):
    return (mandp, type(mandp))
print(meatsandprices(Veal = 8, Beef = 10, Pork = 12, Chicken = 14))

def firstandlastname(**lastname):
    for values in lastname:
        return ("My name is: John", lastname.keys())
print(firstandlastname(Adams = 1, Tester=2, Hoeven=3, Packard=4))


def totalprice(**fandp):
    total = 0
    for types in fandp.values(): #.values()
        total = total + types
    return (total)
print(totalprice(Veal = 8, Beef = 10, Pork = 12, Chicken = 14))
print(type(totalprice))


def totalprice(**fandp):
    return (fandp.keys()) #.keys()
print(totalprice(Veal = 8, Beef = 10, Pork = 12, Chicken = 14))
print(type(totalprice))





def multiply(*x):
    value = 1
    for numbers in x:
        value = value * numbers
    print (value)
multiply(3,4,5)


def alphabet_values(**langauges):
    sum  = 0
    for numbers in langauges.values():
        sum = sum + numbers
    return (sum)
print (alphabet_values(a = 1, b= 2, c=3, d=4))


def alphabet_value_2(**languages):
    sum = 0
    for values in languages.values():
        sum = sum + values
    return(sum)
print (alphabet_value_2(a = 1, b= 2, c=3, d=4))


print ("\n")

def sum_values_3(**numbers):
    total_sum = 0
    for values in numbers.values():
        total_sum = total_sum + values
    return (total_sum)

print (sum_values_3(a=1,b=2,c=3,d=4))

print ("\n")


def alphabet_value_2(**letters):
    return (letters.keys())
print (alphabet_value_2(a=1,b=2,c=3,d=4))

print ("\n")

def alphabet_value_4(**numbers):
    return (numbers.values())
print (alphabet_value_4(a=1,b=2,c=3,d=4))
    

dict_1 = {"a":1,"b":2,"c":3,"d":4}


#input3 = (input("Enter values with comma: "))
#print (input3)

def mult2(*numbers):
    first_value = 1
    for number in numbers:
        first_value = first_value * number
    print (first_value)

mult2(3,4,5)



def add2(*numbers):
    first_value = 0
    for number in numbers:
        first_value = first_value + number
    print (first_value)
add2(3,4,5)



def add3(*numbers):
    first = 0
    for number in numbers:
        first = first + number
    print (first)
add3(4,5,6)





