class Opcode:
    def __init__(self, instructions):
        data = instructions.split("\n")
        self.regA = int(data[0].split(":")[1])
        self.regB = int(data[1].split(":")[1])
        self.regC = int(data[2].split(":")[1])
        data2 = data[4].split(":")
        self.program = [int(n) for n in data2[1].split(",")]

    def do_calc(self):
        pass

    def __str__(self):
        return f"A: {self.regA}\nB: {self.regB}\nC: {self.regC}\nProgram: {self.program}\n\n"