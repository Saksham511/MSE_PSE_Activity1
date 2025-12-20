from mammal import Mammal
class Dog:
    def __init__(self,name,food,breed):
        self.name=name
        self.food=food
        self.breed=breed
    def speak(self):
        print("woof!","I am",self.name,", a",self.breed,". My favourite food is",self.food)