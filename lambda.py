from itertools import product


def function(n):
    return lambda x: x*n

mydoubler = function(2)

print(mydoubler(11))


f = lambda x,y,z: x+y+z
print (f(2,3,4))

def fullname():
    title = 'Sir'
    action = (lambda x: title + " " + x)
    return (action)

act = fullname()
print (act('robin'))
#print (fullname()) - does not work

L = [lambda x: x**2, lambda x:x**3, lambda x:x**4]
for values in L:
    print (values(2))

def func3(x):
    int2 = lambda x: x+2
    return (int2(x) + 10)

print (func3(10))

#cubed
def func4(x):
    int3 = lambda x: 2*x
    return (int3(x) *2 )
print (func4(2))

#product of three values
def func5(x,y,z):
    product1 = lambda x,y: x*y
    return (product1(x,y) *z)

print (func5(3,4,5))


a = [1,2,3,4,5,6,7,8,9]
newList = list(map(lambda x:x+5 ,a))
print (newList)

a2 = [1,2,3,4,5,6,7,8,9]
a2_new = []

for values in a2:
    a2_new.append(values+5)
print (a2_new)

def func6(x,y,z):
    int_func1 = lambda x,y: x*y
    return (int_func1(x,y)*z)
one = int(input("Enter first digit: "))
two = int(input("Enter second digit: "))
three = int(input("Enter thrid digit: "))

print (func6(one,two,three))


def add_values(x,y,z):
    int_func7 = lambda x,y: x+y
    return (int_func7(x,y) + z)   #REVIEW - int_func7(x,y)

x_1 = int(input("First value?: "))
y_1 = int(input("First value?: "))
z_1 = int(input("First value?: "))

print(add_values(x_1,y_1,z_1))




def subtract_three_values(x,y,z):
    inter_5 = lambda x,y: x-y
    return (inter_5(x,y) - z)

print  (subtract_three_values(3,4,5))




def multiplication2 (x,y,z):
    inter4 = lambda x,y: x*y
    return (inter4(x,y) * z)


multi2_1 = int(input("Enter frist value: "))
multi2_2 = int(input("Enter second value: "))
multi2_3 = int(input("Enter thrid value: "))

print (multiplication2(multi2_1,multi2_2,multi2_3))


for i in range(10):
    action = (lambda x: x**2)
print (action)
