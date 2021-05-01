import os
import pickle

from classes.player import Player

__author__ = 'krptstc'

if __name__ == '__main__':
    player = None
    if os.path.exists('data.pfsakana'):
        pickleInput = open('data.pfsakana', 'rb')
        loadedData  = pickle.load(pickleInput)
        player      = loadedData['player']
    else:
        player = Player()

    from modules.functions import *
    from modules.menus     import *

    home()
