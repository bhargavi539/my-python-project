global_variable = 10

def func1():
    a=20
    print(a)
    print(global_variable)


func1()


def func2():
    a=100
    global_variable =200
    print(a)
    print(global_variable)


func2()