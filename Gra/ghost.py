from pgzero.builtins import Actor, animate
from random import randint
from map import get_possible_directions
from time import time

ghost_should_move = 4 # 4 - duch ma sie ruszać0 - nie

def ghost_should_move_up():
    global ghost_should_move
    ghost_should_move +=1
class Ghost:
    def __init__(self): # pozycja każdego ducha (4 duchy )
        self.ghosts = [Actor(f'ghost{i}', pos=(250+(i*20), 370), anchor=(14, 8)) for i in range(1, 5)] # dla każdego ducha tworzymy aktora, ustawiamy pozycję, każdy gdzie indziej to x natomiast Y jest stałe
        for ghost in self.ghosts:
            ghost.dir = randint(0, 3)
            ghost.last_dir = -100
            ghost.status = 0
            ghost.in_center = True
            ghost.decide_point = 0, 8
        self.disable_ghost_image = 'ghost5'   # piąty duch kiedy zostanie zabrany bonus
        self.enable = True # wszystkie duchy włączone
        self.disable_time = 0 # po zabraniu bonusu duchy są wyłączone
        self.ghost_moves = (18, 0), (0, -18), (-18, 0), (0, 18)# jakie mają kierunku prawo góra lewo dół (x,y) (1,0) x - rusza się w prawo lewo y - góra dół
        self.ghost_speed = 3  # prędkość duchów

    def diable_ghost(self):
        self.enable = False
        self.disable_time = time()
        # kiedy duchy są niekatywne mają inny image
        for ghost in self.ghosts:
            ghost.image = self.disable_ghost_image # w tym momencie 4 pozostałe stają się ghost5

    # duchy aktywne

    def enable_ghost(self):
        self.enable = True
        self.disable_time = 0
        for i, ghost in enumerate(self.ghosts):
            ghost.image = f'ghost{i}'

    def draw(self):
        for ghost in self.ghosts:
            ghost.draw()

    def ghost_in_center(self):
        for ghost in self.ghosts:
            if 231 < ghost.x < 370 and 257 + 80 < ghost.y < 337+80:
                ghost.in_center = True
            else:
                ghost.in_center = False

    def update(self):
        self.ghost_in_center()
        self.move_ghost()
        for ghost in self.ghosts:
            ghost.last_dir = ghost.dir

    def move_ghost(self):
        global ghost_should_move
        if ghost_should_move < 4:
            return
        ghost_should_move = 0
        for ghost in self.ghosts:
            directions = get_possible_directions(ghost)
            ghost.dir = randint(0, 3) # losowanie w którą stronę idzie
            while directions[ghost.dir] == 0 or (abs(ghost.last_dir - ghost.dir) == 2 and directions.count(1) > 1): # jeżeli tafimy na brak ruchu czyli 0 losujemy ponownie
                ghost.dir = randint(0, 3)
            animate(ghost, pos=(ghost.x + self.ghost_moves[ghost.dir][0],
                                ghost.y + self.ghost_moves[ghost.dir][1]),
                    duration=1/self.ghost_speed, tween='linear', on_finished=ghost_should_move_up) # wybieramy współrzędną X i razy 20


