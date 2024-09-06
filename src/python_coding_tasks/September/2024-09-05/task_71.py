# Multiple Inheritance

class Father:
    __password = "abc123"

    def father_money(self):
        return 5

    def home(self):
        print("This is Father's home")

    def __show_password(self):
        print("This is a private method from Father class ", self.__password)

    def _show_everything(self):
        self.__show_password()


class Mother:

    def mother_money(self):
        return 7

    def home(self):
        print("This is Mother's home")


class Child(Father, Mother):
    pass


child_obj = Child()
print(child_obj.mother_money())
print(child_obj.father_money())
child_obj.home()


class Child2(Mother, Father):
    pass


child2_obj = Child2()
child2_obj.home()

child1 = Child()
child1._show_everything()
