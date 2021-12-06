f = open("inputs/day6", "r")

FISH = [int(fish) for fish in f.readline().split(",")]

# BRUTE FORCE APPROACH - became pretty clear with part2 it would take ages to calculate
def part1(fish, nr_of_days):
    for i in range(nr_of_days):
        nr_of_fish_ready = sum([1 for ready in fish if ready == 0])
        fish = [timer-1 if timer > 0 else 6 for timer in fish]
        for j in range(nr_of_fish_ready):
            fish.append(8)

    return len(fish)


def part2(fish, nr_of_days):
    count = [fish.count(i) for i in range(9)]
    for i in range(nr_of_days):
        new_fish = count.pop(0)
        count[6] += new_fish
        count.append(new_fish)
    return sum(count)


print(part1(FISH.copy(),80))
print(part2(FISH.copy(),256))