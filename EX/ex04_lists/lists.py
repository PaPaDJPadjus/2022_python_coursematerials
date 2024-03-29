"""Car inventory.""""""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    if all_cars == "":
        return []
    cars_list = all_cars.split(",")
    return cars_list


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    names = []
    cars = list_of_cars(all_cars)
    for el in cars:
        if el.split()[0] in names:
            continue
        else:
            names.append(el.split()[0])
    return names


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    model = []
    cars = list_of_cars(all_cars)
    for car in cars:
        if len(car.split(" ", 1)) == 1:
            continue
        full_car = car.split(" ", 1)
        if full_car[1] in model:
            continue
        model.append(full_car[1])
    return model


def search_by_make(all_cars: str, maker: str):
    """Return list of cars and models."""
    cars_list = list_of_cars(all_cars)
    makes = []
    for el in cars_list:
        makes.append(el.split()[0])
    cars = []
    i = 0
    for car in cars_list:
        if maker.lower() == makes[i].lower():
            i += 1
            cars.append(car)
        else:
            i += 1
            continue
    return cars


def search_by_model(all_cars: str, model: str):
    """Search for model in all the cars."""
    cars_list = list_of_cars(all_cars)
    cars = []
    if len(model.split()) > 1:
        return []
    for car in cars_list:
        full_split = car.upper().split()
        if model.upper() == full_split[0]:
            continue
        if model.upper() in full_split:
            cars.append(car)
        else:
            continue
    return cars


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.

    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5"

    =>

    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    """
    car_list = list_of_cars(all_cars)
    cars = []
    models = []
    makes = car_makes(all_cars)
    full_car_list = []
    for car in car_list:
        car_plus_model = car.split(" ", 1)
        if car_plus_model[0] in cars:
            if car_plus_model[1] in models:
                continue
            spot = cars.index(car_plus_model[0]) + 1
            cars[spot].append(car_plus_model[1])
            models.append(car_plus_model[1])
        else:
            cars.append(car_plus_model[0])
            cars.append([car_plus_model[1]])
            models.append(car_plus_model[1])

    a = 0
    b = 1
    for i in range(len(makes)):
        full_car = [cars[a]] + [cars[b]]
        a += 2
        b += 2
        full_car_list.append(full_car)
    if all_cars == "":
        return []
    return full_car_list


def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    """
    data = []
    allcars = list_of_cars(all_cars)
    xtra_cars = []
    for i in range(len(car_list)):
        data.append(car_list[i][0])
    for el in allcars:
        car_split = el.split(" ", 1)
        if car_split[0] in data:
            i = data.index(car_split[0])
            if car_split[1] in car_list[i][1]:
                continue
            car_list[i][1].append(car_split[1])
        else:
            data.append(car_split[0])
            xtra_cars.append(car_split[0])
            xtra_cars.append([car_split[1]])
            car_list.append(xtra_cars)
            xtra_cars = []
    return car_list


def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.

    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.
    """
    if all_cars == " ":
        return []
    final_list = []
    makes = []
    car = []
    listoc = list_of_cars(all_cars)
    for el in listoc:
        name = el.split(" ", 1)
        makes.append(name[0])
    for el in makes:
        amount = makes.count(el)
        car.append(el)
        car.append(amount)
        if tuple(car) in final_list:
            car = []
            continue
        else:
            final_list.append(tuple(car))
            car = []
    return final_list


def car_list_as_string(cars: list):
    """
    Create a list of cars.

    The input list is in the same format as the result of car_make_and_models function.
    The order of the elements in the string is the same as in the list.
    [['Audi', ['A4']], ['Skoda', ['Superb']]] =>
    "Audi A4,Skoda Superb"
    """
    j = 0
    final = []
    output = ""
    for mark in cars:
        marks = cars[j][0]
        for el in cars[j][1]:
            car = marks + " " + el
            final.append(car)
        j += 1
    for el in final:
        output += el
        if final.index(el) != len(final) - 1:
            output += ","
    return output


print(car_list_as_string([['Audi', ['A4', "A6"]], ['Skoda', ['Superb']]]))  # "Audi A4,Skoda Superb"
