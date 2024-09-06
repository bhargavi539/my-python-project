# Inheritance

class Father:
    key = "2BHK"

    def car(self):
        print("Father car!!", self.key)


class Son(Father):
    key2 = "3BHK"

    def home(self):
        print(self.key2, self.key)


son_obj = Son()
son_obj.car()
son_obj.home()

father_obj = Father()
# father_obj.home() -> cannot access son's attributes or behaviours
