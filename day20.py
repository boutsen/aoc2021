f = open("inputs/day20", "r")

RULE = f.readline().strip()
RAW = f.read().strip()
IMAGE = set()

for x, line in enumerate(RAW.split('\n')):
    for y, ch in enumerate(line.strip()):
        if ch == '#':
            IMAGE.add((x, y))


def enhance_image(image, rule, switch):
    new_image = set()
    rows = [r for r, c in image]
    cols = [c for r, c in image]
    neighbours = [-1, 0, 1]

    for r in range(min(rows)-1, max(rows)+2):
        for c in range(min(cols)-1, max(cols)+2):
            tmp = 0
            bit = 8
            for nr in neighbours:
                for nc in neighbours:
                    if ((r+nr, c+nc) in image) == switch:
                        tmp += 2 ** bit
                    bit -= 1
            if (rule[tmp] == '#') != switch:
                new_image.add((r, c))
    return new_image


for it in range(50):
    IMAGE = enhance_image(IMAGE, RULE, it % 2 == 0)
    if it == 1:
        print(len(IMAGE))
print(len(IMAGE))
