"""Automated datafile reading"""
import os


def read_data(filename="", lines=0, mode=0) -> list:
    """
        Read all the data from a given text file
        use the input or give a filename in the string.
        for all lines leave ommit lines (default = 0)
        Parameters:
            filename (str): the filename 'day1/day1.txt'
            lines (int): number of lines to take (default = 0 = ALL)
            mode (int): 0 = give the file as lines, 1 = give the file as a whole (default = 0)
        Returns:
            data (list): a list with the data lines.
    """
    if not filename:
        filename = input("enter filename (day1/day1.txt) : ")
    first_x = lines
    data = []
    data_whole = None
    try:
        f = open(filename, "r")
        if mode == 0:
            if first_x != 0:
                for i in range(int(first_x)):
                    data.append(f.readline().strip())
            else:
                data = f.readlines()
                data = [d.strip() for d in data]
        else:
            data_whole = f.read()
        f.close()
    except Exception as e:
        print("Oops. there was an error : %s" % e.__str__())

    return data if mode == 0 else data_whole
