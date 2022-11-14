from pacman_behavior import Pacman
import pgzrun
from pgzero.builtins import Actor, keyboard
from pgzero.screen import Screen
from ghost import Ghost
from coins import Coin



BLACK = (0,0,0)
GOLD = 255, 215, 0
WIDTH = 600
HEIGHT = 680
keys: keyboard
screen: Screen
POINTS = 0

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
    # rysujemy ile mamy punktów
    screen.draw.text(f'{POINTS}', color=GOLD, fontsize=50, fontname='bungee-regular',
                     topright=(WIDTH - 10, 10), owidth=1, ocolor=(100, 100, 100))


def on_key_down(key):
    pacman.on_key_down(key)


def on_key_up(key):
    pacman.on_key_up(key)

def update_by_coin():
    global POINTS
    # sprawdzamy czy jest wciśnięty klawisz pacmana
    if pacman.move_pressed():
        # jeżeli jest, sprawdzamy czy jest kolizja
        coin_type = coin.check_collision(pacman.pacman)
        # 3 rodzaje kolizji
        if coin_type == "coin":
            # o ile zwięlsza się nam punktacja
            POINTS += 10
        if coin_type == "powerup":
            pass
        if coin_type == "won":
            pass


def update():
    pacman.update()
    ghost.update(pacman.pacman.pos) # aktor klasy Pacman
    update_by_coin()


pgzrun.go()