from modules.settings import *

class Player:
    def __init__(self):
        self.name      = 'Sudo'
        self.level     = 1
        self.balance   = 0
        self.inventory = []

    def receive_item(self, item):
        self.inventory.append(item)

    def view_stats(self):
        print(self.name)
        print(f'\nLevel: {self.level}')
        print(f'Balance: {self.balance} {currency_symbol}')
        print('\nInventory\n')
        if len(self.inventory) > 0:
            loop_through_inventory(self.inventory)
        else:
            print('  You haven\'t got any items yet!')
