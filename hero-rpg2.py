#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Characters():
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def alive(self, enemy):
        if self.health <= 0:
            print("{} is dead.".format(self.name))
        return self.health

class Hero(Characters):
    def attack(self, goblin):
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))

    def print_status(self):
        print("You have {} health and {} power.".format(hero.health, hero.power))


class Goblin(Characters):

    def attack(self, hero):
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))

    def print_status(self):
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))

class Zombie(Characters):
    def attack(self, hero):
        hero.health -= zombie.power
        print('The zombie does {} damage to you.'.format(zombie.power))

hero = Hero(10, 5, "Hero")
goblin = Goblin(6, 2, "Goblin")
zombie = Zombie(100, 1, "Zombie")

def main():
    hero.health = 10
    hero.power = 5
    goblin.health = 6
    goblin.power = 2
    zombie.power = 1
    zombie.health = 100

while goblin.alive(hero) > 0 and hero.alive(goblin) > 0:
    hero.print_status()
    goblin.print_status()
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    inpt = input()
    if inpt == "1":
        # Hero attacks goblin
        hero.attack(goblin)
        if goblin.health > 0:
            goblin.attack(hero)
            zombie.attack(hero)

    elif inpt == "2":
        goblin.attack(hero)
    elif inpt == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid inpt {}".format(inpt))



if __name__ == "__main__":
  main()

#class Character(object):
    #def __init__(self, ):
    #    self.health = health
    #    self.power = power
