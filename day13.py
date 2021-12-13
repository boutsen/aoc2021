import re
f = open("inputs/day13", "r")

LINES = f.read()
DOTS = [(int(x), int(y)) for x, y in re.findall(r"(\d+),(\d+)", LINES)]
FOLDS = [(axis, int(line)) for axis, line in re.findall(r"fold along (x|y)=(\d+)", LINES)]


def fold(dots, axis, line):
    if axis == 'x':
        return list(dict.fromkeys([(2 * line - x, y) if x > line else (x, y) for x, y in dots]))
    else:
        return list(dict.fromkeys([(x, 2 * line - y) if y > line else (x, y) for x, y in dots]))


def visualize(dots, x, y):
    for i in range(x):
        print("".join(["#" if (j, i) in dots else "." for j in range(y)]))


def part1(dots, folds):
    axis, line = folds[0]
    return len(fold(dots, axis, line))


def part2(dots, folds):
    for axis, line in folds:
        dots = fold(dots, axis, line)
    visualize(dots, max(dots)[1]+1, max(dots)[0]+1)


print(part1(DOTS, FOLDS))
part2(DOTS, FOLDS)
