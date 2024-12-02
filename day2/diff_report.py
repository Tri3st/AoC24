from AoC24.day2.report_item import ReportItem


class DiffReport:
    def __init__(self, id, num1: ReportItem, num2: ReportItem):
        self.id = id
        self.num1 = num1
        self.num2 = num2
        self.type = None
        self.value = None
        self.calc()

    def calc(self):
        if self.num2.num > self.num1.num:
            self.type = "incr"
            self.value = self.num2.num - self.num1.num
        elif self.num2.num < self.num1.num:
            self.type = "decr"
            self.value = self.num1.num - self.num2.num
        else:
            self.type = "equal"
            self.value = 0

    def __str__(self):
        return f"{self.id}: {self.num1}, {self.num2} -> {self.type}:{self.value}"