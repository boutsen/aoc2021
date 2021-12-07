import sys, statistics
f = open("inputs/day7", "r")

CRABS = [int(crab) for crab in f.readline().split(",")]


def part1(crabs):
    smallest = sys.maxsize
    for i in range(min(crabs), max(crabs)):
        smallest = min(smallest, sum([abs(fuel-i) for fuel in crabs]))
    return smallest


def part2(crabs):
    smallest = sys.maxsize
    for i in range(min(crabs), max(crabs)):
        smallest = min(smallest, sum([(abs(fuel - i) * (abs(fuel - i) + 1)) / 2 for fuel in crabs]))
    return smallest


def part1_median(crabs):
    return sum([abs(fuel-statistics.median(crabs)) for fuel in crabs])


print(part1(CRABS))
print(int(part2(CRABS)))

print(int(part1_median(CRABS)))
