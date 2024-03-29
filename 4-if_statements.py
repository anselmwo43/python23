import math
import time

# basic structure
if 1 > 3:
    print("first")
elif 1 > 0:
    print("second")
elif 1 > -1:
    print("third")
else:
    print("else")

# operators
num1 = 3.5
num2 = 3
    # >, >=
if num1 > num2:
    print("The first number is greater")
elif num1 == num2:
    print("The numbers are equal")
else:
    print("The second one is greater")

    # <, <=
if num1 < num2:
    print("The second number is greater")
else:
    print("The first one is greater")

    # ==
# num1 = 3.5, num2 = 3
if math.floor(num1) == num2:
    print("Equal numbers")
else:
    print("The numbers are not equal")


# check a static condition

if not True:
    print("This condition is true")
else:
    print("The above condition is false.")

# check inclusion
    
list_var = [1, 2, ["Sinidu", "Helina"]]
# student_list = [list_var[-2], list_var[-1]]
student_list = list_var[-1]
# list_var = [1, 2, "Sinidu", "Helina", ["Sinidu", "Helina"]]

if student_list in list_var:
    print("Yes, they are in this class")
else:
    print("Kick them out!!!")

# check identity
list_var = student_list
if student_list is list_var:
    print("they are the same object!")
else:
    print("They are different")

# check input condition
username = input("Choose a username, strager: ")

if username == "yared":
    print("EEEEEEEEEEEE!!! username taken!")
else:
    print(f"Your username has been set as '{username}'")

area_cal = input("Choose a shape you would like\nto calculate the area of: ")

if area_cal == 'c' or area_cal == 'C' or area_cal == 'circle':
    print("Calculating the area of your circle...")
    time.sleep(2)
    print("The area of your circle is 36m2")

elif area_cal == 'r' or area_cal == 'R' or area_cal == 'rectangle':
    print("Calculating the area of your rectangle...")
    time.sleep(2)
    print("The area of your rectangle is 36m2")

elif not area_cal and area_cal != 'c':
    print("logical error")

# not area_cal == area_cal = "" ?