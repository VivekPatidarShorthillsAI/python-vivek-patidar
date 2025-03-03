from abc import ABC, abstractmethod

# Defining an Interface
class Animal(ABC):  
    @abstractmethod
    def make_sound(self):  # Abstract method
        pass

# Implementing the interface
class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow
