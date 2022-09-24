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
    full_model = ""
    cars = list_of_cars(all_cars)
    for car in cars:
        if car.split()[1] in model:
            continue
        full_car = car.split()[1:]
        for el in full_car:
            full_model += el
            if el != full_car[-1]:
                full_model += " "
        model.append(full_model)
        full_model = ""
    return model


def search_by_make(all_cars: str, maker: str):
    """Return list of cars and models."""
    cars = []
    cars_list = list_of_cars(all_cars)
    for el in cars_list:
        if el in cars:
            continue
        if maker.lower() in el:
            cars.append(el)
        elif maker.upper() in el:
            cars.append(el)
        elif maker.capitalize() in el:
            cars.append(el)
        else:
            continue
    return cars

print(search_by_make("Audi A4,Skoda Superb,Audi A4,Audi A6", "audi"))


