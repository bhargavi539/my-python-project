import time


def time_decorator(func):

    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Time taken by the function",end_time-start_time)
    return wrapper()

@time_decorator
def test_ui_1():
    print("Add a function, Time taken by the function")
    time.sleep(5)


@time_decorator
def test_ui_2():
    print("Add a function, Time taken by the function")
    time.sleep(8)