class Report:
    def __init__(self, line):
        self.numbers = [int(l.strip()) for l in line.split()]
        self.new_numbers = None
        self.status = "unsafe"
        self.length = len(self.numbers)
        self.report = []
        self.diffs = self.calc()
        self.calc_safe()

    def calc(self, l2=None):
        l3 = l2 if l2 is not None else self.numbers
        diffs = []
        for i,n in enumerate(l3):
            if i > 0:
                diffs.append({
                    'id': i - 1,
                    'num1': l3[i-1],
                    'num2': l3[i],
                    'type': 'incr' if l3[i] > l3[i-1] else 'decr' if l3[i] < l3[i-1] else 'equal',
                    'value': abs(l3[i] - l3[i-1]),
                })
        return diffs

    def calc_safe(self, nmbrs=None):
        diffs = nmbrs if nmbrs is not None else self.diffs
        incr, decr, equal, maxc = self.check(diffs)
        self.safe(incr, decr, equal, maxc)


    def safe(self, incr, decr, equal, maxc):
        main_type = None
        self.safe_pass(incr, decr, maxc, self.length - 1)
        if len(incr) == self.length - 2:
            # one wrong in increase
            wrong = decr[0] if decr else equal[0]
            print("wrong : ", wrong)
            new_numbers = self.numbers.copy()
            new_numbers.pop(wrong['id'])
            print(new_numbers)
            new_diffs = self.calc(new_numbers)
            i, d, eq, m = self.check(new_diffs)
            self.safe_pass(i, d, m, self.length - 2)
            print("status is now ", self.status)

        elif len(decr) == self.length - 2:
            # one wrong in decrease
            wrong2 = incr[0] if incr else equal[0]
            print("wrong : ", wrong2)
            new_numbers = self.numbers.copy()
            new_numbers.pop(wrong2['id'])
            print(new_numbers)
            new_diffs = self.calc(new_numbers)
            i, d, eq, m = self.check(new_diffs)
            self.safe_pass(i, d, m, self.length - 2)
            print("status is now ", self.status)
        else:
            # one wrong in max in/decrease
            pass

    def safe_pass(self, inc, decr, max_crease, length):
        if (len(inc) == length or len(decr) == length) and len(max_crease) == length:
            self.status = 'safe'

    def check(self, diffs=None):
        my_diffs = diffs if diffs is not None else self.diffs
        inc = [d for d in my_diffs if d['type'] == 'incr']
        decr = [d for d in my_diffs if d['type'] == 'decr']
        equal = [d for d in my_diffs if d['type'] == 'equal']
        max_crease = [d for d in my_diffs if (0 < d['value'] < 4) and d['type'] != 'equal']
        return inc, decr, equal, max_crease

    def __str__(self):
        return f"{[f"{x['id']} {x['type']} {x['value']}" for x in self.diffs]} -> {self.status}"
