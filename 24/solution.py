import sympy

with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

hailstones = []
for row in data:
    pxpypz, vxvyvz = row.split(" @ ")
    px, py, pz = map(int, pxpypz.split(", "))
    vx, vy, vz = map(int, vxvyvz.split(", "))
    a, b, c = (vy), -(vx), (vy * px - vx * py)
    hailstones.append((px, py, pz, vx, vy, vz, a, b, c))

total = 0
for i, hs_1 in enumerate(hailstones):
    for hs_2 in hailstones[:i]:
        px1, py1, pz1, vx1, vy1, vz1, a1, b1, c1 = hs_1
        px2, py2, pz2, vx2, vy2, vz2, a2, b2, c2 = hs_2
        if a1 * b2 == b1 * a2:
            continue
        x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
        if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
            results = []
            for hs in (hs_1, hs_2):
                px, py, pz, vx, vy, vz, a, b, c = hs
                results.append(((x - px) * vx >= 0 and (y - py) * vy >= 0))
            if all(results):
                total += 1

print("Sum 1", total)

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for i, (px, py, pz, vx, vy, vz, a, b, c) in enumerate(hailstones):
    equations.append((xr - px) * (vy - vyr) - (yr - py) * (vx - vxr))
    equations.append((yr - py) * (vz - vzr) - (zr - pz) * (vy - vyr))
    if i < 2:
        continue
    answers = []
    for soln in sympy.solve(equations):
        ret = []
        for x in soln.values():
            ret.append(x % 1 == 0) 
        if all(ret):
            answers.append(soln)

    if len(answers) == 1:
        break
    
answer = answers[0]

print("Sum 2", answer[xr] + answer[yr] + answer[zr])
