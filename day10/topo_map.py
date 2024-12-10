from MyMods.Matrix import Matrix


class TopoMap(Matrix):
    """
    Topo Map
    Make sure to give the data in a list of lines.
    """
    def __init__(self, data):
        super().__init__(len(data), len(data[0]), base='.')
        self.add_lines(data)
        self.start = []
        self.routes = []
        self._get_start_coords()
        print("start coords : ", self.start)
        # for (j, i, _) in self.start:
        #     self.calc_routes(j, i)
        self.calc_routes(0, 2)


    def _get_start_coords(self):
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] == '0':
                    self.start.append((j, i, self.grid[j][i]))
        
    def calc_routes(self, j, i):
        neigs = self.seek_neighbors(j, i)
        print("neigbors : ", neigs)
        if neigs is not None:
            for neig in neigs:
                self.routes.append((j, i, self.grid[j][i]))
                if self.grid[j][i] == '9':
                    return True
                ns = self.seek_neighbors(j, i)
                for n in ns:
                    self.routes.append((j, i, self.grid[j][i]))
        

    def seek_neighbors(self, j, i):
        results = []
        curr = int(self.grid[j][i])
        next = str(curr + 1)
        print("seek_nighbors with j=", j, " and i=", i, " and value ", curr)
        if j >= 0 and i >= 0 and self.grid[j-1][i-1] == next:
            print(f"found nighbor at {j-1}, {i-1} with value {next}")
            results.append((j-1, i-1, next))
        if j >= 0 and self.grid[j-1][i] == next:
            print(f"found nighbor at {j-1}, {i} with value {next}")
            results.append((j-1, i, next))
        if j >= 0 and i <= self.dimi - 1 and self.grid[j-1][i+1] == next:
            print(f"found nighbor at {j-1}, {i+1} with value {next}")
            results.append((j-1, i+1, next))
        if i >= 0 and self.grid[j][i-1] == next:
            print(f"found nighbor at {j}, {i-1} with value {next}")
            results.append((j, i-1, next))
        if i <= self.dimi - 1 and self.grid[j][i+1] == next:
            print(f"found nighbor at {j}, {i+1} with value {next}")
            results.append((j, i+1, next))
        if j <= self.dimj - 1 and i >= 0 and self.grid[j+1][i-1] == next:
            print(f"found nighbor at {j+1}, {i-1} with value {next}")
            results.append((j+1, i-1, next))
        if j <= self.dimj - 1 and self.grid[j+1][i] == next:
            print(f"found nighbor at {j+1}, {i} with value {next}")
            results.append((j+1, i, next))
        if j <= self.dimj - 1 and i <= self.dimi - 1 and self.grid[j+1][i+1] == next:
            print(f"found nighbor at {j+1}, {i+1} with value {next}")
            results.append((j+1, i+1, next))
        return results
        
