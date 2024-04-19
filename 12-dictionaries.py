# Basic structure
    # ordered, mutable(changable), do not allow duplicates
# word(key): definition(value)
new_dict = {
    "string": "String value",
    1: 10,
    7: 10,
    "String": "another value",
}
print(new_dict)

var = "7"
# accessing items in a new_dictionary
print(new_dict["string"])
print(new_dict.get("hello"))
print(new_dict.get(var))

# updating an item
new_dict["string"] = "hello world"
print(new_dict)

# creating a new item
new_dict["hello"] = var
print(new_dict)

# dict constructor
user = dict(name = "yared", age = 100, height = 1.1)
print(user)

# dict methods
  # pop
user.pop("height")
print(user)
  # popitem
user.popitem()
print(user)

  # update
user.update({"fullname": "Yared Fekade", "weight": 200})
print(user)

# looping through dictionary
user = dict(name = "yared", age = 100, height = 1.1)
for item in user:
    print(item)

# nested dictionary
nested_dict = {
    "first_item": {
        "name": "First",
        "age": 20
    },
    "second_item": {
        "name": "Second",
        "age": 20
    },
    "third_item": {
        "name": "Third",
        "age": 30
    },
}
print(nested_dict["third_item"]["age"])

first_item = {
    "name": "first",
    "age": 12
}
second_item = {
    "name": "second",
    "age": 12
}
third_item = {
    "name": "third",
    "age": 12
}

nested = {
    "first_item": first_item,
    "second_item": second_item,
    "first_item": third_item,
}

print((nested))

# iterating through a dict
for item in third_item:
    print(item)

    # dict items
print(third_item.items())

    # dict keys
print(third_item.keys())

    # dict values
print(third_item.values())

for key, value in third_item.items():
    print(key, value)

for key, value in zip(third_item.keys(), third_item.values()):
    print(key, value)