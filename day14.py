from collections import Counter

f = open("inputs/day14", "r")

TEMPLATE = f.readline().strip()
RULES = dict(line.split(" -> ") for line in f.read().strip().split("\n"))


def calc(template, rules, steps):
    pairs = Counter([template[i:i + 2] for i in range(len(template) - 1)])
    for _ in range(steps):
        new_pairs = Counter()
        for (l, r), count in pairs.items():
            m = rules[l+r]
            new_pairs[l+m] += count
            new_pairs[m+r] += count
        pairs = new_pairs

    result = Counter()
    for (l, r), count in pairs.items():
        result[r] += count

    return max(result.values()) - min(result.values())


print(calc(TEMPLATE, RULES, 10))
print(calc(TEMPLATE, RULES, 40))
