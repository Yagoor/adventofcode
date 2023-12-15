def hash(string):
    ret = 0
    for char in string:
        ret += ord(char)
        ret *= 17
        ret %= 256
    return ret

with open('input', 'r') as fp:
    data = fp.read()

total = 0
for step in data.split(","):
    total += hash(step)

print("Sum 1", total)

boxes = {}
for i in range(256):
    boxes[i] = []

for step in data.split(","):
    if "=" in step:
        label, focal_length = step.split("=")
        box = hash(label)
        found = False
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                found = True
                break
        if found:
            boxes[box][i] = (label, focal_length)
        else:
            boxes[box].append((label, focal_length))

    elif "-" in step:
        label, focal_length = step.split("-")
        box = hash(label)
        found = False
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                found = True
                break
        if found:
            boxes[box].pop(i)

total = 0
for box in boxes:
    for pos, len in enumerate(boxes[box]):
        total += (box + 1) * (pos + 1) * int(len[1])
    # total += 
    # print()
print("Sum 2", total)
