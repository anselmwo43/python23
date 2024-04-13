# basic structure
    # ordered, indexed, immutable/unchangable, allows duplicate items
tup = (1, 2.5, True, "Hello")
# tup[0] = "hello" -> not allowed
print(tup)

# one item tuple
a = "String"
a = ("hello",) # needs a comma for a single item tuple
print(type(a))

# the tuple constructor
lst = [2, 4, 5, 8]
lst = tuple(lst)
print(type(lst))

# accessing an item in a tuple
print(lst[0])

# workaround to update tuple items
    # changing tuples into lists and back to tuples again
    # after changes
tpl = (0, 0, 2)
tpl = list(tpl)
tpl.remove(0)
tpl.remove(0)
tpl = tuple(tpl)
print(tpl)

tpl = tuple([i for i in range(1,11)])
tpl = list(tpl)
tpl.reverse()
tpl = tuple(tpl)
print(tpl)

# concatinating tuples
tpl1 = ("hello", )
tpl2 = ("world",)
tpl3 = tpl1 + tpl2
print(tpl3)
tu1=(1,3,5)
tu2=(2,4,6)
tu3=()
for i,j in zip(tu1,tu2):
    tu3 += (i, j)
print(tu3)

# repeatition operator (*) in tuples
tpl2 = ("hello",) * 2
print(tpl2)

# unpacking a tuple
(a, b, *c) = (1, 3, 4, 5)
print(a, b, tuple(c))
