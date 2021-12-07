import sys
f = open("inputs/day7", "r")

CRABS = [int(crab) for crab in f.readline().split(",")]


def part1(crabs):
    smallest = sum(crabs)
    for i in range(min(crabs), max(crabs)):
        smallest = min(smallest, sum([fuel-i if fuel > i else i - fuel for fuel in crabs]))
    return smallest


def part2(crabs):
    smallest = sys.maxsize
    for i in range(min(crabs), max(crabs)):
        smallest = min(smallest, sum([((fuel-i)*(fuel-i+1))/2 if fuel > i else ((i-fuel)*(i-fuel+1))/2 for fuel in crabs]))
    return smallest


print(part1(CRABS))
print(part2(CRABS))
