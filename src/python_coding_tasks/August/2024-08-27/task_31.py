def outer_function():
    var1 =22

    def inner_function():
        print("inner_function",var1)

    def inner_function2():
        print("inner_function2",var1)

    inner_function()
    inner_function2()

outer_function()