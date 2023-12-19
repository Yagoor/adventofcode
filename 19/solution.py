import re

with open('input', 'r') as fp:
    data = fp.read()

workflows, parts = data.split("\n\n")

workflows = workflows.split("\n")
parts = parts.split("\n")

flows = { }
for workflow in workflows:
    x = re.search("{.*}", workflow)
    rules = x[0][1:-1]
    name = workflow.replace("{" + rules + "}", '')
    parsed_rules = []
    for rule in rules.split(","):
        rule = rule.split(":")
        if len(rule) > 1:
            rule = [rule[0][0], rule[0][1], rule[0][2:], rule[1]]

        parsed_rules.append(rule)

    flows[name] = parsed_rules


count = 0
for part in parts:
    part = part[1:-1]
    ratings = {}
    for value in part.split(","):
        ratings[value[0]] = value[2:]

    
    next_step = "in"
    while True:
        rules = flows[next_step]
        for rule in rules:
            if len(rule) != 1:
                x = int(ratings[rule[0]])
                operation = rule[1]
                y = int(rule[2])
                if operation == "<":
                    if x < y:
                        next_step = rule[3]
                        break
                elif operation == ">":
                    if x > y:
                        next_step = rule[3]
                        break                    
            else:
                next_step = rule[0]
                break
        if next_step in ("A", "R"):
            break
    if next_step == "A":
        for rating in ratings:
            count += int(ratings[rating])

print("Sum 1", count)


count = 0
queue = [[{
    "x": [1, 4000],
    "m": [1, 4000],
    "a": [1, 4000],
    "s": [1, 4000],
}, "in"]]

intervals = []
while queue:
    interval, next_step = queue.pop()
    if next_step == "A":
        intervals.append(interval)
        continue
    if next_step == "R":
        continue
    rules = flows[next_step]
    for rule in rules:
        if len(rule) != 1:
            range = interval[rule[0]]
            operation = rule[1]
            y = int(rule[2])
            if operation == "<":
                if range[1] < y:
                    queue.append([interval, rule[3]])
                    break
                if range[0] < y < range[1]:
                    new_interval = interval.copy()
                    new_interval[rule[0]] = [
                        range[0],
                        y - 1,
                    ]
                    queue.append([new_interval, rule[3]])
                    interval[rule[0]] = [
                        y,
                        range[1],
                    ]
            if operation == ">":
                if range[0] > y:
                    queue.append([interval, rule[3]])
                    break
                if range[0] <= y < range[1]:
                    new_interval = interval.copy()
                    new_interval[rule[0]] = [
                        y + 1,
                        range[1],
                    ]
                    queue.append([new_interval, rule[3]])
                    interval[rule[0]] = [
                        range[0],
                        y,
                    ]             
        else:
            queue.append([interval, rule[0]])

count = 0
for interval in intervals:
    ret = 1
    for range in interval.values():
        ret *= range[1] - range[0] + 1
    count += ret    

print("Sum 2", count)
