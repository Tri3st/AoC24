import sys


def operate(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 * num2
    else:
        return sys.maxsize


class Equation:
    def __init__(self, data):
        data2 = data.split(':')
        self.eq = int(data2[0])
        self.nms = [int(x) for x in data2[1].split(' ') if x != '']
        self.result = False
        self.calc()

    def calc(self):
        self.calc_tree(self.nms, 1, self.nms[0], [str(self.nms[0])])


    def calc_tree(self, numbers, index=0, current_result=0, path=[]):
        if index == len(numbers):
            print(f"Path: {' -> '.join(path)}, result: {current_result}")
            if current_result == self.eq:
                self.result = True
            return [current_result]

        results= []

        # perform addition
        results += self.calc_tree(numbers, index + 1, current_result + numbers[index], path + [f"{current_result} + {numbers[index]}"])

        #perform multiplication
        results += self.calc_tree(numbers, index + 1, current_result * numbers[index], path + [f"{current_result} * {numbers[index]}"])

        # perform concatation
        results += self.calc_tree(numbers, index + 1, int(str(current_result) + (str(numbers[index]))), path + [f"{current_result} || {numbers[index]}"] )

        return results


    def __str__(self):
        return f"{self.eq}:{self.nms} -> {'MATCH' if self.result else 'no match'}"