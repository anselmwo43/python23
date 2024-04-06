# basic structure (unlimited loop)
"""
while condition:
    ...
    ...
    ...
    ...

"""
# using static stracture
"""
while True:
    print("hello")

"""

# accepting input in a loop
username = ""
while not username:
    username = input("What's your name? ")
    # is the input function blocking?
"""
print("hello")
input("What's your name?")
print("Bye")
"""

# Yared
# Yare
# Yar
# Ya
# Y
name = "Yared"
i = len(name)

while name:
    name = name[:i]
    print(name)
    i -= 1 # i = i - 1 
    # i += 6 > i = i + 6
