# Cache for dynamic programming
handle_problem_cache = {}
def handle_problem(line, groups_size, group_size):
    if hash(line) + hash(groups_size) + hash(group_size) in handle_problem_cache:
        return handle_problem_cache[hash(line) + hash(groups_size) + hash(group_size)]

    if not line:
        return not groups_size and group_size == 0
    
    solutions = 0

    if line[0] == "?":
        characters = [".", "#"]
    else:
        characters = [line[0]]
    
    for character in characters:
        if character == ".":
            if group_size > 0:
                if groups_size and groups_size[0] == group_size:
                    solutions += handle_problem(line[1:], groups_size[1:], 0)
            else:
                solutions += handle_problem(line[1:], groups_size, 0)            
        else:
            solutions += handle_problem(line[1:], groups_size, group_size + 1)

    handle_problem_cache[hash(line) + hash(groups_size) + hash(group_size)] = solutions
    return solutions


with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

result = 0
for row in data:
    line, groups_size = row.split()
    groups_size = tuple(map(int, groups_size.split(",")))
    # Append "." to close the last group if it is still open
    result += handle_problem(line + ".", groups_size, 0)

print("Sum 1", result)

result = 0
for row in data:
    line, groups_size = row.split()
    groups_size = tuple(map(int, groups_size.split(",")))
    # Append "." to close the last group if it is still open
    result += handle_problem("?".join([line] * 5) + ".", groups_size * 5, 0)

print("Sum 2", result)

