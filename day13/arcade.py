from AoC.AoC24.day13.claw import Claw


class Arcade:
    def __init__(self, data, part=1):
        self.part = part
        self.claws = []
        for line in data:
            self.claws.append(Claw(line, self.part))
        self.calc_claws()

    def calc_claws(self):
        total = 0
        for claw in self.claws:
            if claw.result:
                total += claw.cost
        print(total)

    def __str__(self):
        res = ""
        for claw in self.claws:
            res += str(claw)
            res += "\n"
        return res