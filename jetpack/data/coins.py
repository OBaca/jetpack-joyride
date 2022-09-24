from .constants import *
from .coin import *

class Coins():
    def __init__(self, coin):
        self.far_right_x = 0
        self.top_left_x = 0
        self.pattern = self.get_pattern(random.randint(1,3), random.choice([WIDTH+50, WIDTH+300, WIDTH+900]), random.choice([150, 350, 550]))
        

    def get_pattern(self, type, x, y):
        if type == 1:  # this pattern contain 5 in a row, 3 in a col (basic rectangle)
            self.far_right_x = 120
            coins = [
                        Coin(x,y), Coin(x+30,y), Coin(x+60,y), Coin(x+90,y), Coin(x+120,y),
                        Coin(x,y+30), Coin(x+30,y+30), Coin(x+60,y+30), Coin(x+90,y+30), Coin(x+120,y+30),
                        Coin(x,y+60), Coin(x+30,y+60), Coin(x+60,y+60), Coin(x+90,y+60), Coin(x+120,y+60)
                    ]
        if type == 2: # this pattern contatin 8 in a row, 3 in a col
            self.far_right_x = 210
            coins = [
                        Coin(x,y), Coin(x+30,y), Coin(x+60,y), Coin(x+90,y), Coin(x+120,y), Coin(x+150,y), Coin(x+180,y), Coin(x+210,y),
                        Coin(x,y+30), Coin(x+30,y+30), Coin(x+60,y+30), Coin(x+90,y+30), Coin(x+120,y+30), Coin(x+150,y+30), Coin(x+180,y+30), Coin(x+210,y+30),
                        Coin(x,y+60), Coin(x+30,y+60), Coin(x+60,y+60), Coin(x+90,y+60), Coin(x+120,y+60), Coin(x+150,y+60), Coin(x+180,y+60), Coin(x+210,y+60)
                    ]




''' NEED THIS FOR COINS CLASS UPDATE PATTERNS
    if self.rect.x + self.rect.width < 0:
            self.rect.x = random.choice([WIDTH+50, WIDTH+300, WIDTH+900])
            self.rect.y = random.choice([150, 350, 550])
'''