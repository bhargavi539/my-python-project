# OOPs
# Class - Blueprint
# OBject - Instance of class
# Encapsulation - private __, protected _, public.
# Inheritance - single, multiple, multilevel, hierarchical, hybrid
# Poly - method overriding, method overloading(x)
# self, super, __init__

# Abstraction
# Hide the details and show what is required.

# ABC is a class provided by abc module that can be used as the base class for defining abstract classes

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
       print("Bark")


dog = Dog()
dog.sound()
