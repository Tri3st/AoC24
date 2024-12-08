class Order:
    def __init__(self, data):
        data2 = data.split('\n\n')
        data3 = data2[0].split("\n")
        data4 = data2[1].split("\n")
        self.ordering = [d.split("|") for d in data3]
        self.pages_lists = [n.split(",") for n in data4]
        self.wrong_pages = []
        self.sum = 0
        for lst in self.pages_lists:
            print("Checking line ", lst)
            check = self.check_line(lst)
            if check:
                self.sum += int(lst[(len(lst) // 2)])
            else:
                self.wrong_pages.append(lst)
            print(check)
        self.do_wrong_lines(self.wrong_pages[0])

    def check_line(self, line):
        for i, x in enumerate(line):
            print("Checking line ", line)
            # check if x is in rules
            for rule in self.ordering:
                print("rule : ", rule)
                if rule[0] in line and rule[1] in line:
                    idx_1 = line.index(rule[0])
                    idx_2 = line.index(rule[1])
                    if idx_1 < idx_2:
                        continue
                    else:
                        return False
        return True

    def do_wrong_lines(self, line):
        for x in line:
            pass