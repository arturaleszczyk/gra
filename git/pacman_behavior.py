from pgzero.builtins import Actor

class Packman:
    def __int__(self, keys):
        self.images = ['pacman_o','pacman_or','pacman_c','pacman_cr'] # poszczególne wyświetlenie pacmana
        self.keys = keys
        self.keys_active = { 'right': False, 'up': False, 'left': False,'down': False, }
        self.pacman = Actor('pacman_o')
        self.pacman.x = 290
        self.pacman.y = 570
        self.lives = 3

# moment kiedy przycisk klawiatury jest wciśnięty
    def on_key_down(self, key):
        if key == self.keys.RIGHT:
            self.keys_active['right'] = True
        if key == self.keys.UP:
            self.keys_active['up'] = True
        if key == self.keys.LEFT:
            self.keys_active['left'] = True
        if key == self.keys.DOWN:
            self.keys_active['down'] = True

# brak wciśniętego przycisku na klawiaturze

    def on_key_up(self, key):
        if key == self.keys.RIGHT:
            self.keys_active['right'] = False
        if key == self.keys.UP:
            self.keys_active['up'] = False
        if key == self.keys.LEFT:
            self.keys_active['left'] = False
        if key == self.keys.DOWN:
            self.keys_active['down'] = False

    def draw(self, screen): # umieszczenie pacmana na planszy
        self.pacman.draw()
        for live in range(self.lives): # ilość żyć naszego pacmana
            screen.blit("pacman_o", (10+live*32, 40))


    def move_pressed(self): # sprawdzenie czy jedna z wartości ma True: self.keys_active = {'left': False, 'right': False, 'down': False, 'up': False}
        pressed = any(value for value in self.keys_active.values())
        return pressed # zwracamy True or False

    def update(self): # wykonywanie działań w zależności od tego czy jest przycisk wciśnięty czy też nie takich jak zamykanie otwieranie buzi pacmana
        move_pressed = self.move_pressed()
        # typy obrazków

        straight_pacman_image ='pacman_o' # normalne położenie
        flipped_pacman_image = 'pacman_or' # odwrócone położenie
        if self.keys_active.values['right']:     # jeżeli jest w prawo
            self.pacman.x +=1
            self.pacman.image = straight_pacman_image # normalne położenie
            self.pacman.angle = 0 # bez obrotu



