# An example of how to use Classes and Objects in web automation

class VWOLoginPage:

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def login_check(self):
        if self.email == "abc@gmail.com" and self.password == "Pass123":
            print("Login is successful")
        else:
            print("Login failed")


email = input("Enter your email: ")
password = input("Enter your password: ")
vwo_obj = VWOLoginPage(email,password)
vwo_obj.login_check()