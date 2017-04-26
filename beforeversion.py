#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
#class Character():
    #def __init__(self, attack, alive, print_status)

class Hero():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, goblin):
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))

    def alive(self, goblin):
        if hero.health <= 0:
            print("You are dead.")
        return self.health

    def print_status(self):
        print("You have {} health and {} power.".format(hero.health, hero.power))


class Goblin():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, hero):
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))

    def alive(self, hero):
        if goblin.health <= 0:
            print("Goblin is dead")
        return self.health

    def print_status(self):
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))

hero = Hero(10, 5)
goblin = Goblin(6, 2)

def main():
    hero.health = 10
    hero.power = 5
    goblin.health = 6
    goblin.power = 2

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

    elif inpt == "2":
        pass
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
