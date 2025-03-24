class Animal:
    def __init__(self, name):
        self.name = name

    

class Dog(Animal):  # Inheriting from Animal class
    def make_sound(self):
        print(f"{self.name} barks")

class Cat(Animal):  # Inheriting from Animal class
    def make_sound(self):
        print(f"{self.name} meows")

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.make_sound()
cat.make_sound()
