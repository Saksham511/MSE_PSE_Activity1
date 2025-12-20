from mammal import Mammal
class Cat:
    def __init__(self,name,food,breed):
        self.name=name
        self.food=food
        self.breed=breed
    def speak(self):
        print("meow!","I am",self.name,", a",self.breed,". I eat",self.food)