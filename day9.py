import math
f = open("inputs/day9", "r")

DATA = {}

for i, line in enumerate(f.readlines()):
    for j, num in enumerate(line.strip()):
        DATA[(j, i)] = int(num)


def get_neighbours_coordinates(x, y):
    return [(x1, y1) for (x1, y1) in {(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)} if
                      0 <= x1 < 100 and 0 <= y1 < 100]


def get_low_points(data):
    return [(x, y) for x, y in data if all(data[(x, y)] < data[n] for n in get_neighbours_coordinates(x, y))]


def calc_basin(data, coordinate, basin):
    for neighbour in get_neighbours_coordinates(coordinate[0], coordinate[1]):
        if data[neighbour] > data[coordinate] and data[neighbour] != 9:
            basin.add(neighbour)
            calc_basin(data, neighbour, basin)
    return basin


def part1(data):
    return sum([data[low] + 1 for low in get_low_points(data)])


def part2(data):
    return math.prod(sorted([len(calc_basin(data, coordinate, {coordinate})) for coordinate in get_low_points(data)])[-3:])


print(part1(DATA))
print(part2(DATA))
