from MyMods.Matrix import Matrix


class GuardMap(Matrix):
    DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def __init__(self, data):
        super().__init__(len(data), len(data[0]), '.')
        self.add_lines(data)
        self.start = self.find_start()
        self.position = self.start
        self.direction = 0
        self.travel()

    def travel(self):
        j, i = self.start
        while True:
            # walk in direction until obstruction or end of map
            print("Going ", self.DIRECTION[self.direction])
            if self.check_next(j, i):
                j, i = self.go_next(j, i)
            else:
                print("ENDED")
                cnt = self.count_xs()
                print(f"There are {self.count_xs()} X's")
                break


    def check_next(self, j , i):
        direc = self.DIRECTION[self.direction]
        print(j, i)
        if j + direc[0] < 0 or j + direc[0] > self.dimj - 1 or i + direc[1] < 0 or i + direc[1] > self.dimi - 1:
            return False
        return True

    def go_next(self, j, i):
        direc = self.DIRECTION[self.direction]
        new_pos = j + direc[0], i + direc[1]
        if self.grid[new_pos[0]][new_pos[1]] == '.' or self.grid[new_pos[0]][new_pos[1]] == '^' or self.grid[new_pos[0]][new_pos[1]] == 'X':
            self.grid[new_pos[0]][new_pos[1]] = 'X'
            self.position = new_pos
            return new_pos
        elif self.grid[new_pos[0]][new_pos[1]] == '#':
            self.direction = (self.direction + 1) % 4
            return j , i

    def count_xs(self):
        count = 0
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[i][j] == 'X':
                    count += 1
        return count

    def find_start(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] == "^":
                    return j, i