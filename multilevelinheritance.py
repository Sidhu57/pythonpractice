class mom():
    def mom(self):
        print("car")
class daughter(mom):
    def daughter(self):
        print("sweet")
class son(daughter):
    def son(self):
        print("bike")
n1 = son()
n1.son()
n1.daughter()
n1.mom()
#multilevel inheritance
# hence i  can able to  acess the class daughter with the class son
# and also when i have acess to the class daughter  and in can also able to  acess the mom class with the class son