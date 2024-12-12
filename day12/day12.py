from MyMods.ReadDataFile import read_data
from day12.garden import Garden


big_data = read_data("./day12/input_day12.txt")

test_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".split("\n")


def part1():
    garden = Garden(test_data)
    print(garden)
    print([g.__str__() for g in garden.plots])
    print("Total : ", garden.total_price)



def part2():
    pass