class Player:
    def __init__(self):
        self.name      = 'Sudo'
        self.level     = 1
        self.inventory = []

    def receive_item(self, item):
        self.inventory.append(item)
