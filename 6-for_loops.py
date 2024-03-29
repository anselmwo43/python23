# iterable and non-iterable objects (limited loop)

    # int, float - non-iterable
    # string, list, tuple, range - iterable

# interval notation [()]
    # when using 'range(someValue)' the lower range is included and the upper range is excluded

# basic stracture
"""
for someVariable in someIterableObject:
    forLooPBody
    ...
    ...
    ...
    ...
"""
string = "Yared"
# [Y, a, r, e, d]
list_var = [1, 2, 3, 5]
integer = 1
users = [1, 2, ["Sinidu", "Helina"]]

for i in string:
    print(i+"1")

# for i in integer:
#     print(i)
    
for i in list_var[:2]:
    print(list_var[-i])

# users = [1, 2, ["Sinidu", "Helina"]]
admins = [["Yared", "100", "1.9"], ["Sinidu", "1", "1"], ["Helina", ".5", "3"],]
admins = [{"name": "Yared", "age": 11}, {"name": "Sinidu", "age": 100}, {"name": "Helina", "age": 100},]

for user in users:
    print(user)

for admin in admins:
    print(admin["name"])

# using range
for i in range(10):
    print(i)
print("\n")

for i in range(1, 10):
    print(i)
print("\n")

    # step in a range
for i in range(100000, 10000, -2000):
    print(f"{i:,}")