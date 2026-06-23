# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is asleep")
    
class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("Lucky")
cat = Cat("Droo")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.speak()
dog.sleep()

print("-")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.speak()
cat.sleep()