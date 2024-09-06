# Multilevel Inheritance
class GrandFather:
    gold = "2KG"

    def bhk1(self):
        print("1BHK")


class Father(GrandFather):
    diamond = "22carat"

    def bhk2(self):
        print("2BHK")


class Son(Father):
    bitcoin = "bitCoin"

    def bhk3(self):
        print("3BHK")


son_obj = Son()
father_obj = Father()
grandfather_obj = GrandFather()

son_obj.bhk2()
son_obj.bhk1()
son_obj.bhk3()

father_obj.bhk2()
father_obj.bhk1()