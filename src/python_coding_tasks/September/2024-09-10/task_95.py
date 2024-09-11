# custom exception

class BalanceLowException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)


balance = 100
withdraw = int(input("Enter the amount to withdraw"))
if withdraw > balance:
    raise BalanceLowException("Balance is Low")
else:
    print("Your balance is :",(balance - withdraw))
