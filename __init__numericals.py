class calculator:
    def __init__(self,a,b):
        self.a= a 
        self.b= b
    def add(self):
        print("Addition :", self.a + self.b)
    def sub(self):
        print("Subtraction :", self.a - self.b)
    def mul(self):
        print("Multiplication :", self.a * self.b)
    def div(self):
        print("Division :", self.a / self.b)
f1 = calculator(10,10)
f2 = calculator(10,10)
f3 = calculator(10,10)
f4 = calculator(10,10)
f1.add()
f2.sub()
f3.mul()
f4.div()

