from MyMods.Matrix import Matrix


class FrequencyMap(Matrix):
    def __init__(self, data):
        super().__init__(len(data), len(data[0]), '.')
        self.add_lines(data)
        self.grids = {}  # {'A': [['.','.'],[]]}
        self.antennas = {}  # {'A': [(1,0),(2,3)]}
        self.total_antinodes = set()
        self.antinodes = {}  # {name: antinodes}
        self.get_antennas()
        # will become a loop, doing 1 for now
        # self.do_antennas("0")
        # self.print_grid(self.grids["0"])
        # self.do_antennas("A")
        # self.print_grid(self.grids["A"])
        for ant in self.antennas.keys():
            self.do_antennas(ant)

    def get_antennas(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] != '.':
                    if self.grid[j][i] in self.antennas.keys():
                        self.antennas[self.grid[j][i]].append((j, i))
                    else:
                        self.antennas[self.grid[j][i]] = [(j, i)]
        for ant in self.antennas.keys():
            self.grids[ant] = self.make_grid_copy(self.antennas[ant], ant)
            self.antinodes[ant] = 0

    def do_antennas(self, antenna):
        combinations = []
        for k in range(len(self.antennas[antenna])):
            for l in range(1, len(self.antennas[antenna])):
                # calc antinodes between two antennas
                if k != l and k < l:
                    combinations.append((k,l))
        for c in combinations:
            antenna1 = self.antennas[antenna][c[0]]
            antenna2 = self.antennas[antenna][c[1]]
            self.calculate_antinodes(antenna1, antenna2, antenna)

    def calculate_antinodes(self, antenna1, antenna2, name):
        print(antenna1, antenna2)
        d_j = antenna2[0] - antenna1[0]
        d_i = antenna2[1] - antenna1[1]
        x = 0
        while True:
            antinode1 = antenna1[0] - d_j * x, antenna1[1] - d_i * x
            print(antinode1)
            if not self.is_valid(antinode1[0], antinode1[1]):
                break
            self.grids[name][antinode1[0]][antinode1[1]] = '#'
            self.antinodes[name] += 1
            self.total_antinodes.add((antinode1[0], antinode1[1]))
            x += 1
        y = 0
        while True:
            antinode2 = antenna2[0] + d_j * y, antenna2[1] + d_i * y
            print(antinode2)
            if not self.is_valid(antinode2[0], antinode2[1]):
                break
            self.grids[name][antinode2[0]][antinode2[1]] = '#'
            self.antinodes[name] += 1
            self.total_antinodes.add((antinode2[0], antinode2[1]))
            y += 1

    def is_valid(self, j, i):
        return 0 <= j < self.dimj and 0 <= i < self.dimi

    def make_grid_copy(self, antenna, antenna_name):
        antenna_coords = antenna
        grid_copy = [[antenna_name if (j, i) in antenna else '.' for j in range(self.dimj)] for i in range(self.dimi)]
        for j in range(self.dimj):
            for i in range(self.dimi):
                if (j, i) in antenna_coords:
                    grid_copy[j][i] = antenna_name
                else:
                    grid_copy[j][i] = '.'
        return grid_copy

    def print_grid(self, grid):
        res = ""
        for row in grid:
            row_str = ""
            for cell in row:
                row_str += str(cell)
            res += row_str + "\n"
        print(res)