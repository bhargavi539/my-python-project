# Creating a class and its instance using constructor
class Person:

    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")


anvar = Person("Anvar")
anvar.walk()

jacob = Person("Jacob")
jacob.walk()