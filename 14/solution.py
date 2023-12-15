import numpy as np

with open('input', 'r') as fp:
    data = fp.read()

data = list(map(list, data.split("\n")))

for y, row in enumerate(data):
    if y == 0:
        continue
    for x, column in enumerate(row):
        if data[y][x] != "O":
            continue
        for i in range(1, y + 1):
            if data[y - i][x] in ("#", "O"):
                break
            data[y - i][x] = data[y - i + 1][x]
            data[y - i + 1][x] = "."

total = 0
for y, row in enumerate(data):
    count = sum(column == "O" for column in row)
    total += (count * (len(data) - y))

print("Sum 1", total)

with open('input', 'r') as fp:
    data = fp.read()

data = list(map(list, data.split("\n")))

history = {}
i = 0
while i < 1000000000:
    i += 1
    for j in range(4):
        for y, row in enumerate(data):
            if y == 0:
                continue
            for x, column in enumerate(row):
                if data[y][x] != "O":
                    continue
                for k in range(1, y + 1):
                    if data[y - k][x] in ("#", "O"):
                        break
                    data[y - k][x] = data[y - k + 1][x]
                    data[y - k + 1][x] = "."

        m = np.array(data, str)
        m_90 = np.rot90(m, 3)
        data = m_90.tolist()

    key = tuple(tuple(row) for row in data)
    if key in history:
        jump_length = i - history[key]
        jumps = (1000000000 - i) // jump_length
        i += jumps * jump_length
    history[key] = i
    

total = 0
for y, row in enumerate(data):
    count = sum(column == "O" for column in row)
    total += (count * (len(data) - y))


print("Sum 2", total)