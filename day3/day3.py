from MyMods.ReadDataFile import read_data
import re


big_data = read_data("./day3/input_day3.txt", mode=1)

test_data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

def part1():
    regex = r"mul\((\d+),(\d+)\)"
    x = re.findall(regex, big_data)
    print(x)
    print(sum([(int(a) * int(b)) for a,b in x]))

test_data2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def part2():
    search_text  = []
    regex0 = r"^(.*)don't\(\)"
    x = re.findall(regex0, big_data)
    search_text.extend(x)
    regex1 = r"do\(\)\(.+\)don't\(\)*"
    x2 = re.findall(regex1, big_data)
    search_text.extend(x2)
    # regex2 = r"do\(\)(.*)$"
    # x3 = re.findall(regex2, big_data)
    # search_text.extend(x3)
    print(search_text)
    x5 = "".join(search_text)
    regex3 = r"\((\d+),(\d+)\)"
    x4 = re.findall(regex3, x5)
    print(x4)
    print(sum([(int(c) * int(d)) for c,d in x4]))

