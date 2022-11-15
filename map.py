a=[1,2,3,4,5]
a_new = []

newList = list(map(lambda x:x+5,a ))
print (newList)

for values in a[1:]:
    a_new.append(values+5)
print (a_new)



no1 = [1,2,3]
no2 = [4,5,6]

newList = list(map(lambda x,y: x+y, no1,no2))
print(newList)

cities = ["Dallas", "Tokyo"]
newList2 = list(map(list,cities))
print (newList2)



b = [1.2,3,4,5]

b_new = list(map(lambda x: x+5,a))
print (b_new)


no13 = [8,9,0]
no23 = [5,6,7]

new_list = list(map(lambda x,y: x+y, no13,no23))

print (new_list)


c = [1,2,3,4,5,6,7,8,9,10]

c_new = list(filter(lambda x: x%2!=0,c))
print (c_new)


def add7(x):
    return x + 7


def isOdd(x):
    return x%2!=0


d = list(map(add7,a))
print(d)

b = list(map(add7,filter(isOdd,a)))
print(b)

z = [1,2,3,4,5,6]
z_new = list(map(lambda x: x+7,z))
print (z_new)

cities_2 = ["Austin", "Dubuque"]
cities_2_new = tuple(map(tuple,cities_2)) #two arguments - REVIEW
print (cities_2_new)








def dictionary_3_keys(**kargs):
    for keys in kargs.keys():
        print (keys)

print (dictionary_3_keys(a = 1, b= 2, c=3, d=4))


def dictionary_3_values(**kargs):
    sum = 0
    for values in kargs.values():
        sum = sum + values
    return (sum)
print (dictionary_3_values(a = 1, b= 2, c=3, d=4))


def secondpower(x):
    for i in range(10):
        action = (lambda x: x**2)
        return (action)