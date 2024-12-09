from MyMods.ReadDataFile import read_data
from day7.equation import Equation

big_data = read_data("./day7/input_day7.txt")

test_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split("\n")


def part1():
    sum = 0
    for line in big_data:
        eq = Equation(line)
        if eq.result:
            sum += eq.eq

    print(sum)


def part2():
    sum = 0
    for line in big_data:
        eq = Equation(line)
        if eq.result:
            sum += eq.eq

    print(sum)