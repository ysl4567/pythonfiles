#Example 1 - Nested Function
#outside enclosing function
from re import X


def outerfunction(text):
    #local function - innerfunction
    def innerfunction():
        print (text)
    innerfunction()
outerfunction("Hello")
print("\n") # Enter, space
print(outerfunction("Hello"))
print("\n")

#Example 1b 
def outerfunction2(text):
    print (text)
outerfunction2("1b - Hello")

#Example 2 - Nested Function


a = [1,2,3,4,5,6,7,8]
a.insert(4,56)
print (a)


a = [1,2,3,4,5,6,7]
def insert_my_list(list):
    def remove_intermediate_value(my_value):
        return my_value[len(list)-4]
    list.insert(remove_intermediate_value(list),"why")
    return (list)
print(insert_my_list(a))


def pop(list): 
    def get_last_item(my_list):
        return my_list[len(list)-1]

    list.remove(get_last_item(list))
    return list

b = [1,2,3,4,5,6,7,8,9]
print (pop(b))


#Closures Functions

def outer(message):
    #msg = message
    def inner():
        print (message)
    return inner
my_func = outer("Hi")
my_func()





#NonLocal Statement

def outerfn():
    x = "Hello"
    def innerfn():
        nonlocal x
        x = "Bye Bye"
    innerfn()
    return x
print (outerfn())

def outerfn():
    x = "Hello"
    def innerfn():
        #nonlocal x
        x = "Bye Bye"
    innerfn()
    return x
print (outerfn())


#pop function


def pop(b):
    (b.pop(len(b)-1))
    return (b)

asdf=[1,2,3,4,5,6]
print (pop(asdf))










