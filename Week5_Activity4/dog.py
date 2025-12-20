from mammal import Mammal
class Dog(Mammal):
    def __init__(self,name,food,breed):
        super().__init__(name,food)
        self.breed=breed
    def speak(self):
        print("woof!","I am",self.name,", a",self.breed,". My favourite food is",self.food)