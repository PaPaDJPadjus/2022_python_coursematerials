"""Files ;(."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    f = open(filename, "r")
    output = f.read()
    f.close()
    return output


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    f = open(filename, "r")
    output = []
    for line in f:
        if line.endswith("\n") is True:
            output.append(line.strip("\n"))
        else:
            output.append(line)
    f.close()
    return output


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    lists = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            lists.append(row)
    return lists


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    f = open(filename, "w")
    f.write(contents)
    f.close()
    return


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    f = open(filename, "w")
    i = 0
    for line in lines:
        length = len(lines) - 1
        if i == length:
            f.write(line)
        else:
            f.write(line + "\n")
            i += 1
    f.close()
    return


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        for row in data:
            csv_writer.writerow(row)
    return


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str):
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    list_of_stuff = []
    list_list = []
    names = []
    dates_f = open(dates_filename, "r")
    for line in dates_f:
        line = line.split(":")
        list_list.append(line[0])
        names.append(line[0])
        list_list.append("-")
        if line[1].endswith("\n") is True:
            list_list.append(line[1].strip("\n"))
            list_of_stuff.append(list_list)
            list_list = []
        else:
            list_list.append(line[1])
            list_of_stuff.append(list_list)
            list_list = []

    towns_f = open(towns_filename, "r")
    for line in towns_f:
        line = line.split(":")
        for i in range(len(list_of_stuff)):
            if line[0] in list_of_stuff[i]:
                list_of_stuff[i][1] = str(line[1].strip("\n"))
            elif line[0] not in names:
                names.append(line[0])
                list_list.append(line[0])
                if line[1].endswith("\n") is True:
                    list_list.append(line[1].strip("\n"))
                list_list.append("-")
                list_of_stuff.append(list_list)
                list_list = []

    with open(csv_output_filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["name", "town", "date"])
        for row in list_of_stuff:
            csv_writer.writerow(row)
    return


def read_csv_file_into_list_of_dicts(filename: str):
    """
    Read csv file into list of dictionaries.

    Header line will be used for dict keys.
    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:
    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    final = []
    diction = {}
    i = 0
    columns = []
    counter = 0
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if i == 0:
                for el in row:
                    diction[el] = "-"
                    columns.append(el)
            if i >= 1:
                while len(row) > counter:
                    for info in row:
                        diction[columns[counter]] = info
                        counter += 1
                final.append(diction)
                diction = {}
            i += 1
            counter = 0
    return final


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    keys = []
    rows = []
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        if [] in data:
            csv_writer.write("")
            return
        for dicts in data:
            keys = dicts.keys()
        csv_writer.writerow(keys)
        for dicts in data:
            for key in keys:
                value = dicts[key]
                rows.append(value)
            csv_writer.writerow(rows)
            rows = []
    return
