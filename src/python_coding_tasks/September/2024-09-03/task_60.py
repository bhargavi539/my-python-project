# Understanding Global variables, Instance variables

a = 10


class Alpha:
    b = 11
    global a # You can modify global variable within the class
    a = "Hello"
    def print_info(self):
        print(f"value of a can be used within the class {a}")
        print(self.b)
        print(a)


obj_ref = Alpha()
obj_ref.print_info()

print(a)
# print(b) --> instant varibale cannot be accessed outside the class without object reference
print(obj_ref.b)
