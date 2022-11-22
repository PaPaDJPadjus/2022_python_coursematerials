"""Alchemy."""


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """

    def __init__(self, name: str):
        """Define name."""
        self.name = name

    def __repr__(self) -> str:
        """Display element."""
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.elements = []

    def __repr__(self):
        """Display list."""
        return f"{self.elements}"

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError exception.

        :param element: Input object to add to storage.
        """
        if isinstance(element, AlchemicalElement):
            self.elements.append(element)
        else:
            raise TypeError()

    def pop(self, element_name: str) -> AlchemicalElement or None:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        i = len(self.elements) - 1
        while i >= 0:
            if element_name == self.elements[i].name:
                return self.elements.pop(i)
            i -= 1
        return None

    def extract(self) -> list[AlchemicalElement]:
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        new_list = []
        for el in self.elements:
            new_list.append(el)

        self.elements.clear()
        return new_list

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        if not self.elements:
            return "Content:\n Empty."
        sorted_elements_list = sorted(self.elements, key=lambda x: x.name)
        el_dict = {}
        counted_el = []
        final_string = "Content:"
        for el in sorted_elements_list:
            if el not in counted_el:
                amount = sorted_elements_list.count(el)
                el_dict[el.name] = el_dict.get(el.name, 0) + amount
                counted_el.append(el)

        for key_n_value in el_dict:
            final_string += f"\n * {key_n_value} x {el_dict[key_n_value]}"
        return final_string


class AlchemicalRecipes:
    """AlchemicalRecipes class."""

    def __init__(self):
        """
        Initialize the AlchemicalRecipes class.

        Add whatever you need to make this class function.
        """
        self.dict_recipe = {}

    def add_recipe(self, first_component_name: str, second_component_name: str, product_name: str):
        """
        Determine if recipe is valid and then add it to recipes.

        A recipe consists of three strings, two components and their product.
        If any of the parameters are the same, raise the 'DuplicateRecipeNamesException' exception.
        If there already exists a recipe for the given pair of components, raise the 'RecipeOverlapException' exception.

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :param product_name: The name of the product element.
        """
        if first_component_name == second_component_name:
            raise DuplicateRecipeNamesException
        if first_component_name == product_name or second_component_name == product_name:
            raise DuplicateRecipeNamesException
        if [first_component_name, second_component_name] in self.dict_recipe.values():
            raise RecipeOverlapException
        if [second_component_name, first_component_name] in self.dict_recipe.values():
            raise RecipeOverlapException
        if first_component_name != second_component_name != product_name:
            if product_name not in self.dict_recipe.keys():
                new_recipe = [first_component_name, second_component_name]
                self.dict_recipe[product_name] = new_recipe
        else:
            raise DuplicateRecipeNamesException

    def get_product_name(self, first_component_name: str, second_component_name: str) -> str or None:
        """
        Return the name of the product for the two components.

        The order of the first_component_name and second_component_name is interchangeable, so search for combinations
        of (first_component_name, second_component_name) and (second_component_name, first_component_name).

        If there are no combinations for the two components, return None

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            recipes.get_product_name('Water', 'Wind')  # ->  'Ice'
            recipes.get_product_name('Wind', 'Water')  # ->  'Ice'
            recipes.get_product_name('Fire', 'Water')  # ->  None
            recipes.add_recipe('Water', 'Fire', 'Steam')
            recipes.get_product_name('Fire', 'Water')  # ->  'Steam'

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :return: The name of the product element or None.
        """
        for key in self.dict_recipe.keys():
            if self.dict_recipe[key][0] == first_component_name or self.dict_recipe[key][0] == second_component_name:
                if self.dict_recipe[key][1] == first_component_name or self.dict_recipe[key][1] == second_component_name:
                    return str(key)

    def get_component_name(self, product_name: str):
        """Get component name."""
        if product_name in self.dict_recipe.keys():
            return self.dict_recipe[product_name]
        return None


class DuplicateRecipeNamesException(Exception):
    """Raised when attempting to add a recipe that has same names for components and product."""


class RecipeOverlapException(Exception):
    """Raised when attempting to add a pair of components that is already used for another existing recipe."""


class Cauldron(AlchemicalStorage):
    """
    Cauldron class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Cauldron class."""
        super(AlchemicalStorage).__init__()
        self.elements = []
        self.recipes = recipes

    def __repr__(self):
        """Show values."""
        return f"{self.elements}"

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can combine with anything already inside.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            cauldron = Cauldron(recipes)
            cauldron.add(AlchemicalElement('Water'))
            cauldron.add(AlchemicalElement('Wind'))
            cauldron.extract() # -> [<AE: Ice>]

        :param element: Input object to add to storage.
        """
        if not isinstance(element, AlchemicalElement):
            raise TypeError

        el_combos = []
        for combo in self.recipes.dict_recipe.values():
            el_combos.append(combo)

        i = 0
        if_el_in_list_counter = 0
        for el in self.elements[::-1]:
            if not if_el_in_list_counter == 1:
                if [el.name, element.name] in el_combos or [element.name, el.name] in el_combos:
                    new_el = AlchemicalElement(self.recipes.get_product_name(el.name, element.name))
                    self.elements.remove(el)
                    self.elements.append(new_el)
                    i += 1
                    if_el_in_list_counter += 1

        if i == 0:
            self.elements.append(element)


class Catalyst(AlchemicalElement):
    """Catalyst class."""

    def __init__(self, name: str, uses: int):
        """
        Initialize the Catalyst class.

        :param name: The name of the Catalyst.
        :param uses: The number of uses the Catalyst has.
        """
        self.name = name
        self.uses = 0

    def __repr__(self) -> str:
        """
        Representation of the Catalyst class.

        Example:
            catalyst = Catalyst("Philosophers' stone", 3)
            print(catalyst) # -> <C: Philosophers' stone (3)>

        :return: String representation of the Catalyst.
        """
        return f"<C: {self.name} ({self.uses})>."


class Purifier(AlchemicalStorage):
    """
    Purifier class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Purifier class."""
        super().__init__()
        self.recipes = recipes

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can be split into anything.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            purifier = Purifier(recipes)
            purifier.add(AlchemicalElement('Ice'))
            purifier.extract() # -> [<AE: Water>, <AE: Wind>]   or  [<AE: Wind>, <AE: Water>]

        :param element: Input object to add to storage.
        """
        if not isinstance(element, AlchemicalElement):
            raise TypeError

        el_combos = []
        for combo in self.recipes.dict_recipe.values():
            el_combos.append(combo)

        i = 0
        if_el_in_list_counter = 0
        for el in self.elements[::-1]:
            if not if_el_in_list_counter == 1:
                if el.name == element.name:
                    new_el = self.recipes.get_component_name(element.name)
                    self.elements.remove(el)
                    for object in new_el:
                        self.elements.append(AlchemicalElement(object))
                        i += 1
                        if_el_in_list_counter += 1

        if i == 0:
            self.elements.append(element)


if __name__ == '__main__':
    philosophers_stone = Catalyst("Philosophers' stone", 2)

    recipes = AlchemicalRecipes()
    recipes.add_recipe("Philosophers' stone", 'Mercury', 'Gold')
    recipes.add_recipe("Fire", 'Earth', 'Iron')

    cauldron = Cauldron(recipes)
    cauldron.add(philosophers_stone)
    cauldron.add(AlchemicalElement('Mercury'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (1)>, <AE: Gold>]

    cauldron.add(philosophers_stone)
    cauldron.add(AlchemicalElement('Mercury'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Gold>]

    cauldron.add(philosophers_stone)
    cauldron.add(AlchemicalElement('Mercury'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Mercury>]

    purifier = Purifier(recipes)
    purifier.add(AlchemicalElement('Iron'))
    print(purifier.extract())  # -> [<AE: Fire>, <AE: Earth>]    or      [<AE: Earth>, <AE: Fire>]

