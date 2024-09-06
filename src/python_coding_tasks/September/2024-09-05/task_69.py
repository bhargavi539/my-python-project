# Single Inheritance
class Parent:
    gold = "2Kg"

    def bhk2(self):
        print("2BHK")


class Child(Parent):
    diamond = "Diamond"
    def bhk3(self):
        print("3BHK")


child_obj = Child()
print(child_obj.gold)
child_obj.bhk2()
child_obj.bhk3()

parent_obj = Parent()
print(parent_obj.gold)