# Creating a person's attributes and behaviours into an Object and Class
# Implementing OOPs Concept on real world entities

class Person:
    #Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    phone_number = None
    address = None

    # Behaviours
    def talk(self, name):  # No return with argument
        print(f"{name} can talk")

    def sleep(self):  # no argument no return type
        print("I am a class method")
        print("Sleep method")

    def walk(self):  # no argument with return
        print("Can walk")
        return None


# Creating an Object of a class
#ObjectRef = ClassName()

manfred = Person()
manfred.name = "Manfred"
print(manfred.name)

oliver = Person()
oliver.name = "Oliver"
print(oliver.name)
oliver.sleep()
oliver.talk("Oliver")
