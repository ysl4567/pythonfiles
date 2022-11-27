def names(*randoms):
    for values in randoms:
        print ("Hello,", values)
names("John","Bob","Hamilton","Lane")
print ("\n")

def addition(*numbers):
    current_value = 0
    for number in numbers:
        current_value = current_value + number
    print (current_value)

addition(1,2,3,4,5,6)
print ("\n")
