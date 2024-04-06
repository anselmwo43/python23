import math
"""
while condition:
    loop body
    ...
"""
name = ""
while not name:
    name = input("Choose a shape to calculate\nthe area of: \n(c for circle, r for rectangle, t for triangle): ")

if name.lower() == "r" or name.lower() == 'rectangle':
    length = float(input(f"enter the lenghth? (in cm) "))
    width = float(input(f"enter the width? (in cm) "))
    length = (length) / 100
    width = (width) / 100
    area = round(length * width, 2)
    print("the area of this rectangle is", str(area) + "m^2")
elif name.lower() == "t" or name.lower() == "triangle":
    base = float(input("enter the base of the triangle? (in cm) "))
    height = float(input("enter the height of the triangle? (in cm) "))
    base = (base) / 100
    height = (height) / 100
    area = base * height / 2
    print("the area of this triangle is", str(area) + "m^2")
elif name.lower() == "c" or name.lower() == "circle":
    radius = float(input("enter the radius of the circle? "))
    PI = math.pi
    radius1 = pow(radius, 2)
    area = PI * radius1
    print("the area of this circle is", str(area) + "m^2")
else:
    print("Wrong input!")