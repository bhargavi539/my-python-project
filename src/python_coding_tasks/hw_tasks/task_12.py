# Creation of Employee class and Objects
class Employee:

    # Attributes
    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self,name,age,phone,address,eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    #Behaviours
    def walk(self):
        print(f"{self.name} can walk")

    def talk(self):
        print(f"{self.name} can talk")

    def printdetails(self):
        print(f"The employee details are name : {self.name}, age : {self.age}, phone : {self.phone}, "
              f"address : {self.address}, employee_id: {self.eid}")


name1 = input("Enter employee's name\t")
age1 = int(input("Enter employee's age\t"))
phone1 = int(input("Enter employee's phone number\t"))
address1 = input("Enter employee's address\t")
eid1 = int(input("Enter employee's id\t"))
emp1 = Employee(name1,age1,phone1,address1,eid1)
emp1.talk()
emp1.walk()
emp1.printdetails()


name2 = input("Enter employee's name\t")
age2 = int(input("Enter employee's age\t"))
phone2 = int(input("Enter employee's phone number\t"))
address2 = input("Enter employee's address\t")
eid2 = int(input("Enter employee's id\t"))
emp2 = Employee(name2,age2,phone2,address2,eid2)
emp2.talk()
emp2.walk()
emp2.printdetails()