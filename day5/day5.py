from MyMods.ReadDataFile import read_data
from day5.order import Order

big_data = read_data("./day5/input_day5.txt", mode=1)

test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def part1():
    order = Order(big_data)
    print(order)
    print(order.ordering)
    print(order.pages_lists)
    print(order.sum)
    print(order.wrong_pages)


def part2():
    order = Order(test_data)
    print("Order : ", order)
    print("Ordering : ", order.ordering)
    print("Wronge pages : ", order.wrong_pages)