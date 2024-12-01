from MyMods.ReadDataFile import read_data

from AoC24.MyMods.number import Number

big_data = read_data("./day1/input_day1.txt", mode=1)

test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""

print(big_data)

def part1():
    print("Starting part 1 of Day 1")
    series = {0: [], 1: []}
    for line in big_data.split("\n"):
        i = 0
        d = line.split()
        print(d)
        for d2 in d:
            print("d2 : ", d2)
            series[i].append(int(d2.strip()))
            i += 1
    series[0].sort()
    series[1].sort()
    result = [abs(x - y) for x, y in zip(series[0], series[1])]
    print(sum(result))

def part2():
    print("Starting part 2 of Day 1")
    series = {0: [], 1: []}
    results = []
    for line in big_data.split("\n"):
        d = line.split()
        series[0].append(int(d[0]))
        series[1].append(int(d[1]))
    results = [Number(int(x), series) for x in series[0]]
    result = sum([r.spec for r in results])
    print(result)