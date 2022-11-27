alphabet = ['a','b','c','d','e','f','g','h','i','j','k,','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
input1 = input ("Enter string value: ")
string1 = "Hello"
string1_lower = input1.lower()
print (string1_lower)
string1_list = []
caesar_list = []

for letters in string1_lower:
    string1_list.append(letters)
#print(string1_list)

for letter in string1_lower:
    index = alphabet.index(letter)
    #print (index)
    cipher_index = index - 3
    caesar_list.append(alphabet[cipher_index])
#print (caesar_list)

print ("Cipher version: ", ''.join(caesar_list))

