# modules.py
import draw


def play_game():
    ...


def main():
    result = play_game()
    draw.draw_game(result)


# import current namespace
from draw import draw_game


def main():
    result = play_game()
    draw_game(result)


# import all module
from draw import *


def main():
    result = play_game()
    draw_game(result)


# custom import name
import draw as dr


def play_game():
    ...


def main():
    result = play_game()
    dr.draw_game(result)


# draw.py
def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...


def clear_screen(screen):
    ...


class Screen():
    ...


# initialize main_screen as a singleton
main_screen = Screen()
