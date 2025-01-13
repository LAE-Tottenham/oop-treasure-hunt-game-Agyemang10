class Place():
    def __init__(self, given_name, given_size, locked=False):
        self.name = given_name
        self.size = given_size
        self.locked = locked
        self.next_places = []
        self.items = []
        self.enemies = []

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def add_item(self, item_instance):
        self.items.append(item_instance)

    def add_enemy(self, enemy_instance):
        self.enemies.append(enemy_instance)

    def show_items(self):
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f"- {item.name}")
        else:
            print("No items here.\n")

    def show_enemies(self):
        if self.enemies:
            print("You encounter the following enemies:")
            for enemy in self.enemies:
                print(f"- {enemy.name} (Health: {enemy.health}, Strength: {enemy.strength})")
        else:
            print("No enemies here.\n")

    def show_next_places(self):
        print("The possible places you can go to are: ")
        for place in self.next_places:
            print(f"- {place.name} {'(Locked)' if place.locked else ''}")

