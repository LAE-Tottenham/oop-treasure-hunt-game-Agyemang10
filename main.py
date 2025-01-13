from place import Place
from player import Player
from item import Item
from enemy import Enemy

class Game():
    def __init__(self):
        self.current_place = None

    def setup(self):
        # Places
        home = Place('Home', 10)
        garden = Place('Garden', 15)
        bedroom = Place('Bedroom', 5)
        cave = Place('Cave', 50, locked=True)

        home.add_next_place(garden)
        home.add_next_place(bedroom)
        garden.add_next_place(cave)

        # Items
        key = Item("Key", 1, "key")
        sword = Item("Sword", 3, "weapon")
        apple = Item("Apple", 1, "food")

        home.add_item(apple)
        garden.add_item(key)
        bedroom.add_item(sword)

        # Enemies
        goblin = Enemy("Goblin", 10, 30)
        cave.add_enemy(goblin)

        self.current_place = home
        self.places = [home, garden, bedroom, cave]

    def start(self):
        print("Welcome to the Adventure Game!")
        name = input("Enter your name: ")
        player = Player(name)

        while True:
            print(f"You are in {self.current_place.name}\n")
            self.current_place.show_items()
            self.current_place.show_enemies()
            self.current_place.show_next_places()

            action = input("What would you like to do? (move/pickup/fight/inventory/use/unlock/quit): ").lower()

            if action == "move":
                destination = input("Where would you like to go? ").capitalize()
                for place in self.current_place.next_places:
                    if place.name == destination:
                        if place.locked:
                            print(f"{place.name} is locked.")
                            if player.unlock_place(place):
                                self.current_place = place
                        else:
                            self.current_place = place
                        break
                else:
                    print("Invalid place.\n")

            elif action == "pickup":
                if self.current_place.items:
                    item_name = input("Which item would you like to pick up? ").capitalize()
                    for item in self.current_place.items:
                        if item.name == item_name:
                            player.add_item(item)
                            self.current_place.items.remove(item)
                            break
                    else:
                        print("Item not found.\n")
                else:
                    print("No items to pick up.\n")

            elif action == "fight":
                if self.current_place.enemies:
                    enemy = self.current_place.enemies[0]
                    print(f"You are fighting {enemy.name}!")
                    while player.health > 0 and enemy.health > 0:
                        enemy.take_damage(20)
                        if enemy.health > 0:
                            enemy.attack(player)
                        if player.health <= 0:
                            print("You have been defeated. Game Over!")
                            return
                    self.current_place.enemies.remove(enemy)
                else:
                    print("No enemies here.\n")

            elif action == "inventory":
                player.show_inventory()

            elif action == "use":
                item_name = input("Which item would you like to use? ").capitalize()
                player.use_item(item_name)

            elif action == "quit":
                print("Thanks for playing!")
                break

            else:
                print("Invalid action.\n")

game = Game()
game.setup()
game.start()

