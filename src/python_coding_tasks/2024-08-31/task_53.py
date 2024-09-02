# Creation of Employee class and Objects
class Employee:

    # Attributes
    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self,emp_list):
        self.name = emp_list[0]
        self.age = emp_list[1]
        self.phone = emp_list[2]
        self.address = emp_list[3]
        self.eid = emp_list[4]

    #Behaviours
    def walk(self):
        print(f"{self.name} can walk")

    def talk(self):
        print(f"{self.name} can talk")

    def printdetails(self):
        print(f"The employee details are name : {self.name}, age : {self.age}, phone : {self.phone}, "
              f"address : {self.address}, employee_id: {self.eid}")


name = input("Enter employee's name\t")
age = int(input("Enter employee's age\t"))
phone = int(input("Enter employee's phone number\t"))
address = input("Enter employee's address\t")
eid = int(input("Enter employee's id\t"))
emp_list = [name,age,phone,address,eid]

emp1 = Employee(emp_list)
emp1.talk()
emp1.walk()
emp1.printdetails()