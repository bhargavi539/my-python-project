#Execution of UI Testing

print(1)


def before_after_ui(func):
    print("Statement outside the wrapper\n")

    def wrapper():

        print("1.Before running the UI Testcases")
        print("2.Start the browser")
        func()
        print("3.After Executing the UI Testcases")
        print("4.Close the browser\n")

    return wrapper


print(2)


@before_after_ui
def run_ui_tc():
    print("executing the UI Testcases")


run_ui_tc()
print(3)
