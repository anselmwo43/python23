import math
vector1 = [1, 3, 5]
vector2 = [2, 4, 6]
summ = 0
for i, j in zip(vector1, vector2):
    # [[1,2], [3,4], [5,6]]
    summ += pow(i - j, 2)
distance = math.sqrt(summ)

print(pow(distance,2))