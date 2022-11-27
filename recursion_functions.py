# factorial recursion
def factorials(number):
    if number == 1 or number == 0:
        return number
    else:
        return (number * (factorials(number-1)))


input_value = int(input("Enter integer value: "))

print (factorials(input_value))


#addition of first n digits recursion
def addition(number):
    #while (number < 20):
        if number <= 0:
            return (number)
        else: 
            return (number + (addition(number-1)))

input_value2 = int(input("Enter integer value: "))
print(type(input_value2))
print (addition(input_value2))

#input_value2 = int(input("Enter integer value: "))
#print (addition(input_value2))

def factorial2(number):
    if number == 1 or number == 0:
        return number
    else:
        return (number * factorial2(number-1))

inputfactorial2 = int(input("Enter an integer value: "))
print (factorial2(inputfactorial2))


#Recursion Function
#Summation with Recursion
#add the first n numbers
def summation_of_first_n_numbers(number):
    if number == 1 or number == 0:
        return (number)
    else:
        return (number + summation_of_first_n_numbers(number-1))
    
input_value3 = int(input("Enter an integer value: "))
print (summation_of_first_n_numbers(input_value3))


