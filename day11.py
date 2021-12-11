f = open("inputs/day11", "r")

OCTOPUSSIES = {}

for i, line in enumerate(f.readlines()):
    for j, num in enumerate(line.strip()):
        OCTOPUSSIES[(j, i)] = int(num)


def get_neighbours(x, y):
    return [(x1, y1) for (x1, y1) in {
        (x, y - 1), (x, y + 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y - 1), (x - 1, y + 1),
        (x + 1, y - 1), (x + 1, y + 1)
    } if 0 <= x1 < 10 and 0 <= y1 < 10]


def part1(octopussies, steps):
    flashes = 0

    for _ in range(steps):
        for (x, y) in octopussies:
            octopussies[(x, y)] += 1

        flashed = []
        flashers = [(x, y) for (x, y) in octopussies if octopussies[(x, y)] > 9]

        while flashers:
            flashed.extend(flashers)
            for (x, y) in flashers:
                for neighbour in get_neighbours(x, y):
                    octopussies[neighbour] += 1
            flashers = [(x, y) for (x, y) in octopussies if octopussies[(x, y)] > 9 and (x, y) not in flashed]

        for flash in flashed:
            octopussies[flash] = 0
            flashes += 1

    return flashes


def part2(octopussies):
    flashes, steps = 0, 0
    while flashes < 100:
        flashes = part1(octopussies, 1)
        steps += 1

    return steps


print(part1(OCTOPUSSIES.copy(), 100))
print(part2(OCTOPUSSIES.copy()))
