f = open("inputs/day3", "r")

DATA = f.read().splitlines()


def part1(data):
    gamma = ""
    epsilon = ""

    for i in range(len(data[0])):
        arr = [d[i] for d in data]
        gamma += ('1' if arr.count("1") >= len(arr)/2 else '0')
        epsilon += ('1' if arr.count("1") < len(arr)/2 else '0')

    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    oxyarr = data.copy()
    co2arr = data.copy()

    oxy = 0
    co2 = 0

    for i in range(len(data[0])):
        oxybin = [d[i] for d in oxyarr]
        co2bin = [d[i] for d in co2arr]

        oxyarr = [d for d in oxyarr if d[i] == ('1' if oxybin.count("1") >= oxybin.count("0") else '0')]
        co2arr = [d for d in co2arr if d[i] == ('1' if co2bin.count("1") < co2bin.count("0") else '0')]

        if len(oxyarr) == 1:
            oxy = int(oxyarr[0], 2)

        if len(co2arr) == 1:
            co2 = int(co2arr[0], 2)
    return oxy*co2


print(part1(DATA))
print(part2(DATA))