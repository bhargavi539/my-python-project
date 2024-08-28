#Convert the following code into lambda code
"""def power_num(num):
    return math.pow(num,2)

op = power_num(5)
print(op)
"""
import math

output = lambda :math.pow(int(input("Enter the number")),2)
print(output())