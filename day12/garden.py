from collections import deque

from AoC.AoC24.MyMods.Matrix import Matrix
from day12.plot import Plot


class Garden(Matrix):
    def __init__(self, datalines):
        super().__init__(len(datalines), len(datalines[0]), '.')
        self.add_lines(datalines)
        self.plots = []
        self.visited = set()
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        self.total_price = 0
        self.calc()

    def is_valid(self, j, i):
        # Check if the position is within bounds
        return 0 <= j < self.dimj and 0 <= i < self.dimi

    def bfs(self, j, i):
        """Performs BFS to calculate the area and perimeter of a region."""
        queue = deque([(j, i)])
        self.visited.add((j, i))
        region_char = self.grid[j][i]
        area = 0
        perimeter = 0

        while queue:
            cj, ci = queue.popleft()
            area += 1
            # Check all 4 directions
            for dj, di in self.directions:
                nj, ni = cj + dj, ci + di

                if self.is_valid(nj, ni):
                    if self.grid[nj][ni] == region_char and (nj, ni) not in self.visited:
                        self.visited.add((nj, ni))
                        queue.append((nj, ni))
                    elif self.grid[nj][ni] != region_char:
                        perimeter += 1
                else:
                    # Out of bounds contributes to perimeter
                    perimeter += 1

        return area, perimeter

    def seek_plots(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                plot = self.grid[j][i]
                print(plot)
                if plot in [n.name for n in self.plots]:
                    [p for p in self.plots if p.name == plot][0].add_plant((j,i))
                else:
                    new_p = Plot(plot, (j,i))
                    self.plots.append(new_p)

    def calc(self):
        for i in range(self.dimi):
            for j in range(self.dimj):
                if (i, j) not in self.visited:
                    # Calculate area and perimeter for each region
                    area, sides = self.bfs2(i, j)
                    print(f"plant: {self.grid[j][i]}, area: {area}, sides: {sides}")
                    self.total_price += area * sides

    def bfs2(self, j, i):
        """Performs BFS to calculate the area and sides of a region."""
        queue = deque([(j, i)])
        self.visited.add((j, i))
        region_char = self.grid[j][i]
        area = 0
        sides = 0

        while queue:
            cj, ci = queue.popleft()
            area += 1

            # Check all 4 directions
            for dj, di in self.directions:
                nj, ni = cj + di, cj + di

                if self.is_valid(nj, ni) and self.grid[nj][ni] == region_char:
                    sides += 1
                    if (nj, ni) not in self.visited:
                        self.visited.add((nj, ni))
                        queue.append((nj, ni))

        total_sides = 4 * area - sides  # Calculate total sides based on connections
        return area, total_sides