f = open("inputs/day1", "r")

DATA = [int(line) for line in f.readlines()]


def part1(data):
    return sum(1 if data[d] > data[d-1] else 0 for d in range(1, len(data)))


def part2(data):
    return part1([data[d]+data[d-1]+data[d-2] for d in range(2, len(data))])


print(part1(DATA))
print(part2(DATA))