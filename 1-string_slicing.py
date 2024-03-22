# # string indexing
hello = "hello world"
print(hello[-11])

# slice or index operator []
    # [start:end:step]
print(hello[-2:6:-2])

# reverse a string
print(hello[::-1])

# change order of words
print(hello[6:], hello[:5], end="")

# split method
x, y = hello.split( )[1], hello.split( )[0]
print(x, y)

# slice funciton
slice1 = slice(len(hello), 0, -1)

print(hello[slice1])