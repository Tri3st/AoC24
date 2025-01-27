from MyMods.ReadDataFile import read_data

from day25.key_locks import KeyLocks

big_data = read_data('day25/input_day25.txt', mode=1).split("\n\n")

test_data = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".split("\n\n")


def part1():
    kls = KeyLocks(big_data)
    # print(kls)
    # print(kls.fits)
    # print(kls.total_fits)


def part2():
    pass
