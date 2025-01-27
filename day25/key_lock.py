class KeyLock:
    def __init__(self, data):
        self.data = [l for l in data.split("\n")]
        self.key_length = len(self.data[0])
        self.key_lock = self.calc()
        self.type = "LOCK" if self.data[0] == '#####' else "KEY"  # 'key' or 'lock'
        print("type: ", self.type)

    def get_type(self):
        return self.type

    def calc(self):
        ss = {0 : 0, 1: 0, 2: 0, 3: 0, 4: 0}
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] == '#':
                    ss[j] += 1
        return [(v - 1) for k,v in ss.items()]

    def __str__(self):
        return f"{self.type}: {str(self.key_lock)}"