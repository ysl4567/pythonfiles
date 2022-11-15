a = [1,2,3,4,5,6]

#list comprehension
b = [x+5 for x in a]
print (b)

c2 = [x+6 for x in a]
print (c2)

#map
c = list(map(lambda x: x+5, a))
print (c)


#filter

d = list(filter(lambda x: x%2!=0,a))
print (d)


#double for loop
e = [x+y for x in "spam" for y in "SPAM"]
print (e)

spam = "spam"
SPAM = "SPAM"

for letters in spam:
    for letters2 in SPAM:
        print ([letters+ letters2])


#Matrices
M = [[1,2,3],[4,5,6],[7,8,9]]
N = [[2,4,6],[8,10,12],[14,16,18]]

print (M[1][2])

M2 = [row[1] for row in M]
print (M2)

M3 = [M[row][1] for row in (0,1,2)]
print (M3)

M4 = [M[row][col]*N[row][col] for row in range(3) for col in range(3)]
print (M4)



list_10 = [1,2,3,4,5,6]

add_1 = [numbers+5 for numbers in list_10]
print (add_1)



n_list = ["happ",[0,1,2,3]]

print (n_list[1][0])

print ("\n")
print ("\n")

my_list = [1,2,3,4,5,6]

print (my_list[-1])
print (my_list[-6])
print (my_list[-3:-1])
print (my_list[0:6])
print (my_list[0:6:2])
print (my_list[:-7:-1])
print (my_list[:])


#lists are mutable
print ("\n")
my_list2 = [1,2,3,4,5,6,7,8,9]
my_list2.append(10)
print (my_list2)
my_list2.insert(3, "why")
print (my_list2)

#strings are mutable
odd = [1,3,5,7,9]
odd[0:5] = [2,4,6,8,10]
print (odd)

odd.insert(5,12)

print (odd)

odd.extend([14,16,18])
print (odd)

odd.insert(0,1)
print (odd)

odd[2] = 7
print (odd)

odd.insert(0,0)
print (odd)


list1 = [1,2,3,4,5,6,7,8,9]
print (len(list1))
print (list1[-1:(-len(list1)-1):-1]) #print list backwards
print (list1)

del list1[3]
print (list1)

del list1[0:3]
print (list1)


print ("\n")
my_list1 = [1,2,3,4,5,6,7,8,9,10]
my_list1.pop(5) #index value
print ( my_list1)

my_list2 = ['p','r','o','b','l','e','m']
my_list2.remove('p')
print (my_list2)

print ("\n")
my_list2.clear()
print (my_list2)


numbers = [2, 3, 5, 2, 11, 2, 7]
numbers_2 = [2,3,5,11,7]

# check the count of 2
print (numbers.count(2))
print (numbers.index(2))
numbers.clear()
print (numbers)

alphabet = ['b','a','c','d','e','f']
x = sorted(numbers)
print (x)
print ("\n")

second_power = [2**x for x in range(11)]
print (second_power)


print ("\n")

a = [1, 11, 2]

x = sorted(a)
print(x)

y = sorted(numbers_2) #can't have two of the same number
print (y)




for values in range(6,10):
    values_4 = values+4
    print (values_4)
print ("\n")

b = x.copy()
print (x)

print_line = "%s is %d inches long" # %s = string, %d = number
print (print_line%("The ruler", 12))


