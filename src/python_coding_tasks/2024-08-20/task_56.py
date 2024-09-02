# program  to find max of 3 numbers
num1 = float(input("Enter number1"))
num2 = float(input("Enter number2"))
num3 = float(input("Enter number3"))



if num1 > num2 and num1 > num3 :
    print(f"{num1} is greater than {num2} and {num3}")
elif num2 > num3 and num2 > num1:
    print(f"{num2} is greater than {num1} and {num3}")
else:
    print(f"{num3} is greater than {num1} and {num2}")