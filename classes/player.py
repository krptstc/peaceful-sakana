import random

from modules.settings  import *
from modules.functions import *

from classes.fish      import Fish

class Player:
    def __init__(self):
        self.name      = 'Sudo'
        self.level     = 1
        self.xp        = 0
        self.maxXp     = 0
        self.balance   = 0
        self.inventory = []

        for i in range(128):
            self.receive_item(Fish())

        self.calculate_max_xp()

    def calculate_max_xp(self):
        self.maxXp = 100
        if self.level > 1:
            for i in range(self.level - 1):
                self.maxXp *= next_level_rate
            self.maxXp = int(self.maxXp)

    def check_level(self):
        if self.xp >= self.maxXp:
            self.level += 1
            self.xp -= self.maxXp
            self.calculate_max_xp()

    def receive_item(self, item):
        self.inventory.append(item)
        if item.get_class() == 'Fish':
            addedXp = 0
            if item.value > 5:
                addedXp = random.randint(10, 20)
            else:
                addedXp = random.randint(1, 10)
            self.xp += addedXp
            self.check_level()

    def view_stats(self):
        print(self.name)
        print(f'\nLevel: {self.level}')
        print(f'XP: {self.xp} / {self.maxXp}')
        print(f'Balance: {self.balance} {currency_symbol}')
        print('\nInventory\n')
        if len(self.inventory) > 0:
            loop_through_inventory(self.inventory)
        else:
            print('  You haven\'t got any items yet!')
