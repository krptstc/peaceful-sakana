from modules.functions import *
from modules.menus     import *

if __name__ == '__main__':
    clear_screen()
    print_game_title()
    view_menu(main_menu)
    selection = pick_from_menu(main_menu)
    print(f'You picked option {selection}.')
