alphabet = ['a','b','c','d','e','f','g','h','i','j','k,','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
input1 = input("Enter an encoded string value: ")
input1_lower = input1.lower()
print (input1_lower)
input1_lower_list = []
decoded_list = []

for letter in input1_lower:
    input1_lower_list.append(letter)
#print(input1_lower_list)

for letters in input1_lower_list:
    index = alphabet.index(letters)
    new_index = index + 3
    decoded_list.append(alphabet[new_index])
#print (decoded_list)

print(''.join(decoded_list))
