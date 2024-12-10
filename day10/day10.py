from MyMods.ReadDataFile import read_data
from day10.topo_map import TopoMap


big_data = read_data("./day10/input_day10.txt")

test_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split("\n")


def part1():
    map = TopoMap(test_data)
    print(map)
    print(map.start)
    print(map.routes)


def part2():
    pass