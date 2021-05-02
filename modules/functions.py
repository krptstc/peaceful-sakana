import os

from modules.settings import *

def clear_screen():
    os.system('clear')

def print_game_title():
    print(f'{game_title} {game_version} {game_subversion}\n')

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

def loop_through_inventory(inventory, align = True):
    if align:
        maxNumberLength = 0
        maxNameLength   = 0
        maxPriceLength  = 0
        for i in range(len(inventory)):
            if len(str(i + 1)) > maxNumberLength:
                maxNumberLength = len(str(i + 1))
            if len(inventory[i].name) > maxNameLength:
                maxNameLength = len(inventory[i].name)
            if len(str(inventory[i].value)) > maxPriceLength:
                maxPriceLength = len(str(inventory[i].value))
        for i in range(len(inventory)):
            spaces      = ' '
            nameSpaces  = ' '
            priceSpaces = ' '
            if len(str(i + 1)) < maxNumberLength:
                spaces      = (maxNumberLength - len(str(i + 1)) + 1) * ' '
            if len(inventory[i].name) < maxNameLength:
                nameSpaces  = (maxNameLength - len(inventory[i].name) + 1) * ' '
            if len(str(inventory[i].value)) < maxPriceLength:
                priceSpaces = (maxPriceLength - len(str(inventory[i].value)) + 1) * ' '
            print(f'  {i + 1}){spaces}{inventory[i].name}{nameSpaces}[{inventory[i].value}{priceSpaces}{currency_symbol}]')
    else:
        for i in range(len(inventory)):
            print(f'  {i + 1}) {inventory[i].name}[{inventory[i].value} {currency_symbol}]')
