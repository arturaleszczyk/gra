from map import check_dot_point
from pgzero.builtins import Actor, Rect

# nazwy obrazków
# robimy monety
class Coin:
    def __init__(self):
        self.coin_name = 'coin'
        self.power_name = 'power_up'
        self.coins = []
        # przechodzimy po mapie 600 x 600 co jeden pix
        for x in range(20, 580, 1):
            for y in range(20, 580, 1):
                # sprawdzamy x i y
                where_check = x, y
                # sprawdzamy rodzaj kropki
                dot_type = check_dot_point(*where_check)
                # gdzie wstawiamy
                where_put = x, y + 80
                if dot_type == 0:
                    continue
                new_coin = None
                if dot_type == 1:
                    new_coin = Actor(self.coin_name, where_put, anchor=(13, 13) )
                    new_coin.type = 1
                if dot_type == 2:
                    new_coin = Actor(self.power_name, where_put, anchor=(13, 13) )
                    new_coin.type = 2
                new_coin.hidden = False
                self.coins.append(new_coin)
        self.left_coins = len(self.coins)
    def draw_coins(self):
        # rysujemy tylko odkryte
        for coin in self.coins_to_draw():
            coin.draw()

    # jakie jeszcze będą monety

    def coins_to_draw(self):
        coins = []
        for coin in self.coins:
            if not coin.hidden:
                coins.append(coin)
        return coins


        # wpisujemy informacje o pacmanie

    def check_collision(self, pacman):
        x, y, width, height = pacman.x, pacman.y, pacman.width, pacman.height
        # budujemy prostokąt obejmujący pacmana
        # x to jest endpoint pacmana / 2 ustawiamy na połowę długości
        rect = Rect(x - width / 2, y - height / 2, width, height)
        # sprawdzamy czy pacman ma kolizję z monetą
        for coin in self.coins_to_draw():
            # jeżeli pacman ma kolizję z monetą, ukrywamy monetę
            if coin.colliderect(rect):
                coin.hidden = True
                # jednocześnie zmniejszamy ilość monet
                self.left_coins -= 1
                if self.left_coins == 0:
                    return "won"
                if coin.type == 1:
                    return "coin"
                else:
                    return "powerup"
        return "None"
