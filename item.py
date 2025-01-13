class Item():
    def __init__(self, name, weight=1, item_type="general"):
        self.name = name
        self.weight = weight
        self.type = item_type  # Examples: 'key', 'weapon', 'food', 'medicine'

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Weight: {self.weight})"

