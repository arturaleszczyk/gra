# from pgzero.builtins import Actor, animate
# from random import randint, shuffle #shuffle miesza listę
# from map import get_possible_directions
# from time import time
#
# ghost_should_move = 4 # 4 - duch ma sie ruszać0 - nie
#
# def ghost_should_move_up():
#     global ghost_should_move
#     ghost_should_move +=1 # zwiększamy o jeden
# class Ghost:
#     def __init__(self): # pozycja każdego ducha (4 duchy )
#         self.ghosts = [Actor(f'ghost{i}', pos=(250+(i*20), 370), anchor=(14, 8)) for i in range(1, 5)] # dla każdego ducha tworzymy aktora, ustawiamy pozycję, każdy gdzie indziej to x natomiast Y jest stałe
#         ghost_types = ['predator', 'normal', 'normal', 'prey']   # typy naszych duchów jeden goni dwa chodzą losowo czwarty ucieka
#         shuffle(ghost_types) # mieszamy listę ghost_types
#         for ghost in self.ghosts:
#             ghost.dir = randint(0, 3)
#             ghost.last_dir = -100
#             ghost.in_center = True
#             ghost.decide_point = 0, 8
#             ghost.g_type = ghost_types.pop()
#         self.disable_ghost_image = 'ghost5'   # piąty duch, kiedy zostanie zabrany bonus
#         self.enable = True # wszystkie duchy włączone
#         self.disable_time = 0 # po zabraniu bonusu duchy są wyłączone
#         self.ghost_moves = (18, 0), (0, -18), (-18, 0), (0, 18)# jakie mają kierunku prawo góra lewo dół (x,y) (1,0) x - rusza się w prawo lewo y - góra dół
#         self.ghost_speed = 3  # prędkość duchów
#
#     def diable_ghost(self):
#         self.enable = False
#         self.disable_time = time()
#         # kiedy duchy są niekatywne mają inny image
#         for ghost in self.ghosts:
#             ghost.image = self.disable_ghost_image # w tym momencie 4 pozostałe stają się ghost5
#
#     # duchy aktywne
#
#     def enable_ghost(self):
#         self.enable = True
#         self.disable_time = 0
#         for i, ghost in enumerate(self.ghosts):
#             ghost.image = f'ghost{i}'
#
#     def draw(self):
#         for ghost in self.ghosts:
#             ghost.draw()
#
#     def ghost_in_center(self):
#         for ghost in self.ghosts:
#             if 231 < ghost.x < 370 and 257 + 80 < ghost.y < 337+80:
#                 ghost.in_center = True
#             else:
#                 ghost.in_center = False
#
#     def update(self, pacman_pos):
#         self.ghost_in_center()
#         self.move_ghost(pacman_pos)
#         for ghost in self.ghosts:
#             ghost.last_dir = ghost.dir
#
#     @staticmethod
#     def distance(ghost_pos, pacman_pos): # sprawdzamy dystans pomiędzy
#         return ((ghost_pos[0]-pacman_pos[0])**2 + (ghost_pos[1]-pacman_pos[1])**2)**0.5 # pozycje x i y
#
#     def move_ghost(self, pacman_pos): # wykonujemy animację, jeżeli jest mniej niż 4 to funkcja nie jest wykonywana
#         global ghost_should_move
#         if ghost_should_move < 4:
#             return
#         ghost_should_move = 0
#         for ghost in self.ghosts: # dla każdego ducha
#             directions = get_possible_directions(ghost) # obieramy kierunek gdzie otrzymujemy listę możliwych kierunków
#             if ghost.in_center and directions[1]:
#                 ghost.dir = 1
#             elif ghost.g_type == 'normal' or randint(1,50) % 5 == 0: # jeżeli ghost jest normalny lub pozostały typ i wylosuje podzielną przez 5 to kierunek musi zostać wylosowany
#                 ghost.dir = randint(0, 3) # losowanie w którą stronę idzie
#
#
#                 while directions[ghost.dir] == 0 or (abs(ghost.last_dir - ghost.dir) == 2 and directions.count(1) > 1): # jeżeli tafimy na brak ruchu czyli 0 losujemy ponownie tak samo jeżeli został wylosowany kierunek powrotny losowanie jest ponowione
#                     ghost.dir = randint(0, 3)
#             elif ghost.g_type == 'predator' or ghost.g_type == 'prey':
#                 # sprawdzamy który kierunek jest właściwy czyli ten w którym łapie pacmana
#                 best_direction = None
#                 for i, direction in enumerate(directions):
#                     if not directions:
#                         continue
#                     if abs(ghost.last_dir - i) == 2 and directions.count(1) > 1:
#                         continue
#                     if best_direction is None:
#                         best_direction = i # sprawdzenie kierunku
#
#
#                     else:
#                         # sprawdzamy gdzie ghost będzie jak pójdzie do góry
#                         current_best_pos_x = ghost.x + self.ghost_moves[best_direction][0]
#                         current_best_pos_y = ghost.y + self.ghost_moves[best_direction][1]
#                         current_best_pos = (current_best_pos_x, current_best_pos_y)
#                         new_pos_x = ghost.x + self.ghost_moves[i][0]
#                         new_pos_y = ghost.y + self.ghost_moves[i][1]
#                         new_pos = (new_pos_x, new_pos_y)
#                         current_distance = self.distance(current_best_pos, pacman_pos)
#                         new_distance = self.distance(new_pos,pacman_pos)
#                         if ghost.g_type == 'predator':
#                             if new_distance < current_distance:
#                                 best_direction = i
#                         if ghost.g_type == 'prey':
#                             if new_distance > current_distance:
#                                 best_direction = i
#                 ghost.dir = best_direction
#             animate(ghost, pos=(ghost.x + self.ghost_moves[ghost.dir][0], # pozycja ducha to to gdzie jest plus kierunek 1 do góry współrzędna 0 to jest (18, 0) czyli ma wstawione 0 (y)
#                                 ghost.y + self.ghost_moves[ghost.dir][1]), # tutaj jest współrzędna 1 i to jest self.ghost_moves = (18, 0), (0, -18), (-18, 0), (0, 18)  -> (0, -18) czyli ma wstawione -18 (y)
#                     duration=1/self.ghost_speed, tween='linear', on_finished=ghost_should_move_up) # wybieramy współrzędną X i razy 20

from pgzero.builtins import Actor, animate
from random import randint, shuffle
from map import get_possible_directions
from time import time

ghost_should_move = 4  # 4 - YES, 0 - NO


def ghost_should_move_up():
    global ghost_should_move
    ghost_should_move += 1


class Ghost:
    def __init__(self):
        self.ghosts = [Actor(f'ghost{i}', pos=(250+(i*20), 370), anchor=(14, 8)) for i in range(1, 5)]
        ghost_types = ['predator', 'normal', 'normal', 'prey']
        shuffle(ghost_types)
        for ghost in self.ghosts:
            ghost.dir = randint(0, 3)
            ghost.last_dir = -100
            ghost.in_center = True
            ghost.decide_point = 0, 8
            ghost.g_type = ghost_types.pop()
        self.disable_ghost_image = 'ghost5'
        self.enable = True
        self.disable_time = 0
        self.ghost_moves = (18, 0), (0, -18), (-18, 0), (0, 18)
        self.ghost_speed = 3

    def disable_ghost(self):
        self.enable = False
        self.disable_time = time()
        for ghost in self.ghosts:
            ghost.image = self.disable_ghost_image

    def enable_ghost(self):
        self.enable = True
        self.disable_time = 0
        for i, ghost in enumerate(self.ghosts):
            ghost.image = f'ghost{i}'

    def ghost_in_center(self):
        for ghost in self.ghosts:
            if 231 < ghost.x < 370 and 257+80 < ghost.y < 337+80:
                ghost.in_center = True
            else:
                ghost.in_center = False

    def draw(self):
        for ghost in self.ghosts:
            ghost.draw()

    def update(self, pacman_pos):
        self.ghost_in_center()
        self.move_ghost(pacman_pos)
        for ghost in self.ghosts:
            ghost.last_dir = ghost.dir

    @staticmethod
    def distance(ghost_pos, pacman_pos):
        return ((ghost_pos[0]-pacman_pos[0])**2 + (ghost_pos[1]-pacman_pos[1])**2)**0.5

    def move_ghost(self, pacman_pos):
        global ghost_should_move
        if ghost_should_move < 4:
            return
        ghost_should_move = 0
        for ghost in self.ghosts:
            directions = get_possible_directions(ghost)
            if ghost.in_center and directions[1]:
                ghost.dir = 1
            elif ghost.g_type == 'normal' or (ghost.g_type == 'predator' and randint(1, 50) % 5 == 0) or \
                    (ghost.g_type == 'prey' and randint(1, 50) % 10 == 0):
                ghost.dir = randint(0, 3)
                while directions[ghost.dir] == 0 or (abs(ghost.last_dir - ghost.dir) == 2 and directions.count(1) > 1):
                    ghost.dir = randint(0, 3)
            elif ghost.g_type == 'predator' or ghost.g_type == 'prey':
                best_direction = None
                for i, direction in enumerate(directions):
                    if not direction:
                        continue
                    if abs(ghost.last_dir - i) == 2 and directions.count(1) > 1:
                        continue
                    if best_direction is None:
                        best_direction = i
                    else:
                        current_best_pos_x = ghost.x + self.ghost_moves[best_direction][0]
                        current_best_pos_y = ghost.y + self.ghost_moves[best_direction][1]
                        current_best_pos = (current_best_pos_x, current_best_pos_y)
                        new_pos_x = ghost.x + self.ghost_moves[i][0]
                        new_pos_y = ghost.y + self.ghost_moves[i][1]
                        new_pos = (new_pos_x, new_pos_y)
                        current_distance = self.distance(current_best_pos, pacman_pos)
                        new_distance = self.distance(new_pos, pacman_pos)
                        if ghost.g_type == 'predator':
                            if new_distance < current_distance:
                                best_direction = i
                        if ghost.g_type == 'prey':
                            if new_distance > current_distance:
                                best_direction = i
                ghost.dir = best_direction
            animate(ghost, pos=(ghost.x + self.ghost_moves[ghost.dir][0],
                                ghost.y + self.ghost_moves[ghost.dir][1]),
                    duration=1/self.ghost_speed, tween='linear', on_finished=ghost_should_move_up)
