# Creating an Object based on user input (using for loop)

class Person:

    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}")


# List to hold the created Person objects
people = []

# Number of persons to create
people_count = int(input("How many people do you want to add? "))

for _ in range(people_count):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    occupation = input("Enter occupation: ")
    # Create a new Person object and add it to the list
    person = Person(name, age, occupation)
    people.append(person)

# Display information for all persons created
print("\nPeople added:")

for person in people:
    person.display_info()
