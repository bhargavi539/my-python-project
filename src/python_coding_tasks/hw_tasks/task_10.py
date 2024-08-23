# Task #10 -
# Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24
number = int(input("Enter a number to find factorial "))
factorial = 1
if number < 0:
    print("Enter a number greater than zero")
else:
    for i in range(1,number+1):
        factorial = i * factorial

print(f"The Factorial of {number} is :",factorial)