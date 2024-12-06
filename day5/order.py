class Order:
    def __init__(self, data):
        data2 = data.split('\n\n')
        data3 = data2[0].split("\n")
        data4 = data2[1].split("\n")
        self.ordering = [d.split("|") for d in data3]
        self.pages_lists = [n.split(",") for n in data4]
        self.sum = 0
        for lst in self.pages_lists:
            print("Checking line ", lst)
            check = self.check_line(lst)
            if check:
                self.sum += int(lst[(len(lst) // 2)])
            print(check)

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
