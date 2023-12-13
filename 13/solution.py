with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n\n")

def is_mirror(list_to_check, depth):
    if len(list_to_check) == 1:
        return None

    mirror = True
    if len(list_to_check) % 2 == 0:
        for start, end in zip(list_to_check, reversed(list_to_check)):
            if start != end:
                mirror = False
                break
    else:
        mirror = False

    if mirror:
        return tuple(list_to_check)

    return is_mirror(list_to_check[1:], depth + 1)

def is_mirror_rev(list_to_check, depth):
    if len(list_to_check) == 1:
        return None

    mirror = True
    if len(list_to_check) % 2 == 0:
        for start, end in zip(list_to_check, reversed(list_to_check)):
            if start != end:
                mirror = False
                break
    else:
        mirror = False

    if mirror:
        return tuple(list_to_check)
       
    return is_mirror_rev(list_to_check[:-1], depth + 1)

evaluate_puzzle_cache = set()
def evaluate_puzzle(puzzle):
    # Vertical Scan
    columns = list(zip(*puzzle))
    result = is_mirror(columns, 0)

    if result and (result, 1) not in evaluate_puzzle_cache:
        evaluate_puzzle_cache.add((result, 1))
        return len(columns) - ((len(result)) // 2)

    result = is_mirror_rev(columns, 0)

    if result and (result, 2) not in evaluate_puzzle_cache:
        evaluate_puzzle_cache.add((result, 2))
        return ((len(result)) // 2)

    # Horizontal Scan
    rows = puzzle
    result = is_mirror(rows, 0)

    if result and (result, 3) not in evaluate_puzzle_cache:
        evaluate_puzzle_cache.add((result, 3))
        return ((len(rows) - ((len(result)) // 2)) * 100)

    result = is_mirror_rev(rows, 0)

    if result and (result, 4) not in evaluate_puzzle_cache:
        evaluate_puzzle_cache.add((result, 4))
        return (((len(result)) // 2) * 100)

    return None

count = 0
for puzzle in data:
    puzzle = puzzle.split("\n")

    count += evaluate_puzzle(puzzle)

print("Sum 1", count)

count = 0
for puzzle in data:
    puzzle = puzzle.split("\n")

    cache = None
    for y, column in enumerate(puzzle):
        for x, row in enumerate(zip(*puzzle)):
            cache = puzzle[y][x]
            if cache == "#":
                puzzle[y] = puzzle[y][:x] + "." + puzzle[y][x + 1:]
            else:
                puzzle[y] = puzzle[y][:x] + "#" + puzzle[y][x + 1:]
            ret = evaluate_puzzle(puzzle)
            puzzle[y] = puzzle[y][:x] + cache + puzzle[y][x + 1:]
            if ret != None:
                break
        if ret != None:
            break

    count += ret
print("Sum 2", count)
