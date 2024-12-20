from MyMods.Matrix import Matrix

from day14.robot import Robot


class RobotMap(Matrix):
    def __init__(self, dimj, dimi, data, cycles=1):
        super().__init__(dimj, dimi, '.')
        self.robots = []
        self.quadrants = {0: 0, 1: 0, 2: 0, 3: 0, 'total': 0}
        for line in data:
            self.robots.append(Robot(line))
        for robot in self.robots:
            self.adjust_map(robot)

        self.do_cycle(cycles)
        self.get_quadrant_scores()

    def do_cycle(self, nr_of_cycles=1):
        for cyc in range(nr_of_cycles):
            for robot in self.robots:
                robot.move(self.dimj, self.dimi)
                self.adjust_map(robot)
            if self.all_robots_1():
                print(self.__repr__())
                print(f"Cycle {cyc} ...")
                input("Press enter to continue ..")

    def adjust_map(self, robot):
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
        self.quadrants[0] = self._get_quadrant_score(0, 0, jline - 1 ,iline - 1)
        self.quadrants[1] = self._get_quadrant_score(0, self.dimi - iline, jline - 1, self.dimi - 1)
        self.quadrants[2] = self._get_quadrant_score(self.dimj - jline, 0, self.dimj - 1, iline - 1)
        self.quadrants[3] = self._get_quadrant_score(self.dimj - jline, self.dimi - iline, self.dimj - 1, self.dimi - 1)
        total = 1
        for k, v in self.quadrants.items():
            total *= v if k != 'total' else 1
        self.quadrants['total'] = total

    def _get_quadrant_score(self, jmin, imin, jmax, imax):
        score = 0
        for a in range(jmin, jmax + 1):
            for b in range(imin, imax + 1):
                if self.grid[a][b] != '.':
                    score += self.grid[a][b]
        return score

    def all_robots_1(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] != '.' and self.grid[j][i] > 1:
                    return False
        return True

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