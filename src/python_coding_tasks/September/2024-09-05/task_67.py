# Deeper understanding of how private, public and protected attributes

class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)
        print("This is check_balance method")
        self.__internal_method()

    def show_account_number(self, is_auth):
        if is_auth:
            print(self.__account_number)
        else:
            print("Access denied")

    def __internal_method(self):
        print("This is a private internal method ",self.__account_number)
        print("This a private method")


nykredit = Bank(45364356, 1000)
nykredit.check_balance()
nykredit.deposit(2500)
nykredit.check_balance()
nykredit.show_account_number(False)
nykredit.show_account_number(True)