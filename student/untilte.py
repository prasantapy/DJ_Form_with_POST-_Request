from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        print('speak')
    
class Dog(Animal):
    def speak(self):
        print('bow bow')
class Cat(Animal):
    def speak(self):
        print('mou mou')

obj1=Dog()
obj2=Cat()
obj1.speak()
obj2.speak()
