# try except and finally

try:
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    result = num1/num2
except ValueError as ve:
    print("Value error, please enter only integers ",ve)
except ZeroDivisionError as zd:
    print("Please do not enter number2 as zero: ",zd)
else:
    print(f"Result is {result}")
finally:
    print("This code will always be executed")