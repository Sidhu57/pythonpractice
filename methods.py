class phone :
    chargertype = "C"
    def __init__(self):
        self.brand = ""
        self.price = ""
    def setprice(self, brand, price):
        self.brand = brand
        self.price = price
    def getprice(self):
        print("Brand :",self.brand)
        print("Price :",self.price)
        print("ChargerType :" , phone.chargertype)

    @classmethod
    def changechargertype(cls):
        cls.chargertype = "B"
        print("change the charger type to B")
    @staticmethod
    def info():
        print("this phone is much valuable")
    


s1= phone()
phone.changechargertype()
s1.setprice("Apple", 20000)
s1.getprice()
s1.info()
    

        