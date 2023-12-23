with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

boxes_row = []
for i, row in enumerate(data):
    xyz1, xyz2 = row.split("~")
    x1, y1, z1 = map(int,xyz1.split(","))
    x2, y2, z2 = map(int,xyz2.split(","))
    boxes_row.append([x1, y1, z1, x2, y2, z2])

boxes_row.sort(key=lambda x:x[2])

boxes_positions_dict = {}
positions_with_boxes = set()
for i, box_row in enumerate(boxes_row):
    x1, y1, z1, x2, y2, z2 = box_row
    boxes_positions_dict[i] = set()

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                boxes_positions_dict[i].add((x,y,z))
                positions_with_boxes.add((x,y,z))

# print(positions_with_boxes)
# print(boxes_positions_dict)

def fall(boxes_positions_dict, positions_with_boxes, skip):
    falls = set()
    if skip is not None:
        positions_with_boxes -= boxes_positions_dict[skip]
        del boxes_positions_dict[skip]
    for box in boxes_positions_dict:
        while True:
            new_positions = set()
            for position in boxes_positions_dict[box]:
                x, y, z = position
                if z - 1 == 0:
                    continue
                new_positions.add((x, y, z - 1))
            if len(new_positions) != len(boxes_positions_dict[box]):
                break

            positions_with_boxes -= boxes_positions_dict[box]
            contains = False
            for new_position in new_positions:
                if new_position in positions_with_boxes:
                    contains = True
                    break
            if contains:
                positions_with_boxes.update(boxes_positions_dict[box])
                break
            
            falls.add(box)
            positions_with_boxes.update(new_positions)
            boxes_positions_dict[box] = new_positions

    return len(falls) == 0, len(falls)
    
fall(boxes_positions_dict, positions_with_boxes, None)

sum_1 = 0
sum_2 = 0
for i in range(len(boxes_positions_dict)):
    no_fall, num_falls = fall(boxes_positions_dict.copy(), positions_with_boxes.copy(), i)
    sum_1 += no_fall
    sum_2 += num_falls

print("Sum 1", sum_1)
print("Sum 2", sum_2)
