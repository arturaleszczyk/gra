from pacman_behavior import Packman
import pgzrun
from pgzero.builtins import Actor, keyboard
from pgzero.screen import Screen

WIDTH = 600
HEIGHT = 660
keys: keyboard
screen: Screen

pacman = Packman(keys)
def draw():
    pacman.draw(screen)


def on_key_down(key):
    pacman.on_key_down(key)

def on_key_up(key):
    pacman.on_key_up(key)

def update():
    pacman.update()

pgzrun.go()

