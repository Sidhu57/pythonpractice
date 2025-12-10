class teacher:
    def __init__(self,name,regno):
        self.Name = name
        self.regno = regno
    def college(self):
        print("Name :", self.Name)
        print("regno:", self.regno)
d1 = teacher("SIDHU", "12222106127")
d2 = teacher("SHELIN", "12222106128")
d1.college()
d2.college()
         