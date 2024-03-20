
# declaration and naming of variables

    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords.

hello = "hello world"

# print(hello, end=" ")
# print(hello)

# datatypes

num = 3

# hello = num

# print(hello)

num = 3.3

y = False

# string methods

    # len
# print(len(hello))
    # count
# print(hello.count("l"))
    # find
# print(hello.find(" "))
    # capitalize
# print(hello.capitalize())
    # upper

# print(hello.upper())
hello = hello.capitalize()
# print(hello)
    # lower
# print(hello.lower())
    # isdigit

number = "100"


# print(hello.isdigit())
    # isalpha
# print(hello.isalpha())
    # replace
# print(hello.replace(" ", ""))
# hello = hello.replace(" ", "")
# print(hello.isalpha())

# escape sequence

# print("\tasdl\\adfas\\")

# string concatination

firstInt = 2
secondInt = "3"

# thirdInt = firstInt + secondInt

# print(thirdInt)

# * string operator

# print(firstInt*3)

# format
userName = "Yared"
lastName = "Fekade"

# print("Hello {} Welcome to your dashboard\nYour lastname is {}".format(userName, lastName))

# f-string
# print(f"Hello {userName}")

# print(f"{y} are we there yet?")

# multiple assignment

y = x = b = "hello world"

# print(x, y, b.capitalize())

# type casting

x, y, z = 3, 6.6, "9"


# print(x+int(z))
# print(x, y, z*2 + z)
