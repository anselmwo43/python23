# basic structure
    # ordered, indexed, changeable, allow duplicates
# list = ["item 1", 1, True, 3.4]
lst = [True, 1, 0, "Hello", "Hello"]
lst2 = ["Hello", "Bye", 5, 4]
var = lst[-1]
# length of a list
print(len(lst))

# concatinate lists
lst3 = lst + lst2
print(lst3)

# list constructor
hello = list((4, "hello", 8))

# accessing item at a specific index
print(hello[0])

# mutability at specific index
hello[2] = "Bye"
print(hello)

# change a range of items
hello[0:2] = [5, 4, 10, 5]
print(hello)

# unpacking a list
hello = [1, 2, 3, 4, 5]
x, *y, k, p, m = hello
print(x, y, k, p, m)

# list methods
    # append
hello = [1, 3, 5, "yes"]
hello.append(7)
print(hello)

    # copy
hello2 = hello.copy()
print(hello2)

    # clear
hello.clear()
print(hello)

    # count
print(hello2.count(7))

    # extend
hello.extend(hello2)
print(hello)

    # remove
hello.remove("yes")
print(hello)

    # pop
hello.pop(1)
print(hello)
hello.pop()
print(hello)

    # insert
hello.insert(0, 0.1)
print(hello)
    # sort
hello3 = list((3, 1, 9, 90, 23))
hello3.sort()
print(hello3)
hello3.sort(reverse=True)
print(hello3)

    # reverse
hello3.reverse()
print(hello3)
    # zip
lst_i = [1, 3, 5]
lst_j = [2, 4, 6]
# [[1, 2], [3, 4], [5, 6]]
for i, j in zip(lst_i, lst_j):
    print(i, j)

# list comprehension
    # newlist = [expression for item in iterable]
    # newlist = [expression for item in iterable if condition == True]
Lst = lst_i + lst_j
newList = [x for x in Lst if x % 2 != 0]
print(newList)
# 2D lists
# basic structure
dlist = [[x, x + 1] for x in lst_i]
print(dlist)

# accessing items in a 2D list
print(dlist[2][1])
dlist[0][1] = "Hello"
print(dlist)