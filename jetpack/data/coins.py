from tkinter import Y
from .constants import *
from .coin import *

class Coins():
    def __init__(self,type, pattern):
        self.pattern = pattern
        self.type = type
        self.reset()
    
    # reset the fart right coin coordinate
    def reset(self):
        if self.type == 1:
            self.far_right_x = self.pattern[0].rect.x + 150
        if self.type == 2:
            self.far_right_x = self.pattern[0].rect.x + 240
        reset_coin_positions(self)

    def update(self, death, score):
        #updating coin speed according to the obstacle speed
        coins_speed_timing = 50
        if score >= 300:
            coins_speed_timing = 80
        if score >= 1300:
            coins_speed_timing = 100
        
        # the coins are moving only if the player is alive
        if death == False:
            for coin in self.pattern:
                coin.rect.x -= coin.speed
                if score%coins_speed_timing == 0:
                    coin.increase_speed += 0.5
                if coin.increase_speed >= 10:
                    coin.speed += 1
                    coin.increase_speed = 0
            
            self.far_right_x -= coin.speed
        if self.far_right_x < 0:
            reset_coin_positions(self)

            


    def draw(self, screen):
        
        for coin in self.pattern:
            coin.draw(screen)
            coin.update()
        

    #def move_coins(self, death):
        
        

def get_pattern( type, x, y):
    coins = []
       
    if type == 1:  # this pattern contain 5 in a row, 3 in a col (basic rectangle)
        coins = [
                    Coin(x,y), Coin(x+30,y), Coin(x+60,y), Coin(x+90,y), Coin(x+120,y),
                    Coin(x,y+30), Coin(x+30,y+30), Coin(x+60,y+30), Coin(x+90,y+30), Coin(x+120,y+30),
                    Coin(x,y+60), Coin(x+30,y+60), Coin(x+60,y+60), Coin(x+90,y+60), Coin(x+120,y+60)
                ]
    if type == 2: # this pattern contatin 8 in a row, 3 in a col
        coins = [
                    Coin(x,y), Coin(x+30,y), Coin(x+60,y), Coin(x+90,y), Coin(x+120,y), Coin(x+150,y), Coin(x+180,y), Coin(x+210,y),
                    Coin(x,y+30), Coin(x+30,y+30), Coin(x+60,y+30), Coin(x+90,y+30), Coin(x+120,y+30), Coin(x+150,y+30), Coin(x+180,y+30), Coin(x+210,y+30),
                    Coin(x,y+60), Coin(x+30,y+60), Coin(x+60,y+60), Coin(x+90,y+60), Coin(x+120,y+60), Coin(x+150,y+60), Coin(x+180,y+60), Coin(x+210,y+60)
                ]
        
    return coins


def reset_coin_positions(coins):
    if coins.type == 1:
        count_x = 1
        count_y = 1
        x = random.randint(WIDTH+WIDTH//2, WIDTH*2)
        y = random.choice([150, 350, 500])
        for coin in coins.pattern:
            coin.show_image = True
            if count_x == 6:
                count_x = 1
                count_y += 1
            coin.rect.x = x + (30*count_x)
            coin.rect.y = y + (30*count_y)
            count_x += 1
    
    if coins.type == 2:
        count_x = 1
        count_y = 1
        x = random.randint(WIDTH, WIDTH+WIDTH//2)
        y = random.choice([150, 350, 500])
        for coin in coins.pattern:
            coin.show_image = True
            if count_x == 9:
                count_x = 1
                count_y += 1
            coin.rect.x = x + (30*count_x)
            coin.rect.y = y + (30*count_y)
            count_x += 1
    
    if coins.type == 1:
        coins.far_right_x = coins.pattern[0].rect.x + 150
    if coins.type == 2:
        coins.far_right_x = coins.pattern[0].rect.x + 240

def draw_coins(coins, screen):
    for coins_pattern in coins:
        coins_pattern.draw(screen)
    
def update_coins_positions(coins, death, score):

    for coins_pattern in coins:
        coins_pattern.update(death,score)
        

''' NEED THIS FOR COINS CLASS UPDATE PATTERNS
    if self.rect.x + self.rect.width < 0:
            self.rect.x = random.choice([WIDTH+50, WIDTH+300, WIDTH+900])
            self.rect.y = random.choice([150, 350, 550])
'''