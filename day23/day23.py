from MyMods.ReadDataFile import read_data
from day23.lanplan import LanPlan

big_data = read_data('./day23/input_day23.txt', mode=0)

test_data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".split("\n")


def part1():
    lan = LanPlan(test_data)
    print(lan.triplets)


def part2():
    pass