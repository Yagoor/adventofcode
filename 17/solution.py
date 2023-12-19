import heapq

def dijkstra(puzzle, start, end, min, most):
    queue = [(0, start, 0,0)]
    seen = set()
    while queue:
        cost, pos, direction_x, direction_y = heapq.heappop(queue)
        if pos == end: return cost
        if (pos, direction_x, direction_y) in seen: continue
        seen.add((pos, direction_x, direction_y))

        for dx,dy in {(1,0),(0,1),(-1,0),(0,-1)}-{(direction_x, direction_y),(-direction_x, -direction_y)}:
            a,b = pos
            c = cost

            for _ in range(min, most+1):
                a, b = a+dx, b+dy 
                if (a,b) in puzzle:
                    c += puzzle[(a,b)]
                    heapq.heappush(queue, (c, (a,b), dx,dy))

with open('input', 'r') as fp:
    data = fp.read()

data = list(map(list, data.split("\n")))

puzzle = {}
for y, row in enumerate(data):
    for x, column in enumerate(row):
        puzzle[(x,y)] = int(column)

print(dijkstra(puzzle, (0,0),max(puzzle), 1, 3))
print(dijkstra(puzzle, (0,0),max(puzzle), 4, 10))
