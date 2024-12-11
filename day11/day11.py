from MyMods.ReadDataFile import read_data
from day11.stones import Stones


big_data = read_data("./day11/input_day11.txt", mode=1)

test_data = """125 17"""


def part1():
    stones = Stones(big_data)
    print(stones.stones)
    for _ in range(75):
        stones.do_blink()
        print(stones.stones)
    print(len(stones.stones))


def part2():
    pass