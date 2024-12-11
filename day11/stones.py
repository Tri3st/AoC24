class Stones:
    def __init__(self, data):
        data2 = data.split(" ")
        self.stones = [int(d) for d in data2]
        self.cursor = 0
        self.blink = 0

    def do_blink(self):
        temp_stones = []
        for st in self.stones:
            if st == 0:
                temp_stones.append(1)
            elif len(str(st)) % 2 == 0:
                half_length = int(len(str(st)) / 2)
                part1 = int(str(st)[0:half_length])
                part2 = int(str(st)[half_length:])
                temp_stones.append(part1)
                temp_stones.append(part2)
            else:
                temp_stones.append(st * 2024)
        self.stones = temp_stones

    def __str__(self):
        return f"blink {self.blink} : {self.stones}"
