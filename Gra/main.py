from pacman_behavior import Pacman
import pgzrun
from pgzero.builtins import Actor, keyboard
from pgzero.screen import Screen
from ghost import Ghost
from coins import Coin



BLACK = (0,0,0)
WIDTH = 600
HEIGHT = 680
keys: keyboard
screen: Screen

pacman = Pacman(keys)
ghost = Ghost()
coin = Coin()
color_map = Actor("colorful_map", pos=(0, 80), anchor=(0, 0)) # podłączenie mapy plus jej umieszczenie w oknie


def draw():
    screen.fill(BLACK)
    color_map.draw()
    pacman.draw(screen)
    ghost.draw()
    coin.draw_coins()


def on_key_down(key):
    pacman.on_key_down(key)


def on_key_up(key):
    pacman.on_key_up(key)


def update():
    pacman.update()
    ghost.update(pacman.pacman.pos) # aktor klasy Pacman


pgzrun.go()