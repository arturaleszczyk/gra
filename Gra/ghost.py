from pgzero.builtins import Actor, animate
from random import randint
from map import get_possible_directions


class Ghost:
    def __init__(self): # pozycja każdego ducha (4 duchy )
        self.ghosts = [Actor(f'ghost{i}', pos=(250+(i*20), 370)) for i in range(1, 5)] # dla każdego ducha tworzymy aktora, ustawiamy pozycję, każdy gdzie indziej to x natomiast Y jest stałe
        for ghost in self.ghosts:
            ghost.dir = randint(0, 3)
            ghost.status = 0
            ghost.in_center = True
            ghost.decide_point = 1, 1
        self.disable_ghost_image = 'ghost5'   # piąty duch kiedy zostanie zabrany bonus
        self.enable = True # wszystkie duchy włączone
        self.disable_time = 0 # po zabraniu bonusu duchy są wyłączone
        self.ghost_moves = (1, 0), (0, -1), (-1, 0), (0, 1)# jakie mają kierunku prawo góra lewo dół (x,y) (1,0) x - rusza się w prawo lewo y - góra dół
        self.ghost_speed = 3  # prędkość duchów



    def draw(self):
        for ghost in self.ghosts:
            ghost.draw()

    def update(self):
        self.move_ghost()

    def move_ghost(self):
        pass
