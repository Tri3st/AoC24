from MyMods.Matrix import Matrix

from AoC.AoC24.day14.robot import Robot


class RobotMap(Matrix):
    def __init__(self, data, cycles=1):
        super().__init__(7, 11, '.')
        self.robots = []
        for line in data:
            self.robots.append(Robot(line))
        for robot in self.robots:
            self.adjust_map(robot)
        print(self.__repr__())
        self.do_cycle(cycles)

    def do_cycle(self, nr_of_cycles=1):
        for _ in range(nr_of_cycles):
            for robot in self.robots:
                robot.move(self.dimj, self.dimi)
                self.adjust_map(robot)

    def adjust_map(self, robot):
        print("old_coords", robot.old_point)
        print("new_coords", robot.point)
        self.add_robot(robot.point)
        if robot.old_point is not None:
            self.remove_old_robot(robot.old_point)

    def add_robot(self, point):
        self.grid[point[0]][point[1]] = 1 if self.grid[point[0]][point[1]] == '.'  else self.grid[point[0]][point[1]] + 1

    def remove_old_robot(self, old_point):
        self.grid[old_point[0]][old_point[1]] = '.' if self.grid[old_point[0]][old_point[1]] == 1 else self.grid[old_point[0]][old_point[1]] - 1

    def get_quadrant_scores(self):
        jline = self.dimj // 2
        iline = self.dimi // 2

    def get_quadrant_score(self, jmin, jmax, imin, imax):
        score = 0
        for a in range(jmin, jmax + 1):
            for b in range(imin, imax + 1):
                if self.grid[a][b] != '#':
                    score += self.grid[a][b]


    def __str__(self):
        res = ""
        for robot in self.robots:
            res += f"{robot} "
        return res

    def __repr__(self):
        res = ""
        for row in self.grid:
            res += f"{"".join([str(x) for x in row])}\n"
        return res