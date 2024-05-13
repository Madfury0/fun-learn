#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

// Base class for game characters
class Character {
protected:
    int health;
    int attack;

public:
    string name;
    Character(const string& name, int health, int attack) : name(name), health(health), attack(attack) {}

    virtual void attackEnemy(Character& enemy) = 0; // Pure virtual function for attacking an enemy
    virtual void defend(int damage) = 0; // Pure virtual function for defending against an attack

    void displayStatus() const {
        cout << "Name: " << name << ", Health: " << health << ", Attack: " << attack << endl;
    }

    bool isAlive() const {
        return health > 0;
    }
};

// Derived class for player character
class Player : public Character {
public:
    Player(const string& name) : Character(name, 100, 20) {}

    void attackEnemy(Character& enemy) override {
        cout << name << " attacks " << enemy.name << "!" << endl;
        enemy.defend(attack);
    }

    void defend(int damage) override {
        health -= damage;
        cout << name << " takes " << damage << " damage!" << endl;
    }
};

// Derived class for enemy character
class Enemy : public Character {
public:
    Enemy(const string& name, int health, int attack) : Character(name, health, attack) {}

    void attackEnemy(Character& player) override {
        cout << name << " attacks " << player.name << "!" << endl;
        player.defend(attack);
    }

    void defend(int damage) override {
        health -= damage;
        cout << name << " takes " << damage << " damage!" << endl;
    }
};

// Function to simulate a battle between player and enemy
void battle(Player& player, Enemy& enemy) {
    while (player.isAlive() && enemy.isAlive()) {
        player.attackEnemy(enemy);
        if (!enemy.isAlive()) {
            cout << enemy.name << " defeated!" << endl;
            return;
        }
        enemy.attackEnemy(player);
        if (!player.isAlive()) {
            cout << player.name << " was defeated!" << endl;
            return;
        }
    }
}

// Function to generate random number within a range
int getRandom(int min, int max) {
    return rand() % (max - min + 1) + min;
}

// Function to read room descriptions from file
vector<string> readRooms(const string& filename) {
    vector<string> rooms;
    ifstream file(filename);
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            rooms.push_back(line);
        }
        file.close();
    } else {
        cerr << "Error: Unable to open file " << filename << endl;
    }
    return rooms;
}

int main() {
    srand(time(nullptr)); // Seed random number generator

    // Read room descriptions from file
    vector<string> roomDescriptions = readRooms("rooms.txt");

    // Create player character
    string playerName;
    cout << "Enter your name: ";
    cin >> playerName;
    Player player(playerName);

    // Game loop
    int currentRoom = 0;
    while (currentRoom < roomDescriptions.size()) {
        cout << "You are in room " << currentRoom + 1 << ":" << endl;
        cout << roomDescriptions[currentRoom] << endl;

        // Randomly encounter enemy in some rooms
        if (getRandom(1, 2) == 1) {
            Enemy enemy("Goblin", getRandom(20, 30), getRandom(5, 10));
            cout << "You encounter a Goblin!" << endl;
            battle(player, enemy);
            if (!player.isAlive()) {
                cout << "Game Over!" << endl;
                break;
            }
        }

        // Move to next room or end game
        cout << "Do you want to move to the next room? (y/n): ";
        char choice;
        cin >> choice;
        if (choice != 'y' && choice != 'Y') {
            cout << "Thanks for playing!" << endl;
            break;
        }
        currentRoom++;
    }

    return 0;
}
