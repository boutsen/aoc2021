from collections import defaultdict

f = open("inputs/day8", "r")

DIGITS = f.read().splitlines()
KNOWN_SIGNALS = {2: '1', 4: '4', 3: '7', 7: '8'}


def part1(data, known_signals):
    output = [line.split(" | ")[1].split(" ") for line in data]
    result = 0
    for signals in output:
        result += len([signal for signal in signals if len(signal) in known_signals.keys()])
    return result


def part2(data, known_signals):
    result = 0
    for line in data:
        digits = line.split(' | ')[0].split()
        output = [sorted(o) for o in line.split(' | ')[1].split()]
        signals = defaultdict(str)
        for d in [signal for signal in digits if len(signal) in known_signals.keys()]:
            signals[known_signals[len(d)]] = sorted(d)

        for d in [signal for signal in digits if len(signal) not in known_signals.keys()]:
            if len(d) == 6:
                if len(set(signals['4']) & set(d)) == 4:
                    signals['9'] = sorted(d)
                elif len(set(signals['7']) & set(d)) == 3:
                    signals['0'] = sorted(d)
                else:
                    signals['6'] = sorted(d)
            if len(d) == 5:
                if len(set(signals['7']) & set(d)) == 3:
                    signals['3'] = sorted(d)
                elif len(set(signals['4']) & set(d)) == 3:
                    signals['5'] = sorted(d)
                else:
                    signals['2'] = sorted(d)

        result += int(''.join([list(signals.keys())[list(signals.values()).index(o)] for o in output]))
    return result


print(part1(DIGITS, KNOWN_SIGNALS))
print(part2(DIGITS, KNOWN_SIGNALS))
