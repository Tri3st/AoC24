from MyMods.ReadDataFile import read_data
from day14.robotmap import RobotMap

big_data = read_data('./day14/input_day14.txt', mode=0)

test_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".split("\n")


def part1():
    robot_map = RobotMap(test_data, 1)
    print(robot_map.__repr__())


def part2():
    pass