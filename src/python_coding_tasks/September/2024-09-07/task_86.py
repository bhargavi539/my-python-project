# Static Methods
# A static method is a method that belongs to a
# class rather than an instance of the class.

class MathOperation:

    def div(self,a,b):
        return a / b

    def mul(self,a,b):
        return a * b

    @staticmethod
    def sum(a,b):
        return a + b

    @staticmethod
    def sub(a,b):
        return a - b


obj_ref = MathOperation()
print(obj_ref.div(10,5))
print(obj_ref.mul(10,5))

# Static methods can be called direclty without the Object.
print("Static Methods",MathOperation.sum(10,20))
print("Static Methods",MathOperation.sub(100,20))