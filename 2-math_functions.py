import math
import module

#imports

print(module.user_name)

# math functions
floatNumber = 3.454545
intNumber = 3

    # round
print(round(floatNumber))
print(round(floatNumber, 2))

    # math.ceil
print(math.ceil(floatNumber))

    # math.floor
print(math.floor(floatNumber))

    # abs
print(abs(-30))

    # pow
print(pow(2, 3), 2**3)

    # math.sqrt
print(math.sqrt(8))

    # max
print(max(2,3,4,4,5))

    # min
list_numbers = [0, 2, 3, 4, 4]
print(min(list_numbers))

    # divmod
print(divmod(4, 5)) # form: (dividend, divider) return: (quot, remainder)

x = 9
y = 10

quot = int(x/y)
rem = x%y

print(divmod(x, y), (quot, rem))
