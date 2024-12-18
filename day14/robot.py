import re


class Robot:
    def __init__(self, line):
        reg = re.compile(r'^p=(\d+),(\d+) v=(-?\d+),(-?\d+)$')
        result = re.findall(reg, line)[0]
        self.old_point = None
        self.point = int(result[1]), int(result[0]) if result else None
        self.velocity = int(result[3]), int(result[2]) if result else None

    def move(self, dimj, dimi):
        self.old_point = self.point
        self.point = (self.old_point[0] + self.velocity[0]) % dimj, (self.old_point[1] + self.velocity[1]) % dimi
        print(self.point)
        return self.point

    def __str__(self):
        return '<Robot point={}, velocity={}'.format(self.point, self.velocity)
