from MyMods.ReadDataFile import read_data

from day17.opcode import Opcode

big_data = read_data('./day17/input_day17.txt', mode=1)

test_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

test2 = """Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4"""


test3 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

test4 = """Register A: 0
Register B: 29
Register C: 43690

Program: 1,7"""

test5 = """Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0"""

def part1():
    op = Opcode(big_data)


def part2():
    for i in range(10000000, 1000000000):
        data = f"""Register A: {i}
Register B: 0
Register C: 0

Program: 2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0
        """
        op = Opcode(data)
        if op.output == [2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0]:
            print(f"Got it! for i == {i}")
            break
