my_tuple = ("Dallas", "Austin", "SanAntonio", "Houston")


my_iteration1 = iter(my_tuple)

print (next(my_iteration1))
print (next(my_iteration1))
print (next(my_iteration1))
print (next(my_iteration1))


for values in my_tuple:
    print (values)



my_list = [1,2,3,4,5,6]

my_iteration2 = iter(my_list)

print (next(my_iteration2))
print (next(my_iteration2))
print (next(my_iteration2))
print (next(my_iteration2))
print (next(my_iteration2))
print (next(my_iteration2))


my_str = "banana"

iteration_3 = iter(my_str)

print (next(iteration_3)) # prints b

for letters in my_str:
    print (letters)

my_dict = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}

iteration_4 = iter(my_dict)
print (next(iteration_4))
print (next(iteration_4))

my_list3= [1,2,3,4,5,6]

iteration_5 = iter(my_list3)
print (tuple(my_list3))
for value,count in enumerate(my_list3,100):
    print (value,count)

z = [1,2,3,4,5,6,7,8,9,10]

iter_6 = iter(z)

print (list(filter(lambda x: x!=6,z)))

l2 = [1,2,3,4,5,6,7,8,9]






