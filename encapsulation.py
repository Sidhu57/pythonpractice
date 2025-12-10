class college():
    def __init__(self):
        self.collegename = "SRM"
    
s1 = college()
s1.collegename = "VALLIAMMMAI"
print(s1.collegename)
# public access modifiers  
# hence here college is a public variable so it can also be changed outside the class
class family():
    def  __init__(self):
        self._sonname = "sidhu"
class family2(family):
    def display(self):
        print(self._sonname)
d1 = family2()
d1._sonname = "shelin"
print(d1._sonname)
#protective access modifiers
# hence here _sonname has been used since we used" _" it means it is can be accesed over the class to class
class showroon():
    def __init__(self):
        self.__bike = "ROYAL ENFEILD"
    def display(self):
        print(self.__bike)
f1 = showroon()
f1.display()
#private access modifiers
# hence here __bike has been used and since we used "__" it means it cannot be accessed its class
        