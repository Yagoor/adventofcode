import math

with open('input', 'r') as fp:
    data = fp.read()

directions, nodes = data.split("\n\n")

start_points = []
desert_map = {}
for step in nodes.split("\n"):
    node, leafs = step.split("=")
    left, right = leafs.split(",")
    desert_map[node.strip()] = (left.strip()[1:], right.strip()[:-1])
    if node.strip().endswith("A"):
        start_points.append(node.strip())

current_pos = desert_map["AAA"]
sum = 0
while True:
    for direction in directions:
        if direction == 'R':
            step = current_pos[1]
        elif direction == 'L':
            step = current_pos[0]

        current_pos = desert_map[step]
        sum += 1
        if step == "ZZZ":            
            break
    if step == "ZZZ":
        break

print("Sum 1", sum)

current_pos = []
for start_point in start_points:
    current_pos.append(desert_map[start_point])

distances = []
for start_point in start_points:
    current_pos = desert_map[start_point]
    count = 0
    while True:
        for direction in directions:
            if direction == 'R':
                step = current_pos[1]
            elif direction == 'L':
                step = current_pos[0]

            current_pos = desert_map[step]
            count += 1
            if step.endswith("Z"):
                break
        if step.endswith("Z"):
            break
    distances.append(count)

print("Sum 2", math.lcm(*distances))