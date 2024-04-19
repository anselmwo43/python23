# basic structure
    # unordered, unindexed, immutable*, duplicate items not allowed
sett = {"string", True, 10, 1.0, 10}
# {1, 2, 3, 4, 5, 6, 7, 8}
print(sett)
print(hash("a"))
# index = hash(item) % set_length
# set constructor
sett = set((1, 2, 3, 16, 7, 8, 11, 4, 5, 10))
print(sett)

lst = list(sett)
print(lst)
lst[0] = 100
print(lst)
sett = set(lst)
print(sett)

# set methods
    # add
new_set = {"a", "b", "c", True}
new_set.add(1)
print(new_set)

    # update
new_set.update(sett)
print(new_set)
        # different datatypes
lst = ["1", "2"]
new_set.update(lst)
print(new_set)
    # remove
new_set.remove("1")
print(new_set)
# new_set.remove("o")
    # discard
new_set.discard("o")
lst = [1,2,3]
lst.pop()
print(lst)
    # pop
new_set.pop()
print(new_set)
    # clear
set1 = {1, 2, 3, 4, False}
set2 = {5, 6, 7, 8, True, 0}
lst = ["a", "b", "c"]
for i in set1:
    print(i)
for j in zip(set1, set2):
    print(j)

# joining sets
    # union (|)
set3 = set1.union(set2)
print(set3)
set3 = set3.union(lst, set2)
print(set3)
# | is only applicable for sets
set4 = set1 | set2 | set3
print(set4)
    # intersection (&)
set5 = set1.intersection(set2)
print(set5)
set5 = set1 & set2
    # intersection_update
set1.intersection_update(set2)
print(set1)
    # difference (-)
set6 = set2.difference(lst)
print(set6)
set7 = set2 - set1
print(set7)
    # difference_update
set2.difference_update(lst)
print(set2)
    # symmetric difference (^)
set1 = {1, 2, 3, 4, False}
set2 = {5, 6, 7, 8, True, 0}
set8 = set1.symmetric_difference(set2)
print(set8)
    # symmetric difference_update
set1.symmetric_difference_update(set2)
print(set1)

for x in range(len(set1)):
    print(x+1)