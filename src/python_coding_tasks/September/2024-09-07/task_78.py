# Method overriding - Same method name in the parent and the child,
# the child always overrides the parent's methods
# super means -> call my parent method
class Father:
    a = 10

    def home(self):
        print("1BHK")


class Son(Father):
    def home(self):
        super().home()
        print("3BHK")
        print(super().a)


son_obj = Son()
son_obj.home()
