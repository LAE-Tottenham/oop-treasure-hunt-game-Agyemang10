class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.health = 100
        self.energy = 100
        self.inventory_max_weight = 10
        self.inventory = []

    def calculate_inventory_size(self):
        return sum(item.weight for item in self.inventory)

    def add_item(self, item_instance):
        if self.calculate_inventory_size() + item_instance.weight <= self.inventory_max_weight:
            self.inventory.append(item_instance)
            print(f"{item_instance.name} has been added to your inventory.\n")
        else:
            print("Your inventory is full...\n")

    def show_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"- {item}")
        print(f"Total weight: {self.calculate_inventory_size()} / {self.inventory_max_weight}\n")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                if item.type == "food":
                    self.energy += 20
                    print("You ate food and regained 20 energy!\n")
                elif item.type == "medicine":
                    self.health += 20
                    print("You used medicine and regained 20 health!\n")
                self.inventory.remove(item)
                return
        print("You don't have that item.\n")

    def unlock_place(self, place):
        for item in self.inventory:
            if item.type == "key" and place.locked:
                place.locked = False
                print(f"You unlocked {place.name} using a key!\n")
                return True
        print(f"You need a key to unlock {place.name}.\n")
        return False

