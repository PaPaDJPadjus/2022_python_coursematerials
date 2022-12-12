"""Naughty and nice list for santa."""

import csv


class NiceAndNaughtyList:
    """Hold a list of tuples of children on the nice and or naughty list."""
    def __init__(self):
        self.nice_dict = {}
        self.naughty_dict = {}
        self.nice_list_names = []
        self.naughty_list_names = []

    def names_from_csv_file_with_gifts(self, file_name, wish_list):
        """Get the names from the file and link them with the wanted gifts."""
        with open(file_name) as csv_file:
            if file_name == "ex15_nice_list.csv":
                csv_reader = csv.reader(csv_file, delimiter=",")
                for row in csv_reader:
                    self.nice_dict[row[0]] = row[1]
                    self.nice_list_names.append(row[0])
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                self.naughty_dict[row[0]] = row[1]
                self.naughty_list_names.append(row[0])

        with open(wish_list) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                gifts = []
                if row[0] in self.nice_list_names:
                    for gift in row[1::]:
                        gifts.append(gift)
                    location = self.nice_dict[row[0]]
                    self.nice_dict[row[0]] = [location]
                    self.nice_dict[row[0]] += gifts
                elif row[0] in self.naughty_list_names:
                    for gift in row[1::]:
                        gifts.append(gift)
                    location = self.naughty_dict[row[0]]
                    self.naughty_dict[row[0]] = [location]
                    self.naughty_dict[row[0]] += gifts
                else:
                    continue

        return self.naughty_dict


print(NiceAndNaughtyList().names_from_csv_file_with_gifts("ex15_naughty_list (1).csv", "ex15_wish_list.csv"))

