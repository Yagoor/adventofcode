def area_by_shoelace(x, y):
	return abs(sum(x[i-1]*y[i]-x[i]*y[i-1] for i in range(len(x)))) // 2

with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

puzzle = { 0: [0] }
pos = (0, 0)
cycle = []
for row in data:
    direction, length, color = row.split()
    y, x = pos
    for i in range(int(length)):
        if direction == "R":
            x += 1
        elif direction == "L":
            x -= 1
        elif direction == "U":
            y -= 1
        elif direction == "D":
            y += 1
        if y not in puzzle:
            puzzle[y] = []

        puzzle[y].append(x)
        cycle.append((x,y))

    pos = (y, x)

x, y = zip(*cycle)

area = area_by_shoelace(x, y)
points = len(cycle)

result = (area + 1 + (points // 2))
print("Sum 1", result)