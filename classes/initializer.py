

#initializer is a special method that is called whenever a blue print is called it creates an object
#It's a metod function inside a class

class Human():
    def __init__(self,name,gender,age):
        print("Intializer is being called")
        self.gender=gender
        self.name=name
        self.age=age
        if self.gender=="Female":
           self.ribs=23
           self.curse="pain"
        else :
            self.ribs=24
            self.curse="Suffer"   

    #def another_one(self):
      #  print("Another method")

    def print_self(self):
        print("_ _ _ _ _ _ _ _ _")
        print("name",self.name)
        print("gender",self.gender)
        print("age",self.age)
        print("ribs",self.ribs)
        print("curse",self.curse)
        print("_ _ _ _ _ _ _ _ _ ")  

#Maggie=Human(name="Maggie",gender="Female",age="12")
#adam.__init__()
#adam.another_one()
Maggie=Human(name="Maggie",gender="Female",age="12")
Maggie.print_self()
#John=Human(name="John",gender="Male",age="5")
#print("name",John.name)
#print("gender",John.gender)
#print("ribs",John.ribs)
#print("curse",John.curse)