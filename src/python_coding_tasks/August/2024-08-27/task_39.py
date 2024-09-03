#Convert the following code into lambda code
"""def even_odd_num(num):
    if(num % 2 == 0):
        print("Even")
    else:
        print("Odd")


even_odd_num(5)"""

even_odd_num = lambda num:"Even" if num % 2 == 0 else "Odd"
print(even_odd_num(10))
print(even_odd_num(7))