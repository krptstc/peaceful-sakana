import time
import random

from modules.settings  import *
from modules.functions import *
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
    fish1 = Fish()
    fish2 = Fish()
    fish3 = Fish()
    print(fish1.name)
    print(fish2.name)
    print(fish3.name)
    print('[WIP] Sending you back to the main menu.')
    time.sleep(3)
    home()

main_menu = {
    'Go fishing': go_fishing,
    'Inventory': home,
    'Shop': home,
    'Statistics': home,
    'Save and Exit': exit
}
