
# declaration and naming of variables

    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords.


hello = "hello world"

print(hello, end=" ")
print(hello)

# datatypes

num = 3 # int

hello = num # reassigning a variable and passing a value of an int

print(hello) # an integer gets printed

num = 3.3 # floating point number

y = False # boolean

x = not True

print(not x, y)

# string methods

hello = "hello world"

    # len
print(len(hello))

    # count
print(hello.count("l"))

    # find
print(hello.find(" "))

    # capitalize
print(hello.capitalize())

    # upper
print(hello.upper())

# The content of "hello" is not affected by the above print statements since we are NOT
# assigning the modified versions of "hello" to the variable "hello"

hello = hello.capitalize() # alters (changes the content of "hello" permanently)
print(hello)

    # lower
print(hello.lower())

    # isdigit
number = "100"
print(hello.isdigit())
print(number.isdigit())

    # isalpha
print(hello.isalpha())

    # replace
print(hello.replace(" ", "")) 

hello = hello.replace(" ", "")
print(hello.isalpha())

# escape sequence

print("\thello\\world\\")

# string concatination

firstInt = "2"
secondInt = "3"

thirdInt = firstInt + secondInt

print(thirdInt)

# * string operator

print(firstInt*3)

# format

userName = "Yared"
lastName = "Fekade"

print("Hello {} Welcome to your dashboard\nYour lastname is {}".format(userName, lastName))

# f-string

print(f"Hello {userName}")

# multiple assignment

y = x = b = "hello world"

print(x, y, b.capitalize())

# type casting

x, y, z = 3, 6.6, "9"

print(str(x) + str(y)) # concatinates "x" and "y" as their types have been changed into string
print(x + int(z) + float(z))
print(x, y, z*2 + z)
