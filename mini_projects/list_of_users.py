import random

# reference of a dict and copy of a dict
new_dict = {
    "name": "hello",
}

second_dict = new_dict.copy()

new_dict["name"] = "bye"

print(second_dict["name"])


user = {
    "name": "Yared",
    "age": 23,
    "username": "yared",
    "email": "jaredyared83@gmail.com"
}

users = []
names = ["Yared", "Sinidu", "Helina", "Abebe", "Kebede"]
status = {}

for name in names:
    activity = ["inactive", "active"]
    index = random.randint(0, 1)
    status[name] = activity[index]

print(status)

"""
[{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
},
{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
},
{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
},
{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
},
{
    "name": "Yared",
    "age": "23",
    "username": "yared",
    "email": "jaredyared83@gmail.com"
}]
"""
# create 5 users with the same information
for i in range(5):
    users.append(user.copy())


# change the names of users
for user, name in zip(users, names):
    user["name"] = name

# change the status of users
for user in users:
    user["status"] = status[user["name"]]

# assign emails corresponding to names
for user in users:
    randint = random.randint(10, 20)
    user["email"] = user["name"] + str(randint) + "@gmail.com"
    
    # username update
    user["username"] = user["name"] + str(randint)


print(users)