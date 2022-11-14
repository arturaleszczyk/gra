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
        for x in range(0, 600, 1):
            for y in range(0, 600, 1):
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
                self.coins.append(new_coin)
    def draw_coins(self):
        for coin in self.coins:
            coin.draw()

    # jakie jeszcze będą monety

    def coins_to_draw(self):
        coins = []
        for coin in self.coins:
            coins.append(coin)
        return coins

