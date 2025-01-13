class Enemy():
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health

    def attack(self, player):
        print(f"{self.name} attacks {player.name} for {self.strength} damage!")
        player.health -= self.strength
        print(f"{player.name}'s health is now {player.health}.\n")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health left: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated!\n")
