import random

from modules.settings import *

englishLetters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

class Fish:
    def __init__(self):
        self.name = 'Unset'
        self.value = 0
        self.generate_name()
        self.generate_value()

    def generate_name(self):
        firstLetter  = random.randint(0, len(englishLetters) - 1)
        firstLetter  = englishLetters[firstLetter].upper()
        middleNumber = str(random.randint(0, 9))
        secondLetter = random.randint(0, len(englishLetters) - 1)
        secondLetter = englishLetters[secondLetter].upper()
        self.name    = firstLetter + middleNumber + secondLetter

    def generate_value(self):
        self.value = random.randint(1, 10)
