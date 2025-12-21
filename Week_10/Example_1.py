from abc import ABC









class Animal:
   def eat(selfself):
       print("This animal is eating food")

class Dog(Animal):
    def bark(self):
        print("This dog barks")


d = Dog()
d.bark()
d.eat()
