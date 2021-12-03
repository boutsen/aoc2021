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
    oxyArr = data.copy()
    co2Arr = data.copy()

    oxy = 0
    co2 = 0

    for i in range(len(data[0])):
        oxyBin = [d[i] for d in oxyArr]
        co2bin = [d[i] for d in co2Arr]

        oxyArr = [d for d in oxyArr if d[i] == ('1' if oxyBin.count("1") >= oxyBin.count("0") else '0')]
        co2Arr = [d for d in co2Arr if d[i] == ('1' if co2bin.count("1") < co2bin.count("0") else '0')]

        if len(oxyArr) == 1:
            oxy = int(oxyArr[0], 2)

        if len(co2Arr) == 1:
            co2 = int(co2Arr[0], 2)
    return oxy*co2


print(part1(DATA))
print(part2(DATA))

