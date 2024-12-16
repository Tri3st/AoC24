from MyMods.ReadDataFile import read_data

from AoC.AoC24.day13.arcade import Arcade

big_data = read_data('./day13/input_day13.txt', mode=1).split("\n\n")

test_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split("\n\n")


def part1():
    arcade = Arcade(big_data)
    print(arcade)

def part2():
    arcade = Arcade(test_data, part=2)
    print(arcade)