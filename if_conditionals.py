def if_conditions(): 

    input1 = int(input("Enter a value: "))
    input2 = int(input("Enter a value: "))

    if (input1 > 100 and input2 < 450):
        print ("Condition 1 met")

    elif (input1 < 50 or input2 > 10):
        print ("Condition 2 met")

    else:
        print ("Condition 3 met")    


if_conditions()

#OR

def if_conditions(input1,input2): 

    input1 = int(input("Enter a value: "))
    input2 = int(input("Enter a value: "))

    if (input1 > 100 and input2 < 450):
        print ("Condition 1 met")

    elif (input1 < 50 or input2 > 10):
        print ("Condition 2 met")

    else:
        print ("Condition 3 met")    


if_conditions(int, int)
