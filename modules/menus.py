import time
import random

from modules.settings  import *
from modules.functions import *
from __main__          import player
from classes.fish      import Fish

def home():
    clear_screen()
    print_game_title()
    view_menu(main_menu)
    pick_from_menu(main_menu)

def go_fishing():
    clear_screen()
    print_game_title()
    waitingTime = random.randint(fishing_time_min, fishing_time_max)
    print('You are fishing ...')
    time.sleep(waitingTime)
    caughtFish = Fish()
    player.receive_item(caughtFish)
    print(f'You have caught {caughtFish.name}. The value of it is {caughtFish.value} {currency_symbol}.')
    ask_for_input()
    home()

def stats():
    clear_screen()
    print_game_title()
    player.view_stats()
    ask_for_input()
    home()

def shop():
    clear_screen()
    print_game_title()
    print('Shop\n')
    print('Select an item to sell, type 0 to go back.\n')
    if len(player.inventory) > 0:
        loop_through_inventory(player.inventory)
        print('')
        selection = pick_from_list(player.inventory, True)
        if selection == 0:
            home()
        selectedItem = player.inventory[selection - 1]
        print(f'You have sold {selectedItem.name} for {selectedItem.value} {currency_symbol}.')
        player.balance += selectedItem.value
        player.inventory.pop(selection - 1)
    else:
        print('You have no items to sell yet!')
    ask_for_input()
    home()

main_menu = {
    'Go fishing': go_fishing,
    'Shop': shop,
    'Statistics': stats,
    'Save and Exit': exit
}
