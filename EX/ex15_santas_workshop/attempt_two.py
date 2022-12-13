"""Santas helper."""

import csv
import requests


class NeededLists:
    """Hold all the needed lists."""
    def __init__(self):
        """Lists that I need."""
        self.all_names = []
        self.children = []
        self.naughty_kids_in_tuples = []


class Child(NeededLists):
    """Child class, that holds its info."""
    def __init__(self):
        super().__init__()
        self.name = ""
        self.country = ""
        self.behaviour = ""
        self.wishes = []

    def __repr__(self):
        """Show me urself."""
        return f"{self.behaviour} {self.name}, from {self.country} wants {self.wishes}"

    def info_from_csv_files(self, nice_list: str, naughty_list: str, wish_list: str):
        """Get the names from the file and link them with the wanted gifts."""
        with open(naughty_list) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            for row in csv_reader:
                child_from_list = Child()
                child_from_list.name = row[0]
                child_from_list.country = row[1]
                child_from_list.behaviour = "Naughty"
                self.children.append(child_from_list)
                self.all_names.append(child_from_list.name)
                self.naughty_kids_in_tuples.append((child_from_list.name, child_from_list.country))

        with open(nice_list) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            for row in csv_reader:
                if (row[0], row[1]) in self.naughty_kids_in_tuples:
                    continue
                child_from_list = Child()
                child_from_list.name = row[0]
                child_from_list.country = row[1]
                child_from_list.behaviour = "Nice"
                self.children.append(child_from_list)
                self.all_names.append(child_from_list.name)

        with open(wish_list) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:

                for child in self.children:
                    if row[0] == child.name:
                        for gift in row[1::]:
                            child.wishes.append(gift)
                    else:
                        continue

        return [self.children]


class GiftDatabase(NeededLists):
    """Store info bout gifts."""

    def __init__(self):
        super().__init__()
        self.url = "https://cs.ttu.ee/services/xmas/gift?name="
        self.gifts = {}
        self.gifts_list = []

    def __get_gift_from_api(self, name):
        """Api request."""
        url = self.url + name
        response = requests.get(url)
        self.gifts[name] = response.json()

        return self.gifts[name]

    def get_gift(self, name):
        """Get the gift """
        if name in self.gifts:
            return self.gifts[name]

        return self.__get_gift_from_api(name)

    def get_needed_gifts_for_children(self):
        """Get the first item on the nice kids lists info, to add to list of gifts to give."""
        coal_counter = 0

        for child in self.children:

            if child.behaviour == "Nice":
                for gift in child.wishes:
                    self.gifts_list.append(gift)

            else:
                coal_counter += 1
        self.gifts_list.append(f"{coal_counter} pieces of coal")

        return self.gifts_list


if __name__ == '__main__':

    print(Child().info_from_csv_files("nice_list_same_name.csv", "naughty_list_same_name.csv", "wish_list_same_names.csv"))
    print(GiftDatabase().get_needed_gifts_for_children())
