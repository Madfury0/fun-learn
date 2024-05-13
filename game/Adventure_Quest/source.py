import random

width = 56 #decorators

class Character:
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
    while player.is_alive() and enemy.is_alive():
        print("-" * width)
        print (f"                ROUND: {n}")
        player.display_status()
        enemy.display_status()
        print("-" * width)
        #random damages per round
        player.attack = get_random (1,100)
        player.attack_enemy(enemy)

        if not enemy.is_alive():
            print( "•" * width)
            print(f"{enemy.name} defeated!")
            elixr = get_random(10, 60)
            if 10 <= elixr <= 20:
                print (f"Earned green elixr: +{elixr}hp")
            elif 21 <= elixr <= 39:                                       print (f"Earned blue elixr: +{elixr}hp")
            else:
                print (f"Earned purple elixr: +{elixr}hp")
            player.health += elixr
            player.display_status()
            return

        enemy.attack = get_random (1,75)
        enemy.attack_enemy(player)

        if not player.is_alive():
            print ("`" * width)
            print(f"{player.name} was defeated!")
            enemy.display_status()
            print("                  GAME OVER!!")
            print ("`" * width)
            return
        n += 1

def get_random(min, max):
    return random.randint(min, max)

def read_rooms(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def main():
    random.seed() # Seed random number generator

    # Read room descriptions from file
    room_descriptions = read_rooms("rooms.txt")

    # Create player character
    player_name = input("Enter your name: ")
    player = Player(player_name, 100,1)

    #create enemy character
    enemy = Enemy("enemy", get_random(10,250),1)


    # Game loop
    current_room = 0
    while current_room < len(room_descriptions):
        print ("+" * width)
        print(f"You are in room {current_room + 1}:")
        print ("+" * width)
        print ("=" * width)
        print(room_descriptions[current_room])
        print ("=" * width)

        # Randomly encounter enemy in some rooms
        if get_random(1, 2) == 1:
            enemy = Enemy("enemy", get_random(10,250),enemy.attack)
            if 10 <= enemy.health <= 49:
                print ("~" * width)
                print("You encounter a level 1 enemy!")
                print ("~" * width)
                enemy = Enemy("Green Goblin", enemy.health, enemy.attack)
            elif 50 <= enemy.health <= 99:
                print ("~" * width)
                print(f"You encounter a level 2 enemy!")
                print ("~" * width)
                enemy = Enemy("Red Goblin", enemy.health, enemy.attack)
            elif 100 <= enemy.health <= 149:
                print ("~" * width)
                print(f"You encounter a level 3 enemy!")
                print ("~" * width)
                enemy = Enemy("The Witch", enemy.health, enemy.attack)
            else:
                print ("~" * width)
                print (f"You encounter The Boss!")
                print ("~" * width)
                enemy = Enemy("The Dragon", enemy.health, enemy.attack)

            battle(player, enemy)

            if not player.is_alive():
                break
        else:
            print ("~" * width)
            print ("No enemies in the current room")
            print ("~" * width)
        # Move to next room or end game
        print (">" * width)
        choice = input("Do you want to move to the next room? (y/n): ")
        print (">" * width)
        if choice.lower() != 'y':
            print("Thanks for playing!")
            break
        current_room += 1

if __name__ == "__main__":
    main()
