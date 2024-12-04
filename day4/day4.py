from MyMods.ReadDataFile import read_data
from day4.puzzle import Puzzle

big_data = read_data('./day4/input_day4.txt')

test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")

def part1():
    puzzle = Puzzle(big_data)
    print(puzzle)
    print(puzzle.dimj, puzzle.dimi)
    print(f"Total words found : {puzzle.word_count2}")

def part2():
    pass
