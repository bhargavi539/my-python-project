# Polymorphism
# Method overriding - says that child or subclass can have same method name as the parent or super class
# When the method is called the local method has the highest preference
class Shape:
    def area(self):
        print("print the Area of the shape")


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3,4)
print(shape1.area())

shape2 = Circle(5.5)
print(shape2.area())

