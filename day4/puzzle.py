from MyMods.Matrix import Matrix


class Puzzle(Matrix):
    def __init__(self, data):
        super().__init__(len(data), len(data[0]), '.')
        self.dimj = len(data)
        self.dimi = len(data[0])
        self.add_lines(data)
        self.word_count = 0
        self.search_word()
        self.word_count2 = 0
        self.search_word2()

    def search_word(self):
        # search every line
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] == 'X':
                    # Found start letter
                    # check hor going right
                    if i + 4 <= self.dimi and self.grid[j][i + 1] == 'M' and self.grid[j][i + 2] == 'A'and self.grid[j][i + 3] == 'S':
                        self.word_count += 1
                    # check hor going left
                    if i >= 3 and self.grid[j][i - 1] == 'M' and self.grid[j][i - 2] == 'A'and self.grid[j][i - 3] == 'S':
                        self.word_count += 1
                    # check vert going down
                    if j + 4 <= self.dimj and self.grid[j + 1][i] == 'M' and self.grid[j + 2][i] == 'A'and self.grid[j + 3][i] == 'S':
                        self.word_count += 1
                    # check vert going up
                    if j >= 3 and self.grid[j - 1][i] == 'M' and self.grid[j - 2][i] == 'A' and self.grid[j - 3][i] == 'S':
                        self.word_count += 1
                    # check diag going down right
                    if i + 4 <= self.dimi and j + 4 <= self.dimj and self.grid[j + 1][i + 1] == 'M' and \
                            self.grid[j + 2][i + 2] == 'A' and self.grid[j + 3][i + 3] == 'S':
                        self.word_count += 1
                    # check diag going down left
                    if i >= 3 and j + 4 <= self.dimj and self.grid[j + 1][i - 1] == 'M' and \
                            self.grid[j + 2][i - 2] == 'A' and self.grid[j + 3][i - 3] == 'S':
                        self.word_count += 1
                    # check diag going up right
                    print(i, j)
                    if i + 4 <= self.dimi and j >= 3 and self.grid[j - 1][i + 1] == 'M' and \
                            self.grid[j - 2][i + 2] == 'A' and self.grid[j - 3][i + 3] == 'S':
                        self.word_count += 1
                    # check diag going up left
                    if i >= 3 and j >= 3 and self.grid[j - 1][i - 1] == 'M' and \
                            self.grid[j - 2][i - 2] == 'A' and self.grid[j - 3][i - 3] == 'S':
                        self.word_count += 1

    def search_word2(self):
        # Possible patterns
        # 1: M M 2: M S 3: S M 4: S S
        #     A      A      A      A
        #    S S    M S    S M    M M
        # search every line for the A
        for j in range(self.dimj):
            for i in range(self.dimi):
                if self.grid[j][i] == 'A':
                    # Found the letter
                    # always check if the 4 corners are in the puzzle
                    if j - 1 >= 0 and i - 1 >= 0 and j + 1 <= self.dimj - 1 and i + 1 <= self.dimi - 1:
                        # Check corners for pattern 1
                        if self.grid[j - 1][i - 1] == 'M' and self.grid[j - 1][i + 1] == 'M' and self.grid[j + 1][i - 1] == 'S' \
                            and self.grid[j + 1][i + 1] == 'S':
                            self.word_count2 += 1
                        # Check corners for pattern 1
                        if self.grid[j - 1][i - 1] == 'M' and self.grid[j - 1][i + 1] == 'S' and self.grid[j + 1][
                            i - 1] == 'M' and self.grid[j + 1][i + 1] == 'S':
                            self.word_count2 += 1
                        # Check corners for pattern 1
                        if self.grid[j - 1][i - 1] == 'S' and self.grid[j - 1][i + 1] == 'M' and self.grid[j + 1][
                            i - 1] == 'S' and self.grid[j + 1][i + 1] == 'M':
                            self.word_count2 += 1
                        # Check corners for pattern 1
                        if self.grid[j - 1][i - 1] == 'S' and self.grid[j - 1][i + 1] == 'S' and self.grid[j + 1][
                            i - 1] == 'M' and self.grid[j + 1][i + 1] == 'M':
                            self.word_count2 += 1