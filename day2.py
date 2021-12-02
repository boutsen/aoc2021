import re

f = open("inputs/day2", "r")

DATA = [(direction, int(amount)) for direction, amount in re.findall(r"(\w+) (\d+)", f.read())]


def part1(data):
    h = 0
    d = 0
    for inst in data:
        if inst[0] == "forward":
            h += inst[1]
        elif inst[0] == "down":
            d += inst[1]
        elif inst[0] == "up":
            d -= inst[1]
    return h * d


def part2(data):
    h = 0
    d = 0
    aim = 0
    for inst in data:
        if inst[0] == "forward":
            h += inst[1]
            d += (aim*inst[1])
        elif inst[0] == "down":
            aim += inst[1]
        elif inst[0] == "up":
            aim -= inst[1]
    return h * d


print(part1(DATA))
print(part2(DATA))

