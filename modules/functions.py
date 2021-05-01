import os

from modules.settings import *

def clear_screen():
    os.system('clear')

def print_game_title():
    print(f'{game_title} {game_version}')

def view_menu(menu):
    items = []
    for key in menu.keys():
        items.append(key)
    print('')
    for i in range(len(items)):
        print(f'{i + 1}) {items[i]}')
    print('')

def pick_from_menu(menu):
    selection = 0
    while selection < 1 or selection > len(menu):
        try:
            selection = int(input('>> '))
        except:
            pass
    list = []
    for function in menu.values():
        list.append(function)
    list[selection - 1]()
