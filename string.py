# checking if the string contains all the words in the chars
string = "santhanabharathi"
chars = ['a', 'e', 'u']

yes_itcontain = True
for ch in chars:
    if ch not in string:
        yes_itcontain = False
        break
if yes_itcontain:
    print ("yes, it  has all the words which contains in the list")
else:
    print("no the string doesnot have all the characters from the list")
#replace every vowel in the string with the next item in the list
vowels = ['a', 'e', 'i', 'o', 'u']

string = "santhanabharathi"
result = ""

for ch in string:
    if ch in vowels:
        idx = vowels.index(ch)
        new_idx = (idx + 1) % len(vowels)   # move to next vowel (wrap around)
        result += vowels[new_idx]
    else:
        result += ch

print(result)

#Replace characters at even indexes with characters from a list (repeating list if needed).
string = "abcdefghij"
replace_list = ['X', 'Y']

result = ""
list_index = 0   

for i in range(len(string)):
    if i % 2 == 0:  
        result += replace_list[list_index]
        list_index = (list_index + 1) % len(replace_list)  
    else:
        result += string[i]

print(result)
