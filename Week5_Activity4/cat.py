from mammal import Mammal
class Cat(Mammal):
    def __init__(self,name,food,breed):
        super().__init__(name,food)
        self.breed=breed
    def speak(self):
        print("meow!","I am",self.name,", a",self.breed,". I eat",self.food)