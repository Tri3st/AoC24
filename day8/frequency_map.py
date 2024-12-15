from MyMods.Matrix import Matrix


class FrequencyMap(Matrix):
    def __init__(self, data):
        super().__init__(len(data), len(data[0]), '.')
        self.add_lines(data)
        self.grids = {}
        self.antennas = {'A': []}
        self.antinodes = {}  # {name: antinodes}
        self.get_antennas()
        # will become a loop, doing 1 for now
        self.do_antennas("0")
        self.do_antennas("A")

    def get_antennas(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] != '.':
                    if self.grid[j][i] in self.antennas.keys():
                        self.antennas[self.grid[j][i]].append((j, i))
                    else:
                        self.antennas[self.grid[j][i]] = [(j, i)]
        for ant in self.antennas.keys():
            self.grids[ant] = self.grid.copy()
            self.antinodes[ant] = 0

    def do_antennas(self, antenna):
        for j in range(self.dimj):
            row = ""
            for i in range(self.dimi):
                row += self.grid[j][i]
            print(rowgit)
        combinations = []
        for k in range(len(self.antennas[antenna])):
            for l in range(1, len(self.antennas[antenna])):
                # calc antinodes between two antennas
                if k != l and k < l:
                    print(f"combination {antenna}[{k},{l}]")
                    combinations.append((k,l))
        for c in combinations:
            antenna1 = self.antennas[antenna][c[0]]
            antenna2 = self.antennas[antenna][c[1]]
            self.calculate_antinodes(antenna1, antenna2, antenna)

    def calculate_antinodes(self, antenna1, antenna2, name):
        print(antenna1, antenna2)
        d_j = antenna2[0] - antenna1[0]
        d_i = antenna2[1] - antenna1[1]
        antinode1 = antenna1[0] - d_j, antenna1[1] - d_i
        antinode2 = antenna2[0] + d_j, antenna2[1] + d_i
        if self.is_valid(antinode1[0], antinode2[0]):
            print(antinode1)
            self.grids[name][antinode1[0]][antinode1[1]] = '#'
            self.antinodes[name] += 1
        if self.is_valid(antinode2[0], antinode1[1]):
            print(antinode2)
            self.grids[name][antinode2[0]][antinode2[1]] = '#'
            self.antinodes[name] += 1

    def is_valid(self, j, i):
        return 0 <= j < self.dimj and 0 <= i < self.dimi