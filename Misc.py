def AppendList(new_value):
    x = []
    x.append(new_value)
    return (x)

print (AppendList(42))
print (AppendList(21))

list_1 = [1,2,3,4,5,6,7,8,9]

plus_five = [x+5 for x in list_1]
print (plus_five)

list_2 = list(map(lambda x: x+5, list_1))
print (list_2)

list_3 = list(filter(lambda x: x%2 ==0, list_1))
print (list_3)

print (len(list_1))




def add_five(x):
    inter3 = lambda x: x+3
    return (inter3(x)+2)

print (add_five(5))

list_2 = [1,2,3,4,5,6,7,8,9]

list_3 = list(filter (lambda x: x%2 == 0, list_2))
print (list_3)


def MultiplesOf(x):
    inter3 = lambda x: [x*i for i in range(11)]
    return (inter3(x))
    

input_1 = int(input("Enter integer: "))
print (MultiplesOf(input_1))


#
print_line_2 = "I am %s and %d"
print (print_line_2 % ("yourmom", 4))




list_5 = [1,2,3,4,5,6,7,8,9]

print(list_5[6:9])

