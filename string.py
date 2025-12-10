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