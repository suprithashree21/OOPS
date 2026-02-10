from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  
    def sleep(self):
        print("Sleeping...") 
class Dog(Animal):
    def sound(self):
        print(" Animal Barks")
class Cat(Animal):
    def sound(self):
        print(" Cat makes sound as Meow")
class Cow(Animal):
    def sound(self):
        print(" Cow makes sound as Moo")
dog = Dog()
cat = Cat()
cow = Cow()
dog.sound()
dog.sleep()
cat.sound()
cat.sleep()
cow.sound()
cow.sleep()