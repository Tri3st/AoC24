"""Automated datafile reading"""
import os


def read_data(filename="", lines=0) -> list:
    """
        Read all the data from a given text file
        use the input or give a filename in the string.
        for all lines leave ommit lines (default = 0)
        Parameters:
            filename (str): the filename 'day1/day1.txt'
            lines (int): number of lines to take (default = 0 = ALL)
        Returns:
            data (list): a list with the data lines.
    """
    if not filename:
        filename = input("enter filename (day1/day1.txt) : ")
    first_x = lines
    data = []

    try:
        f = open(filename, "r")
        if first_x != 0:
            for i in range(int(first_x)):
                data.append(f.readline().strip())
        else:
            data = f.readlines()
            data = [d.strip() for d in data]
        f.close()
    except Exception as e:
        print("Oops. there was an error : %s" % e.__str__())

    return data
