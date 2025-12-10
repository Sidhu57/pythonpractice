class sidhu():
    def money(self):
        print("money")
class shelin():
    def rent(self):
        print("rent")
class ponki(shelin,sidhu):
    def exchange(self):
        print("exchange")
m1 = ponki()
m1.exchange()
m1.rent()
m1.money()
# multiple inheritance 
# hence i can acess the both sidhu and shelin class with the class ponki