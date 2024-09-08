# Method overloading
# Python doesn't support overloading

class MathUtil(object):  # The object class is the base class of hierarchy
    def add(self, a, b, c=10):
        return a + b + c

    def add(self, a, b, c=15, d=25):
        return a + b + c + d


math = MathUtil()
print(math.add(10, 20))
