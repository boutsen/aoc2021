from collections import defaultdict
f = open("inputs/day12", "r")

CAVECONNECTIONS = defaultdict(list)

for line in f.readlines():
    cave1, cave2 = line.strip().split('-')
    CAVECONNECTIONS[cave1].append(cave2)
    CAVECONNECTIONS[cave2].append(cave1)


def follow(caves, max_visits, visited, cave):
    if cave == 'end':
        return 1
    if cave in visited:
        if cave == 'start' or (cave.islower() and max_visits == 1):
            return 0
        if cave.islower() and max_visits > 1:
            max_visits = 1

    return sum(follow(caves, max_visits, visited | {cave}, next_cave) for next_cave in caves[cave])


print(follow(CAVECONNECTIONS, 1, set(), 'start'))
print(follow(CAVECONNECTIONS, 2, set(), 'start'))
