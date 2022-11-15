import math

def yourmom():
    global X
    X = 234
    print ("Hello")
yourmom()

def addition(x,y):
    """
    Addition DocString
    """
    #one = int(input("Enter an integer: "))
    #two = int(input("Enter a second integer: "))
    z = x + y
    #print (z)
addition(5,3)


print("Enter your wish")
wish = input()
print("May your wish come true!", wish)

def times(x,y):
    print (x*y)
times ("Hi",4)


original_numbers = [1,2,3,4,5,6,7,8,9]
new_list = []
for values in original_numbers:
    new_list.append(values**2)
print(new_list)

def intersect(seq1, seq2):
    intersect_newlist = []
    for values1 in seq1:
        if values1 in seq2:
            intersect_newlist.append(values1)
    print (intersect_newlist)
#outisde the intersect function
print ("Enter first word: ")
seq1_edit = input()
print ("Enter second word: ")
seq2_edit = input()
intersect(seq1_edit, seq2_edit)

#global variable defined in yourmom
print (X)



#global variables
global INT
INT = 99
def GLOBAL():
    global INT
    INT = 88
GLOBAL()





VALUE = 99
def f1():
    VALUE = 88
    def f2():
        print (VALUE)
    f2()
f1()
