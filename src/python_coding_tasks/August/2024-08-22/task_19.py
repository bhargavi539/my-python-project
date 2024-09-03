#Match statement is similar to switch statement in Java
"""
Match variable
    case pattern 1:
        #code to execute
    case pattern 2:
        #code to execute
"""
# Write a program to ask the user which browser you want to use to run automation
browser_name = input("Enter the browser name \n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox code")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser not found")
