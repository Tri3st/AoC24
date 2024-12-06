""" Matrix Class = for use with matrixes or grids.
use dimj -> dimensions rows
    dimi -> dimensions columns """


class Matrix:
    """
       Matrix class. makes a matrix with dimi colums and dimj rows
       Has an add_lines method, with which we can add data to the matrix.
    """
    def __init__(self, dimj, dimi, base=0):
        self.dimj = dimj
        self.dimi = dimi
        self.grid = [[base for i in range(dimi)] for j in range(dimj)]

    def add_lines(self, lines):
        """
           Adds multiple lines lines to the matrix
        """
        for (j, line) in enumerate(lines):
            for i in range(self.dimi):
                self.grid[j][i] = line[i]

    def __str__(self):
        """
           Returns a string representation of the matrix
        """
        t = ""
        for j in range(self.dimj):
            for i in range(self.dimi):
                t += str(self.grid[j][i])
            t += "\n"
        return t
