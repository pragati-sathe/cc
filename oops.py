class Person:
    def __init__(self,name,like,hate):
        self.name=name
        self.like=like
        self.hate=hate

    def taste(self,food):
        if food in self.like:
            print (f"{self.name} eats {food} and loves it !")
        elif food in self.hate:
            print (f"{self.name} eats {food} and hates it !")   
        else:
            print (f"{self.name} eats {food} !")      

p1=Person("Tom",["ice cream"],["carrots"])
p1.taste("carrots")
p1.taste("ice cream")
p1.taste("banana")
