from math import floor


def make_bitstrings_as_long(str1, str2):
    if len(str1) < len(str2):
        for i in range(len(str2) - len(str1)):
            str1 = "0" + str1
    elif len(str1) > len(str2):
        for _ in range(len(str1) - len(str2)):
            str2 = "0" + str2
    return str1, str2


class Comp:
    totals = {}
    def __init__(self, secrets):
        self.secrets = [int(s) for s in secrets]
        self.secret = None
        self.total = 0
        self.results = []
        for s in self.secrets:
            print(f"Secret {s}")
            self.secret = s
            for _ in range(2000):
                self.iterate()
            Comp.totals[s] = self.results[-1]
            print("2000th result : ", self.results[-1])
            self.results = []

    def iterate(self):
        if len(self.results) > 0:
            secr = self.results[-1]
        else:
            secr = self.secret
        temp = secr * 64
        temp = self.mix(temp, secr)
        secr = self.prune(temp)
        temp = floor(secr / 32)
        temp = self.mix(temp, secr)
        secr = self.prune(temp)
        temp = temp * 2048
        temp = self.mix(temp, secr)
        secr = self.prune(temp)
        self.results.append(secr)

    def mix(self, num1, num2):
        temp = bin(num1)[2:]
        bin_num = bin(num2)[2:]
        temp, bin_num = make_bitstrings_as_long(temp, bin_num)
        result = int("".join([ str(int(x) ^ int(y)) for (x,y) in zip(temp, bin_num)]), 2)
        return result

    def prune(self, num):
        return num % 16777216

    def get_sum(self):
        sum = 0
        for k in self.totals.keys():
            sum += self.totals[k]
        return sum
