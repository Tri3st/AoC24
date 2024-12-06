from MyMods.ReadDataFile import read_data
from day6.guard_map import GuardMap

big_data = read_data("./day6/input_day6.txt")

test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split("\n")


def part1():
    map = GuardMap(big_data)
    print(map)


def part2():
    pass