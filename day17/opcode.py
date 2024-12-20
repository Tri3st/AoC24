def xor(num1, num2):
    num1_ = bin(num1)[2:]
    num2_ = bin(num2)[2:]
    xor = [ int(x) ^ int(y) for x, y in zip(num1_, num2_)]
    return int("".join([str(c) for c in xor]), 2)


class Opcode:
    def __init__(self, instructions):
        data = instructions.split("\n")
        self.regA = int(data[0].split(":")[1])
        self.regB = int(data[1].split(":")[1])
        self.regC = int(data[2].split(":")[1])
        data2 = data[4].split(":")
        self.program = [int(n) for n in data2[1].split(",")]
        self.pointer = 0
        self.output = []
        print(self.__str__())

    def do_calc(self):
        opcode = self.program[self.pointer]
        op = self.program[self.pointer + 1]
        print(f"step {self.pointer + 1} : opcode {opcode}, operand {op}")
        if 0<= op < 4:
            operand = op
        elif op == 4:
            operand = self.regA.copy()
        elif op == 5:
            operand = self.regB.copy()
        elif op == 6:
            operand = self.regC.copy()
        if opcode == 0:
            self.adv(operand)
        elif opcode == 1:
            self.bxl(operand)
        elif opcode == 2:
            self.bst(operand)
        elif opcode == 3:
            self.jnz(operand)
        elif opcode == 4:
            self.bxc(operand)
        elif opcode == 5:
            self.out(operand)
        elif opcode == 6:
            self.bdv(operand)
        elif opcode == 7:
            self.cdv(operand)
        print(self.__str__())

    def adv(self, operand):
        self.regA = int(self.regA / 2 ** operand)
        self.pointer += 2

    def bxl(self, operand):
        self.regB = xor(self.regB, operand)
        self.pointer += 2

    def bst(self, operand):
        self.regB = (operand % 8)
        self.pointer += 2

    def jnz(self, operand):
        if self.regA != 0:
            self.pointer = operand
        else:
            self.pointer += 2

    def bxc(self, _):
        temp = xor(self.regB, self.regC)
        self.regB = temp
        self.pointer += 2

    def out(self, operand):
        self.output.extend([int(x) for x in list(str(operand % 8))])
        self.pointer += 2

    def bdv(self, operand):
        self.regB = int(self.regA / 2 ** operand)
        self.pointer += 2

    def cdv(self, operand):
        self.regC = int(self.regA / 2 ** operand)
        self.pointer += 2

    def __str__(self):
        return f"A: {self.regA}\nB: {self.regB}\nC: {self.regC}\nProgram: {self.program}\nOutput: {self.output}\n\n"