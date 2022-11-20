"""Adventure time."""
from math import floor


class Adventurer:
    """Class for Adventurer characters."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Define name."""
        possible_classes = ["Fighter", "Druid", "Wizard", "Paladin"]
        self.name = name
        self.class_type = class_type
        self.power = power
        self.experience = experience

        if self.class_type not in possible_classes:
            self.class_type = "Fighter"
        if self.power > 99:
            self.power = 10

    def __repr__(self):
        """Display correctly."""
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."

    def add_power(self, power: int):
        """Add power to adventurer."""
        self.power += power

    def add_experience(self, exp: int):
        """Add XP to adventurer."""

        if 0 > self.experience:
            self.experience = 0

        if self.experience >= 0:
            if 0 > exp:
                self.experience = self.experience
            else:
                self.experience += exp
            if self.experience > 99:
                self.power += floor(self.experience / 10)
                self.experience = 0


class Monster:
    """Class fo tha monsters."""

    def __init__(self, name: str, type: str, power: int):
        """Define monstah"""
        self.name = name
        self.type = type
        self.power = power

        if self.type == "Zombie":
            self.name = "Undead " + self.name

    def __repr__(self):
        """Display correctly."""
        return f"{self.name} of type {self.type}, Power: {self.power}."


class World:
    """World-class."""

    def __init__(self, python_master):
        """World init."""
        self.python_master = python_master
        self.adventurer_list = []
        self.monster_list = []
        self.graveyard = []

    def get_python_master(self):
        """Get python master."""
        return self.python_master

    def get_adventurer_list(self):
        """Get adventurer list."""
        return self.adventurer_list

    def get_monster_list(self):
        """Get monster list."""
        return self.monster_list

    def add_adventurer(self, adventurer: Adventurer):
        """Add adventurer to list of adventurers."""
        if isinstance(adventurer, Adventurer):
            self.adventurer_list.append(adventurer)

    def add_monster(self, monster: Monster):
        """Add monster to list of monsters."""
        if isinstance(monster, Monster):
            self.monster_list.append(monster)

    def get_graveyard(self):
        """Get graveyard."""
        return self.graveyard


if __name__ == "__main__":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)

    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    friend.add_power(20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

    world.add_monster(annoying_friend)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    world.add_adventurer(annoying_friend)
    print()

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)
    print(world.get_monster_list())
