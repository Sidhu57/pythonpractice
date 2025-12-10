class srm:
    def __init__(self):
        self.name = ""
        self.dept =  ""
    def college (self):
        print("Name :" ,self.name)
        print("Dept :" , self.dept)
d1 = srm()
d2 = srm()
d1.name="sidhu"
d1.dept="ece"
d2.name="shelin"
d2.dept="cse"
d1.college()
d2.college()
    