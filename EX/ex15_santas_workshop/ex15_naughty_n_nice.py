"""Naughty and nice list for santa."""

import csv


class NiceAndNaughtyList:
    """Hold a list of tuples of children on the nice and or naughty list."""
    def __init__(self):
        self.nice_list = []
        self.naughty_list = []

    def names_from_csv_file(self, file_name):
        """Get the names from the file."""
        with open(file_name) as csv_file:
            if file_name == "ex15_nice_list.csv":
                csv_reader = csv.reader(csv_file, delimiter=",")
                for row in csv_reader:
                    self.nice_list.append((row[0], row[1]))
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                self.naughty_list.append((row[0], row[1]))


print(NiceAndNaughtyList().names_from_csv_file("ex15_naughty_list (1).csv"))
