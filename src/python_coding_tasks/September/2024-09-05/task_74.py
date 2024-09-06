# Hierarchical Inheritance

class Father:
    def BHK1(self):
        print("1BHK")


class Son(Father):
    def BHK2(self):
        print("2BHK")


class Daughter(Father):
    def BHK3(self):
        print("3BHK")


class Baby(Father):
    def no_house(self):
        print("NO house")


son = Son()
son.BHK1()
son.BHK2()

daughter = Daughter()
daughter.BHK1()
daughter.BHK3()
# daughter.BHK2()? This belong to Son
