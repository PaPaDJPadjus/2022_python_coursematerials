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
        if " " not in car:
            model.append(car)

        full_car = car.split()[1:]
        for el in full_car:
            full_model += el
            if el != full_car[-1]:
                full_model += " "
        if full_model in model:
            continue
        elif full_model == "":
            continue
        else:
            model.append(full_model)
        full_model = ""
    return model


def search_by_make(all_cars: str, maker: str):
    """Return list of cars and models."""
    cars_list = list_of_cars(all_cars)
    cars = []
    for el in cars_list:
        if el in cars or el.lower() in cars or el.upper() in cars or el.capitalize() in cars:
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


print(search_by_make("Audi A4,Skoda Superb,audi a4,audi haige machine,AUDI elukas X", "audi"))  # ["Audi A4", "Skoda"
print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
print(car_makes("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # ['Mazda']
print(car_makes(""))  # []
print(car_models("6"))  # ["A4", "Superb", "A6"]
