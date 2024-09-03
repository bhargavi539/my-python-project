#Decorator - is a way to modify the behaviour of a function or class without changing its code
#Understanding the decorators in Python

def add_decorator(func):
    def wrapper():
        print("1.Before the function is called")
        print("2.Add Helmet, DashCam, Gloves, Knee Guard")
        func()
        print("3.After the function is called")
        print("Secure Driving\n")

    return wrapper()


@add_decorator
def drive_bike():
    print("I am driving")

@add_decorator
def drive_bicycle():
    print("I am driving bicycle")
