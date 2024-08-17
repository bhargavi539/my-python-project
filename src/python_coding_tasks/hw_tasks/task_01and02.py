#Task 1
# Home Can you create a Program I will give you number(userinput and print table)

table = int(input("Enter a number"))
print(f"{table} * 1 = {table*1}")
print(f"{table} * 2 = {table*2}")
print(f"{table} * 3 = {table*3}")
print(f"{table} * 4 = {table*4}")
print(f"{table} * 5 = {table*5}")
print(f"{table} * 6 = {table*6}")
print(f"{table} * 7 = {table*7}")
print(f"{table} * 8 = {table*8}")
print(f"{table} * 9 = {table*9}")
print(f"{table} * 10 = {table*10}")

"""
Task #2

Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

print(f"Maximum value of {num1} and {num2} is ", max(num1,num2))
print(f"{num1} to the power of {num2} is",pow(num1,num2))
print(f"sum of {num1} + {num2} is", num1+num2)
print(f"sub of {num1} - {num2} is", num1-num2)
print(f"mul of {num1} * {num2} is", num1*num2)
print(f"div of {num1} / {num2} is", f"{num1/num2:.5f}")