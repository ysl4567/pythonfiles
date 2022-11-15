a = [1,2,3,4,5,6]
obj1 = enumerate(a)
print (type(obj1))
print (list(enumerate(a))) #type(enumerate(a))
print (tuple(enumerate(a)))


for i in enumerate(a):
    print (i)

my_tuple = ("Dallas", "Austin", "SanAntonio", "Houston")
my_list = [1,2,3,4,5,6]
my_dict = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}

for values in enumerate(my_list): #enumeration
    print (values)

for cities in enumerate(my_tuple): #enumeration
    print (cities)

for values in enumerate(my_dict):
    print (values)

list1 = [1,2,3,4,5,6,7,8,9,10]
enum_1 = enumerate(list1)
print (list(enum_1))


str2 = (1,2,3,4,5)
enum_2 = enumerate(str2)
print (tuple(enum_2))

string3 = "asdf"
enum_4 = enumerate(string3)
print (list(enum_4))

# REVIEW

l1 = ["eat", "sleep", "repeat"]
for values,count in enumerate(l1,100):
    print (values,count)

letters = ["a","b","c","d","e","f","g","h"]
enum_5 = enumerate(letters,100)
print (list(enum_5))

for numbers in enumerate(range(5)): #range(5) = 0,1,2,3,4
    print (numbers)

G = (1,2,3,4,5,6,7,8,9,10)
G_new = [x**2 for x in G]
print (G_new[2])

spam = "SPAM"
spam_new = [letters*4 for letters in spam]
print (spam_new)

#iteration and for loop
spam = "SPAM"
spam_new2 = iter([letters*4 for letters in spam])
print (next(spam_new2))


S1 = "abc"
S2 = "xyz123"
New_S1_S2 = iter([letter1 + letter2 for letter1 in S1 for letter2 in S2])
print (next(New_S1_S2))

values_1 = "123"
values_2 = "456"

New_v1_v2 = iter((no1 + no2 for no1 in values_1 for no2 in values_2))
print (next(New_v1_v2))




my_dict = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}


my_dict_v1_v2 = iter(v1+v2 for v1 in my_dict for v2 in my_dict)
print (next(my_dict_v1_v2))


my_list_3 = [1,2,3,4,5,6]


for numbers in enumerate(my_list_3):
    print (numbers)


word = "word"

word_four = [x*4 for x in word]
print ((word_four))

for words in enumerate(word):
    print (words)



list_4 = [1,2,3,4,5,6,7,8,9]

for numbers in enumerate(list_4):
    print (numbers)


print ("\n")

hello = "HELLO"
print_hello = [letter * 4 for letter in hello]
print (print_hello)

print_hello_enum = enumerate(hello)

print (list(print_hello_enum))




