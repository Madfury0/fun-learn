import random
import time
class  Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.defend(self.attack)

    def defend(self, damage):
        if damage > self.health:
            damage = self.health
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")

    def display_status(self):
        print(f"Name: {self.name}, Health: {self.health}")
    def is_alive(self):
        return self.health > 0


class Player(Character):
    pass

class Enemy(Character):
    pass

def battle(player, enemy):
    n = 1
    width = 56
    offset = 23
    delay = 3
    while player.is_alive() and enemy.is_alive():
        print("-" * width)
        print (" " * offset,f"ROUND: {n}")
        player.display_status()
        enemy.display_status()
        print("-" * width)

        #random damages per round
        player.attack = get_random (1,100)
        player.attack_enemy(enemy)
        time.sleep(delay)
        if not enemy.is_alive():
            print( "•" * width)
            print(f"{enemy.name} defeated!")
            elixr = get_random(10, 60)
            if 10 <= elixr <= 20:
                print (f"Earned green elixr: +{elixr}hp")
            elif 21 <= elixr <= 39:
                print (f"Earned blue elixr: +{elixr}hp")
            else:
                print (f"Earned purple elixr: +{elixr}hp")
            player.health += elixr
            player.display_status()
            return

        enemy.attack = get_random (1,75)
        enemy.attack_enemy(player)
        time.sleep(delay)

        if not player.is_alive():
            print ("`" * width)
            print(f"{player.name} was defeated!")
            enemy.display_status()
            print(" " * offset,"YOU ARE DEAD!!")
            print ("`" * width)
            return
        n += 1


def get_random(min, max):
    return random.randint(min, max)

def read_rooms(filename):
    with open(filename, 'r') as file:
        return file.readlines()
