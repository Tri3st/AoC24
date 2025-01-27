from AoC.AoC24.day25.key_lock import KeyLock


class KeyLocks:
    def __init__(self, data):
        self.key_locks = []
        for data_block in data:
            d = KeyLock(data_block)
            self.key_locks.append(d)
        self.key_length = self.key_locks[0].key_length
        self.locks = []
        self.keys = []
        for k_l in self.key_locks:
            if k_l.get_type() == "LOCK":
                self.locks.append(k_l)
            else:
                self.keys.append(k_l)
        self.fits = self.check_fits()
        self.total_fits = [len([x for x in f if x]) == self.key_length for f in self.fits]
        print(len([x for x in self.total_fits if x == True]))

    def check_fits(self):
        res = []
        for k in self.keys:
            for l in self.locks:
                temp_res = [k + l <= self.key_length for k, l in zip(k.key_lock, l.key_lock)]
                res.append(temp_res)
        return res

    def __str__(self):
        res = ""
        for lock in self.key_locks:
            res += str(lock) + "\n"
        return res