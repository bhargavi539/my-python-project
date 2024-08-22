#Continue statement
"""
Continue statement is used inside the loop
to skip the rest of the code inside the loop for the current iteration
and proceed to continue to the next iteration
"""

for variable in range(2, 10):
    if variable % 4 == 0:
        continue
    else:
        print(variable)
