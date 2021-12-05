import re
from collections import defaultdict

f = open("inputs/day5", "r")

vents = [(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", f.read())]
ocean_floor = defaultdict(int)
for vent in vents:
    if vent[0] == vent[2]:
        for i in range(min(vent[1], vent[3]), max(vent[1], vent[3])+1):
            ocean_floor[str(vent[0]) + "-" + str(i)] += 1
    if vent[1] == vent[3]:
        for i in range(min(vent[0], vent[2]), max(vent[0], vent[2])+1):
            ocean_floor[str(i) + "-" + str(vent[1])] += 1

print("Part 1: " + str(sum([1 for count in ocean_floor.values() if count >= 2])))

for vent in vents:
    if abs(vent[0] - vent[2]) == abs(vent[1] - vent[3]):
        for i in range(abs(vent[0] - vent[2]) + 1):
            cx = (i if vent[0] < vent[2] else -i)
            cy = (i if vent[1] < vent[3] else -i)
            ocean_floor[str(vent[0] + cx) + "-" + str(vent[1] + cy)] += 1

print("Part 2: " + str(sum([1 for count in ocean_floor.values() if count >= 2])))