a = [1,2,3,4,5,6,7,8,9]


def add7(x):
    return x+7
    
def isOdd(x):
    return x%2 !=0

c = list(filter(isOdd,a))
print (c)

d = list(map(add7,a))
print(d)

b = list(map(add7,filter(isOdd,a)))
print(b)




c = [1,2,3,4,5,6,7,8,9,10]

c_new = list(filter(lambda x: x%2!=0,c))
print (c_new)

c_list = ["a","b","c"]

new_c = list(filter(lambda x: x!="c" , c_list)) #two arguments, REVIEW

print (new_c)


words = ["words","hello", "by", "tom", "a"]

words_new = list(filter(lambda word: len(word)>=3 , words))
print (words_new)

dict_2 = {x*x for x in range(10)}
print (dict_2)


f = [1,2,3,4,5,6,7,8,9]

f_new = list(filter(lambda x: x%2==0, f))
print (f_new)


print (*f)
print (f)
print (tuple(f))




def multiply(*x):
    value = 1
    for numbers in x:
        value = value * numbers
    print (value)


qwerty = [1,2,3,4,5,6,7,8,9,10]


inter3 = list(filter(lambda x: x%2!=0,qwerty))
print (inter3, type(inter3))



list_1 = [1,2,3,4,5,6,7,8,9,10]

odd_only = list(filter(lambda x: x%2!=0,list_1))
print (odd_only)
print (type(odd_only))






