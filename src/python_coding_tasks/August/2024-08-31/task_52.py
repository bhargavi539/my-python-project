"""
Class creation using __init__ constructor to initialize variables in the class

"""
class Dog:

    # attributes
    name = None
    age = None

    def __init__(self, name,age):
        print("Default construction to initialize variables")
        self.name = name
        self.age = age


    def sleeping(self):
        print(f"{self.name} is sleeping")


dog1 = Dog("Snoopy",12)
print(dog1.name)
dog1.sleeping()