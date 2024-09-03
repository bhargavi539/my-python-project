# Take an input from the user and create a class in Python

class Person:

    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = int(input("Enter the age\n"))
        self.phone = int(input("Enter the phone\n"))
        self.occupation = (input("Enter the occupation\n"))

    def display_information(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone is {self.phone}")
        print(f"occupation is {self.occupation}")


# Create an Object
person1 = Person()

#Call the class function using an object
person1.display_information()