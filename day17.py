import re
f = open("inputs/day17", "r")

x1, x2, y1, y2 = map(int, re.findall(r'-?\d+', f.read()))


def follow(vx, vy):
    x, y, top = 0, 0, 0
    while x <= x2 and y >= y1:
        x, y = x + vx, y + vy
        vx, vy = max(0, vx - 1), vy - 1
        top = max(top, y)
        if x1 <= x <= x2 and y1 <= y <= y2:
            return top
    return -1


all_valid = {(x, y): follow(x, y) for x in range(x2+1) for y in range(y1, -y1) if follow(x, y) >= 0}

print(max(all_valid.values()))
print(len(all_valid))
