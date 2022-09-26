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
    for car in cars:
        if len(car.split(" ", 1)) == 1:
            continue
        if car.split()[1] in model:
            continue
        full_car = car.split(" ", 1)
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
        if maker.lower() == makes[i] or maker.upper() == makes[i] or maker.capitalize() == makes[i]:
            i += 1
            cars.append(car)
        else:
            i += 1
            continue
    return cars


def search_by_model(all_cars: str, model: str):
    """Search for model in all the cars."""
    cars_list = list_of_cars(all_cars)
    models = []
    cars = []
    if len(model.split()) > 1:
        return []
    for el in cars_list:
        car_model = el.split(" ", 1)
        models.append(car_model[1])
    for car in cars_list:
        full_split = car.split()
        if model.upper() in full_split[0] or model.lower() in full_split[0] or model.capitalize() in full_split[0]:
            continue
        if model.upper() in full_split or model.lower() in full_split or model.capitalize() in full_split:
            cars.append(car)
        else:
            continue
    return cars


cars = "Audi A4,Skoda Superb superb,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb x,Skoda Superb,BMW x5"
print(search_by_model(cars, "A4 2021"))  # == ['Audi A4 2021']
print(search_by_model(cars, "sept"))  # == ['Audi A4 2022 sept']
print(search_by_model(cars, "superb"))  # == []
print(search_by_make(cars, "skODA"))
# == ['Audi A4', 'Audi A4', 'Audi A4', 'Audi A6', 'Audi A4 2022']
print(search_by_make("Audi A4", "A4"))  # == []
