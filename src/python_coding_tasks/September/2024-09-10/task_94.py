#  Using exceptions inside the class

class XYZ:
    def f1(self):
        try:
            a = int(input("Enter an integer"))

        except Exception as e:
            print("Please enter only integer ",e)
        else:
            print("The value you entered is: ",a)

        finally:
            print("It is executed always")


x = XYZ()
x.f1()