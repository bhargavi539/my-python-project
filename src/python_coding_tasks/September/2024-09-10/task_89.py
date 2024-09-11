# More understanding about exceptions
print("Start of the program")
try:
    a = int(input("Enter the num1")) # ValueError: invalid literal for int() with base 10: ' aa'
    b = int(input("Enter the num2"))
    c = a/b # ZeroDivisionError: division by zero
    print(f"{a} divided by {b} is:",c)

except Exception as e:
    print("Please check your inputs, should not be a zero or string ",e)


print("End of the program")