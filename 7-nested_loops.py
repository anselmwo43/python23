import random
# basic structure
"""
for i in range(10):
    for j in range(i):
        ...
    for k in range(10):
        ...
    other code
"""

# using while loop
x, j = 6, 9
while x > 1:
    while j > 4:
        print(j, end="")
        j -= 1
        if j==4:
            print()
    print(x, end="")
    x -= 1

# using for loop
print()
l, m = 6, 9
# for i in range(l, 1, -1):
#     for j in range(m, 4, -1):
#         print(j, end="")
#         if j == 5:
#             print()
#     print(i, end="")

# real-world example
# Senario: We have three shopping bags and we would
# like to fill each one with various grocery items

bags = ["black bag", "red bag", "white bag"]
items = ["bananas", "oranges", "potatoes", "chicken"]
cart = {}

# cart = {"black bag": [], "red bag": [...], "white bag": [], }
for bag in bags:
    rand = random.randint(1,5)
    for i in range(rand):
        cart[bag] = items[:i]
    # cart[bag] = items
    # cart[bag] = [item for item in items]
    # bag_items = cart.get(bag, [])
    # for item in items:
    #     bag_items.append(item)
    # cart[bag] = bag_items
        

print(f"{cart = }")

# Please refer to the section named "second method" in the mini-project entitled "dimond_shape"
# for a project done using nested loops