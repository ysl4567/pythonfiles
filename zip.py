import math
#zip
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print (list(x))


#iter,zip
y = iter(zip(a,b))
print (next(y))

print ("\n")

#enum
enum_z = enumerate(a)
print (list(enum_z))


def values (*x):
    return x

print (values(2,3,4,5))

print (abs(-2))
print (pow(3,2))

print ("\n")

enum_b = enumerate(b)
print (list(enum_b))