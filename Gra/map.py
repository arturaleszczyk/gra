# robimy ściany naszej mapy

from pygame import image, Color

# pobieramy kolor z obrazka

moveimage = image.load('Gra/images/move_map.png')


def check_move_point(pacman):
    move_x, move_y = 0,0

    if pacman.keys_active['right']:
        move_x = 1
    if pacman.keys_active['up']:
        move_y = -1
    if pacman.keys_active['left']:
        move_x = -1
    if pacman.keys_active['down']:
        move_y = 1

# jeżeli pacman wejdzie na kolor black ruch ma zostać zablokowany
    if moveimage.get_at((int(pacman.x+move_x), int(pacman.y+move_y-80))) != Color('black'):
        return False
    return True