class phone:
    chargertyp = "C-TYP"
    def __init__(self):
        self.brand = "iphone"
        self.price = 50
    def setValue(self,brand,price):
        self.brand = brand
        self.price = price
    def getValue(self):
        print(self.brand)
        print(self.price)
    @classmethod
    def changechargertyp (cls):
        cls.chargertyp= "B-typ"
        print("chage the charger type to B")
    @staticmethod
    def info ():
        print("this phone is much valuable")
        
t1=phone()
t1.setValue("Apple",200000)
t1.getValue()

phone.changechargertyp()
t1.info()
