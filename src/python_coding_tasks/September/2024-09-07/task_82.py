# More about abstraction
# Hide the details and show what is required.

# ABC is a class provided by abc module that can be used as the base class for defining abstract classes


from abc import ABC,abstractmethod

class Father(ABC):

    def __init__(self,amount):
        self.amount = amount

    @abstractmethod
    def loan(self):
        pass


class Son(Father):

    def loan(self):
        print("Paid the Loan")


son_obj = Son("100K")
son_obj.loan()