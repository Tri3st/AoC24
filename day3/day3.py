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
    search_text = []
    regex = r"^(.*)don't()"
    first  = re.search(regex, big_data)
    search_text.append(first.group(1))
    new_data = big_data[first.span()[1]:]
    regex2 = r"do\(\)^(.*)don't()"
    while True:
        next = re.search(regex2, new_data)
        if next:
            search_text.append(next.group(1))
            new_data = new_data[next.span()[1]:]
        else:
            break
    print(search_text, len(search_text))
    regex3 = r"mul\((\d+),(\d+)\)"
    result = []
    for tx in search_text:
        last = re.findall(regex3, tx, re.DOTALL)
        print(last)
        result.extend(last)
    print(sum([(int(a) * int(b)) for a,b in result]))


import re


def parse_and_evaluate_memory(memory):
    # Regex patterns
    mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"  # Matches valid mul(X,Y)
    control_pattern = r"\b(do\(\)|don't\(\))"  # Matches do() or don't()

    # Variables to track state
    enabled = True  # Initially, mul instructions are enabled
    total_sum = 0  # Sum of valid multiplications

    # Split memory into sections for processing
    instructions = re.findall(f"{mul_pattern}|{control_pattern}", memory)

    for instruction in instructions:
        if instruction[2]:  # Control instructions (do() or don't())
            if instruction[2] == "do()":
                enabled = True
            elif instruction[2] == "don't()":
                enabled = False
        elif instruction[0] and instruction[1]:  # Valid mul(X,Y)
            if enabled:
                x, y = int(instruction[0]), int(instruction[1])
                total_sum += x * y

    return total_sum


# Test input
memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def part3():
    # Compute the sum of valid multiplications
    result = parse_and_evaluate_memory(big_data)
    print("The sum of the valid multiplications is:", result)


