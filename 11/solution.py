

# Python code for the above approach
import math as Math
from itertools import combinations

# Code to calculate Manhattan distance
def manhattan_distance(X1, Y1, X2, Y2, extra_x, extra_y):
    dist = (Math.fabs(X2 - X1) + extra_x) + (Math.fabs(Y2 - Y1) + extra_y)
    return dist

with open('input', 'r') as fp:
    data = fp.read()

map = data.split("\n")

new_rows = []
for y, row in enumerate(map):
    if row.find("#") == -1:
        new_rows.append(y)

# for y, row in reversed(new_rows):
#         map.insert(y, row)

new_columns = []
for x, column in enumerate(zip(*map)):
    present = False
    for element in column:
        if element == "#":
            present = True
            break        
    if present == False:
        new_columns.append(x)

# for x, column in reversed(new_columns):
#     for map_y, map_row in enumerate(map):
#         for i in range(1000000):
#             new_row = list(map_row)
#             new_row.insert(x, ".")
#             map[map_y] = ''.join(new_row)

galaxies = []

for y, row in enumerate(map):
    for x, column in enumerate(row):
        if column == "#":
            galaxies.append((y, x))

comb = combinations(galaxies, 2)
count_1 = count_2 = 0
for i in comb:
    x1 = i[0][1]
    y1 = i[0][0]
    x2 = i[1][1]
    y2 = i[1][0]
    extra_x = 0
    for column in new_columns:
        if x1 <= column <= x2 or x2 <= column <= x1:
            extra_x += 1

    extra_y = 0
    for row in new_rows:
        if y1 <= row <= y2 or y2 <= row <= y1:
            extra_y += 1

    count_1 += manhattan_distance(x1, y1, x2, y2, extra_x, extra_y)
    count_2 += manhattan_distance(x1, y1, x2, y2, extra_x * (1000000 - 1), extra_y * (1000000 - 1))


print("Sum 1", count_1)
print("Sum 2", count_2)
