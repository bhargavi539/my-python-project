class GrandFather:
    x = 10

    def home(self):
        print("old model home")


class Father(GrandFather):
    a = 55

    def home(self):
        super().home()
        print("1BHK")


class Son(Father):
    b = 22

    def home(self):
        print("3BHK")
        super().home()
        print(super().x)


son_obj = Son()
son_obj.home()
print("Value of X :",son_obj.x)
