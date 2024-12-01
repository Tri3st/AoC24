class Number:
    def __init__(self, number, series):
        self.number = number
        self.series = series
        self.occ = 0
        self.spec = 0
        self.calc_occ()
        self.cal_spec()

    def calc_occ(self):
        for x in self.series[1]:
            if self.number == x:
                self.occ += 1

    def cal_spec(self):
        for x in self.series[1]:
            if self.number == x:
                self.spec = self.number * self.occ

    def __str__(self):
        return f"{self.number}: {self.occ} - {self.spec}"