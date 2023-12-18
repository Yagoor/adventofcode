def area_by_shoelace(x, y):
	return abs(sum(x[i-1]*y[i]-x[i]*y[i-1] for i in range(len(x)))) // 2

with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

pos = (0, 0)
cycle = []
points = 0
for row in data:
    direction, length, color = row.split()
    y, x = pos
    if direction == "R":
        x += int(length)
    elif direction == "L":
        x -= int(length)
    elif direction == "U":
        y -= int(length)
    elif direction == "D":
        y += int(length)
    
    points += int(length)
    cycle.append((x,y))
    pos = (y, x)

x, y = zip(*cycle)

area = area_by_shoelace(x, y)

result = (area + 1 + (points // 2))
print("Sum 1", result)

pos = (0, 0)
cycle = []
points = 0
for row in data:
    _, _, color = row.split()
    direction = color[7:8]
    length = color[2:7]
    y, x = pos
    if direction == "0":
        x += int(length, 16)
    elif direction == "2":
        x -= int(length, 16)
    elif direction == "3":
        y -= int(length, 16)
    elif direction == "1":
        y += int(length, 16)
    
    points += int(length, 16)
    cycle.append((x,y))
    pos = (y, x)

x, y = zip(*cycle)

area = area_by_shoelace(x, y)

result = (area + 1 + (points // 2))
print("Sum 2", result)
