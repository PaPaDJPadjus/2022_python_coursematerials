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


def find_two_people_with_most_common_hobbies(data: str):
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
    names_n_hobbies = create_dictionary(data)
    keys = []
    first = []
    second = []
    results = []
    commons = []
    i = 0
    j = 1
    a = 0
    for key in names_n_hobbies.keys():
        keys.append(key)
    if 1 >= len(keys):
        return None
    for i in range(len(names_n_hobbies)):
        for el in names_n_hobbies[keys[i]]:
            first.append(el)
        second.append(set(first))
        first = []
        i += 1

    for el in second:
        for a in range(len(second) - 1):
            intersect = second[j].intersection(el)
            if el == intersect:
                index_one = second.index(el) - 1
                names = [keys[index_one]]
                if len(names) == 2:
                    return tuple(names)
            symmetric = second[j].symmetric_difference(el)
            if len(symmetric) == 0 and len(intersect) >= 1:
                div_zero = [keys[j - 1], keys[j]]
                return tuple(div_zero)
            commons.append(len(intersect))
            ratio = len(intersect) / len(symmetric)
            results.append(ratio)
            j += 1
            a += 1
        a = 0
        j = 0

    if results.count(max(results)) > 1:
        com_max = commons.index(max(commons))
        final_result = keys[com_max], keys[com_max + 1]
    else:
        maximum_index = results.index(int(max(results)))
        final_result = [keys[maximum_index], keys[maximum_index + 1]]

    return tuple(final_result)


#  print(find_two_people_with_most_common_hobbies("John:running\nJohn:walking\nMary:dancing\nMary:running\nNora:running\nNora:singing\nNora:dancing"))  # ('Mary', 'Nora')
#  print(find_two_people_with_most_common_hobbies("name8:hobby1\nname13:hobby6\nname3:hobby1\nname10:hobby9\nname2:hobby9\nname14:hobby5\nname12:hobby0\nname5:hobby6\nname8:hobby4\nname11:hobby2"))      # [{'name5', 'name13'}, {'name10', 'name2'}, {'name10', 'name2'}, {'name5', 'name13'}]
print(find_two_people_with_most_common_hobbies("name3:hobby10\nname3:hobby11\nname0:hobby1\nname10:hobby8\nname10:hobby0\nname2:hobby1\nname12:hobby8\nname1:hobby5\nname1:hobby5\nname8:hobby8"))      # [{'name2', 'name0'}, {'name2', 'name0'}, {'name8', 'name12'}, {'name8', 'name12'}]
print(find_two_people_with_most_common_hobbies("name12:hobby3\nname11:hobby1\nname9:hobby6\nname1:hobby3\nname12:hobby5\nname3:hobby0\nname7:hobby5\nname0:hobby6\nname8:hobby3\nname9:hobby6\nname11:hobby3\nname8:hobby0\nname11:hobby1\nname3:hobby3"))      # [{'name8', 'name3'}, {'name8', 'name3'}]
print(find_two_people_with_most_common_hobbies("name0:hobby8\nname2:hobby1\nname2:hobby2\nname4:hobby10\nname0:hobby9\nname1:hobby4\nname0:hobby4\nname0:hobby6\nname2:hobby2\nname4:hobby2"))      # [{'name2', 'name4'}, {'name2', 'name4'}]
print(find_two_people_with_most_common_hobbies("name0:hobby1\nname2:hobby5\nname2:hobby6\nname2:hobby5\nname5:hobby3\nname5:hobby4\nname0:hobby5\nname2:hobby6\nname5:hobby1\nname5:hobby1\nname4:hobby1"))     # [{'name0', 'name4'}, {'name0', 'name4'}]
print(find_two_people_with_most_common_hobbies("name5:hobby2\nname0:hobby0\nname4:hobby9\nname4:hobby10\nname5:hobby10\nname2:hobby2\nname3:hobby0\nname4:hobby2\nname2:hobby0\nname4:hobby5\nname5:hobby2\nname2:hobby10"))        #[{'name0', 'name3'}, {'name0', 'name3'}]
print(find_two_people_with_most_common_hobbies("name4:hobby0\nname2:hobby2\nname1:hobby2\nname5:hobby2\nname3:hobby1\nname1:hobby5\nname2:hobby1\nname0:hobby4\nname3:hobby3\nname4:hobby0"))       # [{'name5', 'name2'}, {'name5', 'name1'}, {'name5', 'name2'}, {'name5', 'name1'}]
print(find_two_people_with_most_common_hobbies("name9:hobby3\nname9:hobby4name7:hobby6\nname9:hobby10\nname12:hobby9\nname13:hobby9\nname7:hobby8\nname8:hobby3\nname0:hobby3\nname8:hobby4"))      # [{'name13', 'name12'}, {'name13', 'name12'}]
print(find_two_people_with_most_common_hobbies("name3:hobby3\nname9:hobby4\nname13:hobby7\nname5:hobby6\nname4:hobby6\nname4:hobby5\nname9:hobby0\nname0:hobby2\nname10:hobby6\nname3:hobby7"))     # [{'name10', 'name5'}, {'name10', 'name5'}]
print(find_two_people_with_most_common_hobbies("name3:hobby0\nname5:hobby4\nname3:hobby0\nname4:hobby8\nname3:hobby4\nname3:hobby9\nname4:hobby6\nname3:hobby3\nname5:hobby7\nname0:hobby10\nname1:hobby3"))        # [{'name1', 'name3'}, {'name1', 'name3'}]
print(find_two_people_with_most_common_hobbies("name3:hobby4\nname1:hobby1\nname5:hobby0\nname5:hobby2\nname5:hobby4\nname4:hobby0\nname6:hobby0\nname3:hobby1\nname3:hobby1\nname7:hobby2\nname3:hobby3\nname3:hobby3\nname6:hobby0\nname7:hobby0\nname7:hobby1\nname1:hobby0"))       # [{'name4', 'name6'}, {'name4', 'name6'}]