with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

class MapItem:
    def __init__(self, up, right, down, left) -> None:
        self.up = up
        self.right = right
        self.down = down
        self.left = left

map = data
start_y = start_x = 0
for y, row in enumerate(map):
    for x, val in enumerate(row):
        if val == "S":
            start_x = x
            start_y = y

def get_connected_points(map, y, x):
    ret = set()
    # North
    if y - 1  >= 0 and y - 1 < len(map):
        if map[y - 1][x] in ['|', '7', 'F', 'S']:
            ret.add((y - 1, x))
    # South
    if y + 1  >= 0 and y + 1 < len(map):
        if map[y + 1][x] in ['|', 'L', 'J', 'S']:
            ret.add((y + 1, x))
    # West
    if x - 1  >= 0 and x - 1 < len(map[y]):
        if map[y][x - 1] in ['-', 'F', 'L', 'S']:
            ret.add((y, x - 1))
    # East
    if x + 1  >= 0 and x + 1 < len(map[y]):
        if map[y][x + 1] in ['-', '7', 'J', 'S']:
            ret.add((y, x + 1))

    return ret

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

graph = { }
moves = [(start_y, start_x)]
end_points = []
count = 0
while True:
    next_moves = []
    for move in moves:
        if move in graph:
            continue
        connected_points = get_connected_points(map, move[0], move[1])
        # connected_points -= set(graph.keys())
        graph[move] = connected_points
        next_moves += connected_points
        if len(connected_points - set(graph.keys())) == 0:
            end_points.append(move)

    if len(next_moves) == 0:
        break
    else:
        moves = next_moves

paths = [path for path in dfs(graph, (start_y, start_x), (start_y, start_x))]
paths.sort(key=len, reverse=True)

cycle = paths[0]

print("Sum 1", len(cycle) // 2)

counter = 0
for y, row in enumerate(map):
    inside = False
    for x, val in enumerate(row):
        if (y, x) in cycle:
            if val in ("|", "L", "J"):
                inside = not inside
        else:
            counter += inside

print("Sum 2", counter)
