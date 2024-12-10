from MyMods.Matrix import Matrix


class FrequencyMap(Matrix):
    def __init__(self, data):
        super().__init__(len(data), len(data[0]), '.')
        self.add_lines(data)
        self.antennas = {'A': []}
        self.get_antennas()
        # will become a loop, doing 1 for now
        self.do_antennas("0")

    def get_antennas(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] != '.':
                    if self.grid[j][i] in self.antennas.keys():
                        self.antennas[self.grid[j][i]].append((j, i))
                    else:
                        self.antennas[self.grid[j][i]] = [(j, i)]

    def do_antennas(self, antenna):
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
            self.calculate_antinodes(antenna1, antenna2)

    def calculate_antinodes(self, antenna1, antenna2):
        print(antenna1, antenna2)
        d_j = abs(antenna1[0] - antenna2[0])
        d_i = abs(antenna1[1] - antenna2[1])
        antinode1 = (antenna1[0] + d_j, antenna1[1] + d_i)
        if 0 <= antinode1[0] <= self.dimj - 1 and 0 <= antinode1[1] <= self.dimi - 1:
            print(antenna1[0], antenna1[1])
