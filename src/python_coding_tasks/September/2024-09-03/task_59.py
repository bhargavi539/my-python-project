# Calculator program
class Calc:

    def __init__(self):
        print("--DC--")

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def multi(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b


obj_ref = Calc()
a = int(input("Enter value1"))
b = int(input("Enter value2"))
sum_output = obj_ref.sum(a,b)
sub_output = obj_ref.sub(a,b)
multi_output = obj_ref.multi(a,b)
div_output = obj_ref.div(a,b)

print(sum_output,sub_output,multi_output,div_output)