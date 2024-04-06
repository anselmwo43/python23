
rows = int(input("Insert the number of rows "))

# first method
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("_" * (2 * i + 1))

for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1), end="")
    print("_" * (2 * i + 1))


# second method
for i in range(rows):
    for j in range(rows - i -1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()

for i in range(rows):
    for j in range(i + 1):
        print(" ", end="")
    for k in range(rows - i - 1):
        print("* ", end="")
    print()