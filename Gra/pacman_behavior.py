from pgzero.builtins import Actor
from time import time
from map import check_move_point

class Pacman:
    def __init__(self, keys):
        self.images = ["pacman_o", "pacman_or", "pacman_c", "pacman_cr", ]
        self.keys = keys
        self.pacman = Actor("pacman_o")
        self.pacman.keys_active = {'right': False, 'up': False, 'left': False, 'down': False}
        self.pacman.x = 290
        self.pacman.y = 580
        self.start_pos = self.pacman.x, self.pacman.y
        self.lives = 3
        self.teeth_time = 0.1
        self.teeth = False
        self.dt = None

# moment kiedy przycisk klawiatury jest wciśnięty
    def on_key_down(self, key):
        if key == self.keys.RIGHT:
            self.pacman.keys_active['right'] = True
        if key == self.keys.UP:
            self.pacman.keys_active['up'] = True
        if key == self.keys.LEFT:
            self.pacman.keys_active['left'] = True
        if key == self.keys.DOWN:
            self.pacman.keys_active['down'] = True



# brak wciśniętego przycisku na klawiaturze

    def on_key_up(self, key):
        if key == self.keys.RIGHT:
            self.pacman.keys_active['right'] = False
        if key == self.keys.UP:
            self.pacman.keys_active['up'] = False
        if key == self.keys.LEFT:
            self.pacman.keys_active['left'] = False
        if key == self.keys.DOWN:
            self.pacman.keys_active['down'] = False

    def draw(self, screen): # umieszczenie pacmana na planszy
        self.pacman.draw()
        for live in range(self.lives): # ilość żyć naszego pacmana
            screen.blit("pacman_o", (10 + live * 60, 20))


    def move_pressed(self): # sprawdzenie czy jedna z wartości ma True: self.keys_active = {'left': False, 'right': False, 'down': False, 'up': False}
        pressed = any(value for value in self.pacman.keys_active.values())
        if not pressed:
            self.teeth = False # zęby pacmana kiedy nie ma wciśniętego przycisku
            self.dt = None # powrót do ustawień początkowych
        return pressed # zwracamy True or False

    def update(self): # wykonywanie działań w zależności od tego czy jest przycisk wciśnięty czy też nie takich jak zamykanie otwieranie buzi pacmana
        move_pressed = self.move_pressed()
        if not move_pressed:
            return
        # czy pacman może się poruszać
        can_move = check_move_point(self.pacman)
        if not can_move:
            return

        if move_pressed and self.dt is None: # jeżeli jest przycisk naciśnięty i pacman jest w pozycji zamkniętej
            self.teeth = True
            self.dt = time() # czas kłapania dziobem
        if self.dt is not None: # jeżeli przycisk nie jest wciśnięty
            now = time()
            if now - self.dt > self.teeth_time: # sprawdzamy czy aktualny czas odjąć czas kiedy pokazaliśmy pacmana czy jest większy niż w momencie startu
                self.teeth = not self.teeth # jeżeli jest większy zmieniamy wygląd
                self.dt = now # aktualizacja czasu


        # typy obrazków
        straight_pacman_image = 'pacman_c' if self.teeth else 'pacman_o' # normalne położenie
        flipped_pacman_image = 'pacman_cr' if self.teeth else 'pacman_or' # odwrócone położenie
        if self.pacman.keys_active['right']:     # jeżeli jest w prawo
            self.pacman.x +=1
            self.pacman.image = straight_pacman_image # normalne położenie
            self.pacman.angle = 0 # bez obrotu
        if self.pacman.keys_active['up']:     # jeżeli jest w górę zmniejszamy w y o jeden
            self.pacman.y -=1
            self.pacman.image = straight_pacman_image # normalne położenie
            self.pacman.angle = 90 # obrót o 90stopni
        if self.pacman.keys_active['left']:     # jeżeli jest w lewo zmniejszamy x o jeden
            self.pacman.x -=1
            self.pacman.image = flipped_pacman_image # normalne położenie
            self.pacman.angle = 180 # obrót o 180stopni
        if self.pacman.keys_active['down']:     # jeżeli jest w dół zwiększamy y
            self.pacman.y +=1
            self.pacman.image = flipped_pacman_image # normalne położenie
            self.pacman.angle = 270 # obrót o 270stopni





