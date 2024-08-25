"""
#TYPES OF FUCNCTIONS
1.NO return type and No Arguments
2.No return type with arguments
3.No return type with default arguments
4.with return values and with Arguments
"""


# 1.NO return type and No Arguments
def greet():
    print("Hello")


result = greet()
print(result)


# 2.No return type with arguments
def greet_by_name(name):
    print("Hello", name)


greet_by_name("Amir")


# 3.No return type with default arguments
def greet_by_default_name(name="Guest"):
    print("Hello ", name)


greet_by_default_name()
greet_by_default_name("Aman")
greet_by_default_name(name="Ajay")  #positional arguments
