import math
import re


class Claw:
    def __init__(self, data, part=1):
        self.part = part
        self.buttons = {'A' : {'x': 0, 'y': 0, 'cost': 3},'B': {'x': 0, 'y': 0, 'cost': 1}}
        self.prize = {'x': 0, 'y': 0}
        self.result = None
        self.cost = 0
        self.do_data(data)

    def do_data(self, data):
        data2 = data.split('\n')
        reg = r"^Button [AB]: X\+(\d+), Y\+(\d+)$"
        reg2 = r"^Prize: X=(\d+), Y=(\d+)$"
        button_a = re.findall(reg, data2[0])
        button_b = re.findall(reg, data2[1])
        prize = re.findall(reg2, data2[2])
        self.buttons['A']['x'] = int(button_a[0][0])
        self.buttons['A']['y'] = int(button_a[0][1])
        self.buttons['B']['x'] = int(button_b[0][0])
        self.buttons['B']['y'] = int(button_b[0][1])
        if self.part == 1:
            self.prize = {'x': int(prize[0][0]), 'y': int(prize[0][1])}
        else:
            fac = 10000000000000
            self.prize = {'x': int(prize[0][0]) + fac, 'y': int(prize[0][1]) + fac}

        self.result = self.min_times_to_prize()
        self.cost = (self.result[0] * self.buttons['A']['cost'] + self.result[1] * self.buttons['B']['cost']) if self.result else 0

    def min_times_to_prize(self):
        min_presses = float('inf')
        result = None

        for a in range(self.prize['x'] // self.buttons['A']['x'] + 1):
            remaining_x = self.prize['x'] - a * self.buttons['A']['x']
            remaining_y = self.prize['y'] - a * self.buttons['A']['y']

            if remaining_x >= 0 and remaining_y >= 0:
                if remaining_x % self.buttons['B']['x'] == 0 and remaining_y % self.buttons['B']['y'] == 0:
                    b = remaining_x // self.buttons['B']['x']
                    if b * self.buttons['B']['y'] == remaining_y:
                        min_presses = a + b
                        result = (a, b)
        print(result)
        return result

    def cost(self, list_of_results):
        # list of results for instance [80, 40] where 80 is the A button and 40 is the B button
        print(list_of_results, type(list_of_results))
        return list_of_results[0] * self.buttons['A']['cost'] + list_of_results[1] * self.buttons['B']['cost']

    def __str__(self):
        return (f"Button A: X+{self.buttons['A']['x']}, Y+{self.buttons['A']['y']}\n"
                f"Button B: X+{self.buttons['B']['x']}, Y+{self.buttons['B']['y']}\n"
                f"Prize: X={self.prize['x']}, Y={self.prize['y']}\n")