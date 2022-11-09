# robimy ściany naszej mapy

from pygame import image, Color

# pobieramy kolor z obrazka

moveimage = image.load('images/move_map.png')


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
# obsługa wyjścia pacmana z ekranu
    if pacman.x+move_x < 0:
        pacman.x = 576
        return True
    if pacman.x+move_x > 576:
        pacman.x = 0
        return True
# jeżeli pacman wejdzie na kolor black ruch ma zostać zablokowany
    if moveimage.get_at((int(pacman.x+move_x), int(pacman.y+move_y-80))) != Color('black'):
        return False
    return True

# kierunki poruszania się duchów
def get_possible_directions(ghost): # funkcja sprawdza gdzie duch doszedł oraz czy tam jest kolor black
    bw = 18 # wysokość korytarzy black width
    if ghost.in_center:
        bw = 20
    directions = [0,0,0,0] # kierunki right, up, left, down
    # obsługa wyjścia pacmana z ekranu
    if ghost.x - bw < 0:
        ghost.x = 576
    elif ghost.x + bw > 600:
        ghost.x = bw

    move_x, move_y = ghost.decide_point
    # punkty końcowe gdzie duch będzie po zakończeniu swojego ruchu
    dpx = ghost.x + move_x
    dpy = ghost.y + move_y

    if moveimage.get_at((int(dpx+bw), int(dpy-80))) == Color('black'):
        directions[0] = 1 # jeżeli jest tutaj dostępne czarne pole, duch może iść w prawo
    if moveimage.get_at((int(dpx), int(dpy-80-bw))) == Color('black'):
        directions[1] = 1
    if moveimage.get_at((int(dpx-bw), int(dpy-80))) == Color('black'):
        directions[2] = 1
    if moveimage.get_at((int(dpx), int(dpy-80+bw))) == Color('black'):
        directions[3] = 1
    return directions

