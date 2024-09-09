# One more example on Abstraction

from abc import ABC,abstractmethod

class PyATM(ABC):
    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("Enrolled for the course")

class Student(PyATM):

    def payfee(self):
        print("Course fee paid")


jay = Student()
jay.enrolled()
jay.payfee()

# python_course = PyATM() -> cannot instantiate abstract class
