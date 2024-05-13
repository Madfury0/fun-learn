import aspects as asp
from aspects import Player,Enemy,battle,get_random

width = 56 #decorators
offset = 20
# Read room descriptions from file
room_descriptions = asp.read_rooms("rooms.txt")
# Create player character
player_name = input("Enter your name: ")
player = Player(player_name, 100,1)


def saving():
    print ("Saving progress, DO NOT REMOVE THE FLASH DISK!")
    for i in range(5):
        asp.time.sleep(0.3)
        print ("." * width)
    print ("PROGRESS SAVED!")

def enemy_spawn ():
    #create enemy character
    enemy = Enemy("enemy", get_random(10,250),1)
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
    return enemy


def main ():
    asp.random.seed() # Seed random number generator
    # Game loop
    current_room = 0
    New_Game = True

    while New_Game:
        while current_room < len(room_descriptions):
            print ("+" * width)
            print(f"You are in room {current_room + 1}:")
            print ("+" * width)
            print ("=" * width)
            print(room_descriptions[current_room])
            print ("=" * width)

            # Randomly encounter enemy in some rooms
            if get_random(1, 2) == 1:
                enemy = enemy_spawn()

                battle(player, enemy)

                if not player.is_alive():
                    New_Game = False
                    print ("!" * width)
                    print (" "*offset,"GAME OVER!")
                    print ("!" * width)
                    print ("°" * width)
                    pick = input("New game? (y/n)")
                    print ("°" * width)
                    if pick.lower() == 'y':
                        print ("." * width)
                        print (" "*offset,"NEW GAME!")
                        print ("." * width)
                        player.health = 100
                        main()
                    else:
                        print("Thanks for playing!")
                        print ("-" * width)
                        saving()
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
                print ("-" * width)
                saving()
                New_Game = False
                break
            current_room += 1
    

if __name__ == "__main__":
    main()
