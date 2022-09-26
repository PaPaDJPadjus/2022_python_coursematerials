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

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    """
    car_list = list_of_cars(all_cars)
    i = 0
    cars = []
    models = []
    all_models = []
    for car in car_list:
        car_plus_model = car.split(" ", 1)
        for el in car_plus_model:
            if el in cars:
                index = car.index(el)
                i = 2
            if el.upper() in cars or el.lower() in cars or el.capitalize() in cars:
                continue
            if i == 2:
                model = models.append(el)
                cars.insert(index, model)
                i = 0
            if i == 0:
                cars.append(el)
                i = 1
            else:
                if el.upper() in all_models or el.lower() in all_models or el.capitalize() in all_models:
                    i = 0
                    continue
                if i == 1:
                    models.append(el)
                    all_models.append(el)
                    cars.append(models)
                    i = 0
                else:
                    i = 1
    return [cars]

print(car_make_and_models("Skoda Super,Skoda Octavia,BMW 530,Skoda Superb,Skoda Superb,BMW x5"))
#  print(car_make_and_models("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5,audi a4"))


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
    return []
