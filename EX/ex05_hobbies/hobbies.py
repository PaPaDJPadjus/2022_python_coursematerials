"""EX05 - Hobbies."""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    name_and_hobby = data.split("\n")
    dictionary = {}
    for el in name_and_hobby:
        hobbies = []
        name = el.split(":")

        for person in name_and_hobby:
            name_two = person.split(":")
            if name[0] == name_two[0]:
                if name_two[1] in hobbies:
                    continue
                hobbies += [name_two[1]]
        dictionary[name[0]] = hobbies

    return dictionary


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    names_keys = dic.keys()
    for key in names_keys:
        dic[key].sort()
    return dic


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    name_and_hobby = data.split("\n")
    dictionary = {}
    for el in name_and_hobby:
        names = []
        name = el.split(":")
        for person in name_and_hobby:
            name_two = person.split(":")
            if name[1] == name_two[1]:
                if name_two[0] in names:
                    continue
                names += [name_two[0]]
        dictionary[name[1]] = names
    sort_dictionary(dictionary)
    return dictionary


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have the most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    dictionary = create_dictionary(data)
    names_keys = dictionary.keys()
    all_names = []
    final = []
    lengths = []
    i = 0
    for key in names_keys:
        all_names.append(key)
        length = len(dictionary[key])
        lengths.append(length)
    max_len = max(lengths)
    for el in lengths:
        if el == max_len:
            final.append(all_names[i])
        i += 1

    return sorted(final)


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    dictionary = create_dictionary_with_hobbies(data)
    names_keys = dictionary.keys()
    all_hobbies = []
    final = []
    lengths = []
    i = 0
    for key in names_keys:
        all_hobbies.append(key)
        length = len(dictionary[key])
        lengths.append(length)
    min_len = min(lengths)
    for el in lengths:
        if el == min_len:
            final.append(all_hobbies[i])
        i += 1

    return sorted(final)


def sort_names_and_hobbies(data: str):
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    name_and_hobby = data.split("\n")
    list_names = []
    tuple_list = []
    for el in name_and_hobby:
        hobbies = []
        name = el.split(":")
        if name[0] in list_names:
            continue
        for person in name_and_hobby:
            name_two = person.split(":")
            if name_two[0] in list_names:
                continue

            if name[0] == name_two[0]:
                if name_two[1] in hobbies:
                    continue
                hobbies += [name_two[1]]
        list_names.append(name[0])
        hobbies.sort()
        tuple_hob = tuple(hobbies)
        tuple_nam = (name[0], tuple_hob)
        tuple_list.append(tuple_nam)
    tuple_list.sort()
    return tuple(tuple_list)


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    r"""
    Find all the different people with certain hobbies.

    It is recommended to use set here.

    Example:
        data="John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting"
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    dic = create_dictionary_with_hobbies(data)
    keys = []
    people = []
    for key in dic.keys():
        keys.append(key)
    for el in hobbies:
        for key in keys:
            if el == key:
                for peeps in dic[key]:
                    people.append(peeps)
    return set(people)


def find_two_people_with_most_common_hobbies(data: str) -> tuple:
    """
    Find a pair of people who have the highest ratio of common hobbies to different hobbies.

    Common hobbies are the ones which both people have.
    Different hobbies are the ones, which only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies, ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair (and in which order) is returned.

    If there are less than 2 people in the input, return None.
    """
    return ()


if __name__ == '__main__':
    sample_data = """Jack:painting\nPeter:painting\nJack:running\nMary:running\nSmith:walking"""
    print(find_people_with_hobbies(sample_data, ["running", "painting"]))
    print(find_people_with_hobbies(
        "John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting",
        ["running", "dancing"]
    ))  # {"John", "Mary", "Jack"}

    sample_data = """John:running\nJohn:walking\nMary:dancing\nMary:running\nNora:running\nNora:singing\nNora:dancing"""
    print(find_two_people_with_most_common_hobbies(sample_data))  # ('Mary', 'Nora')
