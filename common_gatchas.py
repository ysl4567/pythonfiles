#https://docs.python-guide.org/writing/gotchas/
#1 - Mutable Default Arguments 

def MutableDefaultArguments (element, new_list=[]):
    new_list.append(element)
    return (new_list)

print (MutableDefaultArguments(42))
print (MutableDefaultArguments(21))

#2 - Late Binding Closures

def EvenNumbers():
    return [2*i for i in range(6)]

print (EvenNumbers())

def Multipleof(x):
    inter_3 = lambda x: [x*i for i in range(11)] #REVIEW - lambda goes outside the list
    return (inter_3(x))
print (Multipleof(3))


print_line = "%s and %d"
print (print_line%("asdf", 3))



def MultipleofNumber(x):
    intermediate3 = lambda x: [x*i for i in range(11)]
    return (intermediate3(x))

integer_input_1 = int(input("What multiple: "))
print (MultipleofNumber(integer_input_1))


print ("\n")

def EvenNumbers(x):
    intermediate_3 = lambda x: [x*2 for x in range(1,11)] #starting from 2*1 to 2*10
    return (intermediate_3(x))
print(EvenNumbers(11))


def AppendList(x):
    newList = []
    newList.append(x)
    return (newList)
print (AppendList(42))
print (AppendList(21))



