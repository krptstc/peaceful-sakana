import os

from modules.settings import *

def clear_screen():
    os.system('clear')

def print_game_title():
    print(f'{game_title} {game_version}')

def view_menu(menu):
    print('')
    for i in range(len(menu)):
        print(f'{i + 1}) {menu[i]}')
    print('')

def pick_from_menu(menu):
    selection = 0
    while selection < 1 or selection > len(menu):
        try:
            selection = int(input('>> '))
        except:
            pass
