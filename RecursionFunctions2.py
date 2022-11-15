a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)

print (a)

#add list indexes - original order
summation_of_first_n_numbers_newlist = []
def summation_of_list_values(list):
    if len(list) == 1:
        return (list[0])
    else:
        return (list[0] + summation_of_list_values(list[1:]))
        #return (summation_of_first_n_numbers_newlist.append(list[len(list)-1]) + summation_of_list_values(summation_of_first_n_numbers_newlist.append(list[len(list)-1]-1)))

input_value = ['a','b','c','d']
print (summation_of_list_values(input_value))


#add list indexes - for loop version - integers only
#list = input("Enter list of values: ") #integers only
list = [1,2,3]
total_sum =0
for indices in list:
    total_sum = total_sum + indices
print (total_sum)


#add list indexes - for loop version - chars
list = ['a','b','c']
total_sum = ""                                      #STRING
for indices in list:
    #total_sum = total_sum + indices
    total_sum += indices
print (total_sum)
                                                    #OUTPUT = abc




