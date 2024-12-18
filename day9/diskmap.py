class Diskmap:
    def __init__(self):
        """
        Initializes the Diskmap instance by parsing the input map.
        :param input_map: String representing the disk layout.
        """
        self.diskmap = []
        self.type = "value"  # or "free"
        self.idx = 0
        self.count_empty = 0

    def new_num(self, n):
        if self.type == "value":
            self.diskmap.extend([self.idx for _ in range(n)])
            self.idx += 1
        else:
            self.diskmap.extend(["." for _ in range(n)])
        self.type = "value" if self.type == "free" else "free"
        self.count_empty = len([d for d  in self.diskmap if d == '.'])

    def calc(self):
        self.count_empty = len([x for x in self.diskmap if x == "."])
        self.fill_empty()

    def fill_empty(self):
        while not self.is_finished():
            # find first index of empty
            e = self._find_first_empty()
            # find last index of filled
            l = self._find_last_filled()
            self._swap(e, l)
            print(self.diskmap)

    def fill_empty2(self):
        pass

    def find_block_last_block(self):
        pass

    def _find_first_empty(self):
        idx = -1
        for i, d in enumerate(self.diskmap):
            if d == '.':
                return i

    def _find_last_filled(self):
        idx = -1
        for i in range(len(self.diskmap) - 1, -1 , -1):
            if self.diskmap[i] != '.':
                return i

    def _swap(self, x1, x2):
        temp = self.diskmap[x1]
        self.diskmap[x1] = self.diskmap[x2]
        self.diskmap[x2] = temp

    def calc_sum(self):
        return sum([i * d for i,d in enumerate(self.diskmap) if d != '.'])

    def is_finished(self):
        return self.diskmap[len(self.diskmap) - self.count_empty:] == [x for x in self.diskmap if x == '.']


    def __str__(self):
        """
        Returns a string representation of the diskmap.
        """
        return f"{self.diskmap} - empty {self.count_empty} - total {self.calc_sum()}"
