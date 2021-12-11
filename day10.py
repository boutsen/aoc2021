import statistics

f = open("inputs/day10", "r")

SYNTAX = [line.strip("\n") for line in f.readlines()]
OPENBRACKETS = "([{<"
CLOSINGBRACKETS = ")]}>"


def part1(data, openc, closec):
    scores = [3, 57, 1197, 25137]
    score = 0
    for line in data:
        expected = []
        for i in range(len(line)):
            if line[i] in openc:
                expected.append(closec[openc.index(line[i])])
            elif expected[-1] != line[i]:
                score += scores[closec.index(line[i])]
                break
            else:
                expected = expected[:-1]
    return score


def part2(data, openc, closec):
    scores = [1, 2, 3, 4]
    total_score = []
    for line in data:
        score = 0
        expected = []
        for i in range(len(line)):
            if line[i] in openc:
                expected.append(closec[openc.index(line[i])])
            else:
                expected = expected[:-1]
        for i in reversed(expected):
            score = score * 5 + scores[closec.index(i)]
        total_score.append(score)
    total_score.sort()
    return total_score[int(len(total_score)/2)]


print(part1(SYNTAX, OPENBRACKETS, CLOSINGBRACKETS))
print(part2(SYNTAX, OPENBRACKETS, CLOSINGBRACKETS))
