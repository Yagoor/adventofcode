def f(points, n):
    y0 = points[0]
    y1 = points[1]
    y2 = points[2]
    a = (y2+y0-2*y1)/2
    b = y1-y0 -a
    c = y0
    return a*n**2 + b*n +c

with open('input', 'r') as fp:
    data = fp.read()

data = list(map(list, data.split("\n")))

n = len(data)
m = len(data[0])

start_x = start_y = 0
for y, row in enumerate(data):
    for x, column in enumerate(row):
        if column == "S":
            start_x = x
            start_y = y
            break
    if column == "S":
        break

positions = [(start_y, start_x)]
points = {}
for i in range(1, 26501365):
    new_positions = set()
    for position in positions:
        y, x = position
        for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            new_y = y + dy
            new_x = x + dx
            if data[new_y % n][new_x % m] == "#":
                continue
            new_positions.add((new_y, new_x))
            
    if i == 64:
        print("Sum 1", len(new_positions))
    if i % n == 26501365 % n:
        points[i//n] = len(new_positions)
    if len(points) == 3:
        break
    positions = new_positions

print("Sum 2", f(points, 26501365//n))
