dict_2 = {x*x for x in range(10)}
print (dict_2)

dict_3 = {x*x for x in range(10) if x%2!=0}
print (dict_3)


a = [1,2,3]
b = [4,5,6]

a_b = [numbers1+numbers2 for numbers1 in a for numbers2 in b]
print (a_b)

a_b_plus = list(map(lambda x,y:x+y, a,b))
print (a_b_plus)


print ("\n")
my_list1 = [1,2,3,4,5,6,7,8,9,10]
my_list1.pop(5)
print ("asasdf", my_list1)




list1 = [1,2,3,4,5,6,7,8,9]
comp1 = [number+1 for number in list1]
print (list1)
print (comp1)
