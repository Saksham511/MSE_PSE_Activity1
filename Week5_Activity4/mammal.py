from animal import Animal
class Mammal(Animal):
    def __init__(self,name,food):
        super().__init__(name)
        self.food=food
    def speak(self):
        print("I am mammal")
    def eat(self):
        print("I eat",self.food)
