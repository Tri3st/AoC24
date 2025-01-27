from MyMods.ReadDataFile import read_data
from day22.comp import Comp

big_data = read_data("day22/input_day22.txt")

test_data = """1
10
100
2024""".split("\n")

def part1():
    comp = Comp(big_data)
    print("Total of totals : ", comp.get_sum())

def part2():
    pass
