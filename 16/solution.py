import sys  

limit = sys.getrecursionlimit() 
sys.setrecursionlimit(limit * 5)  

with open('input', 'r') as fp:
    data = fp.read()

data = list(map(list, data.split("\n")))

def energize(y, x, data, direction, visited):
    if y < 0 or x < 0 or y >= len(data) or x >= len(data[y]) or ((y,x) in visited and direction in visited[(y,x)]):
        return
    if (y,x) in visited:
        visited[(y,x)].append(direction)
    else:
        visited[(y,x)] = [direction]
    next_directions = []
    if data[y][x] == ".":
        data[y][x] = direction
        next_directions.append(direction)
    elif data[y][x] == "|":
        if direction == ">" or direction == "<":
            next_directions.append("^")
            next_directions.append("v")
        else:
            next_directions.append(direction)            
    elif data[y][x] == "-":
        if direction == "v" or direction == "^":
            next_directions.append(">")
            next_directions.append("<")
            next_directions.append(">")
            next_directions.append("<")
        else:
            next_directions.append(direction)
    elif data[y][x] == "/":
        if direction == ">":
            next_directions.append("^")
        elif direction == "<":
            next_directions.append("v")
        elif direction == "v":
            next_directions.append("<")
        elif direction == "^":
            next_directions.append(">")
    elif data[y][x] == "\\":
        if direction == ">":
            next_directions.append("v")
        elif direction == "<":
            next_directions.append("^")
        elif direction == "v":
            next_directions.append(">")
        elif direction == "^":
            next_directions.append("<")
    else:
        next_directions.append(direction)

    for next_direction in next_directions:
        if next_direction == ">":
            energize(y, x + 1, data, next_direction, visited)
        elif next_direction == "^":
            energize(y - 1, x, data, next_direction, visited)
        elif next_direction == "v":
            energize(y + 1, x, data, next_direction, visited)
        elif next_direction == "<":
            energize(y, x - 1, data, next_direction, visited)

def run(y, x, data, direction):
    visited = {}

    energize(y, x, data, direction, visited)

    for y, row in enumerate(data):
        for x, column in enumerate(row):
            if (y,x) in visited:
                data[y][x] = "#"
            else:
                data[y][x] = "."

    # for row in data:
    #     print("".join(row))

    return len(visited.keys())

ret = run(0, 0, [row[:] for row in data], ">")
print("Sum 1", ret)

vals = []
for y in range(len(data)):
    ret = run(y, 0, [row[:] for row in data], ">")
    vals.append(ret)

for y in range(len(data)):
    ret = run(y, len(data[0]) - 1, [row[:] for row in data], "<")
    vals.append(ret)

for x in range(len(data[0]) - 1):
    ret = run(0, x, [row[:] for row in data], "v")
    vals.append(ret)

for x in range(len(data[0]) - 1):
    ret = run(len(data) - 1, x, [row[:] for row in data], "^")
    vals.append(ret)

print("Sum 2", max(vals))    