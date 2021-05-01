from modules.settings import *

def view_menu(menu):
    print('')
    for i in range(len(menu)):
        print(f'{i + 1}) {menu[i]}')
    print('')

def print_game_title():
    print(f'{game_title} {game_version}')
