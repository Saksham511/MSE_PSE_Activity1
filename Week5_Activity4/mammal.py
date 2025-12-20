from animal import Animal
class Mammal:
    def __init__(self,name,food):
        self.name=name
        self.food=food
    def speak(self):
        print("I am mammal")
    def eat(self):
        print("I eat",self.food)
