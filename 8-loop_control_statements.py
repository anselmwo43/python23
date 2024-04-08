# break
for i in range(1, 21):
    if i == 10:
        break
    else:
        print(i)
    print(10)

while True:
    name = input("What's your name? ")
    if name != "": break

# continue
for i in range(1, 21):
    if i == 10:
        continue
    else:
        print(i)
    print(10)

# pass
for i in range(1, 21):
    if i == 10:
        pass
    else:
        print(i)
    print(10)
    # print odd numbers

for i in range(21):
    if i % 2 == 0: continue
    else: print(i)