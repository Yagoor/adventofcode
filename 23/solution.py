def generate_graph(cardinal_points, data, slopes):
    graph = {pt: {} for pt in cardinal_points}

    for sx, sy in cardinal_points:
        stack = [(0, sx, sy)]
        seen = {(sx, sy)}

        while stack:
            n, x, y = stack.pop()
            if n != 0 and (x, y) in cardinal_points:
                graph[(sx, sy)][(x, y)] = n
                continue

            if slopes and data[y][x] in ("^", ">", "v", "<"):
                if data[y][x] == "^":
                    directions = {(0,-1)}
                elif data[y][x] == ">":
                    directions = {(1,0)}
                elif data[y][x] == "v":
                    directions = {(0,1)}
                elif data[y][x] == "<":
                    directions = {(-1,0)}
            else:
                directions = {(0,-1),(1,0),(0,1),(-1,0)}

            for dx,dy in directions:
                a, b = x + dx, y + dy
                if 0 <= b < len(data) and 0 <= a < len(data[0]) and data[b][a] != "#" and (a,b) not in seen: 
                    stack.append((n + 1, a, b))
                    seen.add((a, b))

    return graph

def dfs(graph, seen, point, end_pos):
    if point == end_pos:
        return 0

    m = -float("inf")

    seen.add(point)
    for nx in graph[point]:
        if nx not in seen:
            m = max(m, dfs(graph, seen, nx, end_pos) + graph[point][nx])
    seen.remove(point)

    return m

with open('input', 'r') as fp:
    data = fp.read()

data = list(map(list, data.split("\n")))

cardinal_points = set()
start_pos = end_pos = None
for y, row in enumerate(data):
    for x, column in enumerate(row):
        if column == "#":
            continue
        if y == 0:
            start_pos = (x, y)
        elif y == len(data) - 1:
            end_pos = (x, y)

        neighbors = 0
        for dx,dy in {(0,-1),(1,0),(0,1),(-1,0)}:
            a, b = x + dx, y + dy
            if 0 <= b < len(data) and 0 <= a < len(data[0]) and data[b][a] != "#":
                neighbors += 1
        if neighbors >= 3:
            cardinal_points.add((x, y))

cardinal_points.add(start_pos)
cardinal_points.add(end_pos)

graph = generate_graph(cardinal_points, data, True)
print("Sum 1", dfs(graph, set(), start_pos, end_pos))
graph = generate_graph(cardinal_points, data, False)
print("Sum 2", dfs(graph, set(), start_pos, end_pos))
