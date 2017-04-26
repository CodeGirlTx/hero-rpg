#!/usr/bin/env python3

"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""

import random
import time

class Character:
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        if self.name == 'Zombie':
            return True
        else:
            return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))


    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0

    def receive_damage(self, points):
        points = points - self.armor
        if self.evade == 2:
            probability = random.random() < 0.1
            if probability:
                points = 0
        if self.evade == 4:
            probability = random.random() < 0.15
            if probability:
                points = 0
        if self.evade == 6:
            probability = random.random() < 0.2
            if probability:
                points = 0
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))

    def attack(self, enemy):
        super().attack(enemy)
        probability = random.random() < 0.2
        if probability:
            super().attack(enemy)
            print("You used double power!")

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to {}!".format(self.health))
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 5
        self.power = 2
        self.bount = 4

    def recuperate(self):
        give_health = random.random() > 0.2
        if give_health:
            self.health += 2

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 3
        self.bounty = 7


    def little_damage(self):
        min_damage = random.random() > 0.9
        if min_damage:
            self.health = 1

class Zombie(Character):
    def __init__(self):
        self.name = 'Zombie'
        self.health = 2
        self.power = 3
        self.bounty = 0



class Battle:
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the {}".format(enemy.name))
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight {}".format(enemy.name))
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            keyinput = int(input())
            if keyinput == 1:
                hero.attack(enemy)
            elif keyinput == 2:
                pass
            elif keyinput == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input {}".format(input))
                continue
            enemy.attack(hero)
        if hero.alive():
            print("You defeated the {}".format(enemy.name))
            hero.coins += enemy.bounty
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic:
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class Sword:
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class SuperTonic:
    cost = 12
    name = 'supertonic'
    def apply(self, hero):
        hero.health += 10
        print("Hero's health increased by 10")

class Armor:
    cost = 5
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print("You now have {} armor and are stronger against enemy attacks!".format(hero.armor))

class Evade:
    cost = 10
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2
        print("You now have {} evade points!".format(hero.evade))

class Store:
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            choice = int(input("> "))
            if choice == 10:
                break
            else:
                ItemToBuy = Store.items[choice - 1]
                item = ItemToBuy()
                hero.buy(item)

if __name__ == "__main__":
    hero = Hero()
    enemies = [Goblin(), Wizard(), Medic(), Shadow(), Zombie()]

    battle_engine = Battle()
    shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")


# def give_bounty(self, hero):
#     add_coins = self.bounty + hero.coins
#     if self.health <= 0:
#         add_coins
