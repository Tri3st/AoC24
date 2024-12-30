from day23.lanconn import LanConn


class LanPlan:
    def __init__(self,data):
        self.connections = []
        self.triplets = []
        for d in data:
            d2 = d.split("-")
            self.connections.append(LanConn(d2[0], d2[1]))
        print(self.connections)
        self.calc_triplets()

    def calc_triplets(self):
        length = len(self.connections)
        conns, trips, results = [], [], []
        for i in range(length):
            node = self.connections[i]
            print(f"{i} {self.connections[i]}")
            conns = [c for c in self.connections if c.name == node.conn]
            


