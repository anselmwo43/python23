import math
# what's a funciton
    # a block of code that only runs when called that accomplishes
    # a specific purpose


# function definition
def walk():
    print("walking")

def greetUsers(user):
    print(f"hello, {user}")

# function calling
greetUsers("Yared")

# arguments and parameters
def greet_special_users(username, email, /, *, age, height):
    print(f"Hello, {username} {email}")

greet_special_users("yared", "yared@gmail.com", height=2, age=25)

# default parameter value
def circle_area_calc(rad=5):
    PI = 2
    area = PI * rad**2
    print(area)

circle_area_calc(10)

# multiple arguments


# positional and keyword arguments


# positional and keyword argument restriction (/, *)
def greet_special_users(username, email, /):
    print(f"Hello, {username} {email}")

greet_special_users("yared", "yared@gmail.com")


# arbirtrary arguments (*args) and arbitrary keyword arguments(**kwargs)
def email_assignment(*user, **username) -> None:
    print(user[1])
    print(username["name"])

email_assignment("yared", "Sinidu", "Helina", name="yared", age=20)

# scope
def add_numbers(*args):
    summation = 0
    for num in args:
        summation += num

add_numbers(1, 2, 3)
# print(summation)

# return statements
def add_numbers(*args):
    summation = 0
    for num in args:
        summation += num

    return summation

print(add_numbers(1, 2) + 4)

var:int = 10

def multiply_ints(*args) -> int:
    mul = 1
    for num in args:
        mul *= num
    
    return mul

# recursion
def recurring_adder(num) -> int:
    if num > 0:
        summation = num + recurring_adder(num - 1)
    else:
        return 0
    # summation = 3 + (2 + (1 + 0))
    return summation

print(recurring_adder(3))