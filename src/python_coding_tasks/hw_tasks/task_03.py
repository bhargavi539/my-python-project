"""
### Task #3
- Explain the difference between the = operator and the == operator in Python.
"""
# = operator is used to assign value to a variable
# whereas == operator is used to compare two values or variables, and it returns boolean values True or False

first_name = "Alvira"
print(first_name) # Now the string "Alvira" prints on the console

user_name = "Alvira"
print(first_name==user_name) # -> The value of first_name and user_name are compared and
# returns a boolean value True if the condition is true, else False



#- What does the ** operator do in Python, and how is it used?

# ** operator is used to raise a number to the power of another number. It is used for exponentiation
base_number = float(input("Enter base number\n"))
exponent = float(input("Enter exponent\n"))
print(f"{base_number} raised to the power of {exponent} is ",f"{base_number ** exponent:.2f}")

#- What does the ^ operator do in Python, and in what context is it commonly used?
# ^ operator or XOR (exclusive OR) operator is used to compare the corresponding bits of two integer numbers
#It returns 1 if the bits are different i.e if one is 0 and one is 1
#It returns 0 if both the bits are same i.e both are 0 or both are 1

num1 = int(input("Enter number1\t"))
num2 = int(input("Enter number2\t"))
print(f"The result is { num1 ^ num2}")




