# Another program to convert real world entities into Objects and classes
class Dog:
    # Attributes
    name = None
    color = None
    age = None

    # Behaviours
    def sleep(self):
        print("sleep method")

    def bark(self):
        print("bark method")


dog1 = Dog()
dog1.name = "Labrador"
print(dog1.name)
dog1.bark()

dog2 = Dog()
dog2.name = "Pom"
print(dog2.name)
dog2.sleep()

