import os

from modules.settings import *

def clear_screen():
    os.system('clear')

def print_game_title():
    print(f'{game_title} {game_version}\n')

def view_menu(menu):
    items = []
    for key in menu.keys():
        items.append(key)
    for i in range(len(items)):
        print(f'{i + 1}) {items[i]}')
    print('')

def pick_from_list(list, canGoBack = False):
    selection = -1
    while selection < 1 or selection > len(list):
        try:
            selection = int(input('>> '))
            if selection == 0 and canGoBack:
                return selection
        except:
            pass
    return selection

def pick_from_menu(menu):
    selection = pick_from_list(menu)
    list = []
    for function in menu.values():
        list.append(function)
    list[selection - 1]()

def ask_for_input():
    print('\nPress ENTER to return back.')
    input()

def loop_through_inventory(inventory):
    for i in range(len(inventory)):
        print(f'  {i + 1}) {inventory[i].name} [{inventory[i].value} {currency_symbol}]')
