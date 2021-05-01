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
    selection = pick_from_menu(main_menu)

def go_fishing():
    clear_screen()
    print_game_title()
    waitingTime = random.randint(fishing_time_min, fishing_time_max)
    print('You are fishing ...')
    time.sleep(waitingTime)
    caughtFish = Fish()
    player.receive_item(caughtFish)
    print(f'You have caught {caughtFish.name}.')
    ask_for_input()
    home()

def stats():
    clear_screen()
    print_game_title()
    print(player.name)
    print(f'\nLevel: {player.level}')
    print('\nInventory\n')
    if len(player.inventory) > 0:
        for i in range(len(player.inventory)):
            print(f'  {i + 1}) {player.inventory[i].name}')
    else:
        print('  You haven\'t got any items yet!')
    ask_for_input()
    home()

main_menu = {
    'Go fishing': go_fishing,
    'Shop': home,
    'Statistics': stats,
    'Save and Exit': exit
}
