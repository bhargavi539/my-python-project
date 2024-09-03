#program to take input from the user and calculate sum, subtract, divide, multiply
#whenever we take input using input method. It is string type, we need to format to int type to perform calculations

num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
print(type(num1))
print(type(num2))
print("sum of num1 and num2 is", num1+num2)
print("sub of num1 and num2 is", num1-num2)
print("mul of num1 and num2 is", num1*num2)
print("div of num1 and num2 is", num1/num2)