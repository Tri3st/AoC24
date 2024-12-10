import sys

from MyMods.ReadDataFile import read_data
from day9.diskmap import Diskmap

test_data = """2333133121414131402"""

def read_char():
    with open('day9/input_day9.txt', 'r') as file:
        while char := file.read(1):
            yield char

t = 2

def part1():
    d = Diskmap()
    if t == 1:
        for i in test_data:
            d.new_num(int(i))
    else:
        for c in read_char():
            d.new_num((int(c)))
    print(d)
    print(d.count_empty)
    print([x for d.diskmap])
    #d.calc()
    #print(d)
    #print(d.calc_sum())


def part2():
    pass
