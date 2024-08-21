""" Task #8
✅ Triangle Classifer:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle."""

length1 = int(input("Enter length of side 1 "))
length2 = int(input("Enter length of side 2 "))
length3 = int(input("Enter length of side 3 "))

if length1 == length2 == length3:
    print("It is an equilateral triangle ")
elif length1 == length2 or length1 == length3 or length2 == length3:
    print("It is an isosceles triangle")
else:
    print("It is a scalene triangle")