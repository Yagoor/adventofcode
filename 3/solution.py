class Point:
    x = 0
    y = 0
    value = 0

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def is_adjacent(self, possible_adjacent):
        adjacent = False
        for i in range(len(possible_adjacent.value)):
            if point.x - 1 == possible_adjacent.x + i and point.y == possible_adjacent.y:
                adjacent = True
            elif point.x - 1 == possible_adjacent.x + i and point.y - 1 == possible_adjacent.y:
                adjacent = True
            elif point.x - 1 == possible_adjacent.x + i and point.y + 1 == possible_adjacent.y:
                adjacent = True

            for j in range(len(point.value)):
                if point.x + j == possible_adjacent.x + i and point.y - 1 == possible_adjacent.y:
                    adjacent = True
                elif point.x + j == possible_adjacent.x + i and point.y + 1 == possible_adjacent.y:
                    adjacent = True

            if point.x + len(point.value) == possible_adjacent.x + i and point.y == possible_adjacent.y:
                adjacent = True
            elif point.x + len(point.value) == possible_adjacent.x + i and point.y - 1 == possible_adjacent.y:
                adjacent = True
            elif point.x + len(point.value) == possible_adjacent.x + i and point.y + 1 == possible_adjacent.y:
                adjacent = True

        return adjacent


with open('input', 'r') as fp:
    data = fp.readlines()

points = []
for y in range(len(data)):
    line = data[y]
    line = line.strip()
    accumulator = ""
    initial_x = None
    for x in range(len(line)):
        char = line[x]
        if char == ".":
            if accumulator != "":
                points.append(Point(initial_x, y, accumulator))
                accumulator = ""
                initial_x = None
            continue

        if not char.isnumeric() and accumulator.isnumeric():
            # .990#.
            points.append(Point(initial_x, y, accumulator))
            accumulator = ""
            initial_x = None
        elif char.isnumeric() and not accumulator.isnumeric() and accumulator != "":
            # .#990.
            points.append(Point(initial_x, y, accumulator))
            accumulator = ""
            initial_x = None

        if initial_x is None:
            initial_x = x
        accumulator += char

    if accumulator != "":
        points.append(Point(initial_x, y, accumulator))
        accumulator = ""
        initial_x = None

sum = 0
for point in points:
    for possible_adjacent in points:
        if possible_adjacent.value.isnumeric():
            # Skip numbers
            continue

        if point.x == possible_adjacent.x and point.y == possible_adjacent.y:
            # Skip myself
            continue

        adjacent = point.is_adjacent(possible_adjacent)     

        if adjacent:
            sum += int(point.value)

print("Sum 1", sum)

multiply_adjacents = {}
for point in points:
    if point.value != "*":
        # Skip not *
        continue

    multiply_adjacents[point] = []
    for possible_adjacent in points:
        if point.x == possible_adjacent.x and point.y == possible_adjacent.y:
            # Skip myself
            continue

        adjacent = point.is_adjacent(possible_adjacent)

        if adjacent:
            multiply_adjacents[point].append(possible_adjacent)

sum = 0
for key in multiply_adjacents:
    value = multiply_adjacents[key]
    print(key.x, key.y, key.value)

    if len(multiply_adjacents[key]) == 2:
        sum += int(multiply_adjacents[key][0].value) * int(multiply_adjacents[key][1].value)

print("Sum 2", sum)
