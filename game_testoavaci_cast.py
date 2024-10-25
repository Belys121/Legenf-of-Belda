import random

print(" WELCOME in Legend of Belda")


class Warrior():

    def __init__(self, name, character):
        self.name = name
        self.health = 100
        self.damage = 10
        self.game_character = character

    def introduce(self):
        print(f"Name: {self.name}, HP: {self.health}, Character: {self.game_character}")

    def attack(self, enemy):
        bonus_damage_chance = random.random()
        bonus_damage = 0
        miss_chance = random.random()
        if miss_chance < 0.2:
            print(f"{self.name} attacks {enemy.name} but misses!")
            return

        if self.is_alive():
            if bonus_damage_chance < 0.3:
                bonus_damage = random.randint(1, 5)
            total_damage = self.damage + bonus_damage
            enemy.health -= total_damage
            print(f"{self.name} attacks {enemy.name} and deals {total_damage} damage (including {bonus_damage} bonus damage).")
            if not enemy.is_alive():
                print(f"{enemy.name} is dead and {self.name} is winner!!!.")

    def is_alive(self):
            return self.health > 0


class Knight(Warrior):

    def __init__(self, name):
        super().__init__(name, "Knight")  # Rytir
        self.health = 120  # Vyšší zdraví
        self.damage = 12  # Vyšší základní poškození


class Archer(Warrior):

    def __init__(self, name):
        super().__init__(name, "Archer")  # Lucistnik
        self.health = 100  # Vyšší zdraví
        self.damage = 13  # Vyšší základní poškození


class DeathKnight(Warrior):

    def __init__(self, name):
        super().__init__(name, "Death Knight")  # Rytir smrti
        self.health = 115  # Vyšší zdraví
        self.damage = 15  # Vyšší základní poškození


class Paladin(Warrior):

    def __init__(self, name):
        super().__init__(name, "Paladin")
        self.health = 110  # Středně vysoké zdraví
        self.damage = 12  # Mírně vyšší poškození


class Hunter(Warrior):

    def __init__(self, name):
        super().__init__(name, "Hunter")  # Lovec
        self.health = 95  # Nižší zdraví
        self.damage = 14  # Vyšší poškození


class Rogue(Warrior):

    def __init__(self, name):
        super().__init__(name, "Rogue")  # Zlodej
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class Evoker(Warrior):

    def __init__(self, name):
        super().__init__(name, "Evoker")  # Vyvolavac
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class DemonHunter(Warrior):

    def __init__(self, name):
        super().__init__(name, "Demon_Hunter")  # lovec demonu
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class Druid(Warrior):

    def __init__(self, name):
        super().__init__(name, "Druid")
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class Monk(Warrior):

    def __init__(self, name):
        super().__init__(name, "Monk")  # mnich
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class Priest(Warrior):

    def __init__(self, name):
        super().__init__(name, "Priest")  # Knez
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class Shaman(Warrior):

    def __init__(self, name):
        super().__init__(name, "Shaman")  # Saman
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class Warlock(Warrior):

    def __init__(self, name):
        super().__init__(name, "Warlock")  # cernokneznik
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class Mage(Warrior):

    def __init__(self, name):
        super().__init__(name, "Mage")  # mag
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class Demon(Warrior):

    def __init__(self, name):
        super().__init__(name, "Demon")  # demon
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class HalfGod(Warrior):

    def __init__(self, name):
        super().__init__(name, "HalfGod")  # mnich
        self.health = 90  # Nižší zdraví
        self.damage = 16  # Vyšší poškození


class Arena:

    def __init__(self):
        self.warriors = []

    def register_warrior(self, warrior):
        self.warriors.append(warrior)

    def start_battle(self, warrior1, warrior2):
        print(f"\nYou choose {warrior1.name} - {warrior1.game_character} and enemy is {warrior2.name} - {warrior2.game_character}!\n")
        print("-" * 20)

        while warrior1.is_alive() and warrior2.is_alive():
            warrior1.attack(warrior2)
            if not warrior2.is_alive():
                print("-" * 20)
                break

            warrior2.attack(warrior1)
            if not warrior1.is_alive():
                print("-" * 20)
                break

            print("-" * 20)
            warrior1.introduce()
            warrior2.introduce()

        print("Battle is over.")

    def run_tournament(self):
        while len(self.warriors) > 1:
            warrior1 = self.warriors.pop(0)
            warrior2 = self.warriors.pop(0)
            print(f"\n{warrior1.name} vs {warrior2.name}")
            self.start_battle(warrior1, warrior2)
            if warrior1.is_alive():
                self.warriors.append(warrior1)
            else:
                self.warriors.append(warrior2)
        print(f"\n{self.warriors[0].name} is the Tournament Champion!")


class GameTypeSelector:

    def __init__(self, ):
        self.arena = Arena()

    def choose_type_game(self):
        choose_game = input("Choose game type:\n1: Duel\n2: Tournament\n Enter your choice (1/2): ")
        if choose_game == "1":
            self.start_duel()
        elif choose_game == "2":
            self.start_tournament()
        else:
            print("Ivalid choice, try it again!")
            self.choose_type_game()

    def start_duel(self):
        warrior1 = choose_warrior("Choose your warrior:\n")
        warrior2 = choose_warrior("Choose your enemy:\n")
        self.arena.start_battle(warrior1, warrior2)

    def start_tournament(self):
        for _ in range(16):
            warrior = choose_warrior("Choose your warrior for tournament:\n")
            self.arena.register_warrior(warrior)
        self.arena.run_tournament()


def choose_warrior(selection_type):

    warriors = {
        "1": Knight("Aragorn"),
        "2": Archer("Legolas"),
        "3": DeathKnight("Darius"),
        "4": Paladin("Garen"),
        "5": Hunter("Master Yi"),
        "6": Rogue("Shaco"),
        "7": Evoker("Amumu"),
        "8": DemonHunter("Aphleios"),
        "9": Druid("Neeko"),
        "10": Monk("Jax"),
        "11": Priest("Viego"),
        "12": Shaman("Swain"),
        "13": Warlock("Shen"),
        "14": Mage("Ryze"),
        "15": Demon("Nocturne"),
        "16": HalfGod("Pearcy")
    }
    print(f"\n{selection_type}")
    for key, warrior in warriors.items():
        print(f"{key}: {warrior.name}, {warrior.game_character}")

    while True:
        choice = input("Enter the number of the warrior you want to choose: ")
        if choice not in warriors:
            print("You didn't choice right warrior. Try it again!")
        else:
            return warriors.get(choice)


# class UserInput():
#     pass

# arena = Arena()
#
# warrior1 = choose_warrior("Now choose your warrior please!\n")
# arena.register_warrior(warrior1) # registry to arena
#
# warrior2 = choose_warrior("And now choose enemy warrior please!\n")
# arena.register_warrior(warrior2) # registry to arena


# print("-" * 20)
# arena.start_battle() # funguje
# arena.run_tournament() # nefunguje

game = GameTypeSelector()
game.choose_type_game()

# TODO - uprav classy hracu - zivoty utoky
