"""Car inventory."""


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
    for el in cars:
        if el.split()[1] in model:
            continue
        else:
            full_model = el[1:3]
            model.append(str(full_model))
    return model


print(car_models("Tesla Model X"))
