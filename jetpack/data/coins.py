from .constants import *
from .coin import *

class Coins():
    ''' This class represents a coins pattern.   '''
    def __init__(self,type, pattern):
        self.pattern = pattern
        self.type = type
        self.reset()
    

    ''' This function reset all the coins coordinates.   '''
    def reset(self):
        # Resetting the far_right_x of the far right coin.
        if self.type == 1:
            self.far_right_x = self.pattern[0].rect.x + 150
        if self.type == 2:
            self.far_right_x = self.pattern[0].rect.x + 240
        # Resetting all the single coins coordinates.
        reset_coin_positions(self)


    ''' This function updates the speed of the coins and reset the coins pattern as soon as the coins disapear. '''
    def update(self, death, score):
        # Setting the coins speed that relies on the score progress.
        coins_speed_timing = 50
        if score >= 300:
            coins_speed_timing = 80
        if score >= 1300:
            coins_speed_timing = 100
        
        # The coins are moving only if the player is alive.
        if death == False:
            # Updating the coins speed.
            for coin in self.pattern:
                coin.rect.x -= coin.speed
                if score%coins_speed_timing == 0:
                    coin.increase_speed += 0.5
                if coin.increase_speed >= 10:
                    coin.speed += 1
                    coin.increase_speed = 0
            self.far_right_x -= coin.speed
            
        # When the far right coin pass the screen we will respawn the coins.
        if self.far_right_x < 0:
            reset_coin_positions(self)

            
    ''' This function draw the coins and update them to the screen  '''
    def draw(self, screen):
        for coin in self.pattern:
            coin.draw(screen)
            coin.update()
        

''' This function return a chosen type we want to be as the coins pattern'''
def get_pattern( type, x, y):
    coins = []
    if type == 1:  # This pattern contain 5 coins in a row and 3 coins in a col
        coins = [
                    Coin(x,y),    Coin(x+30,y),    Coin(x+60,y),    Coin(x+90,y),    Coin(x+120,y),
                    Coin(x,y+30), Coin(x+30,y+30), Coin(x+60,y+30), Coin(x+90,y+30), Coin(x+120,y+30),
                    Coin(x,y+60), Coin(x+30,y+60), Coin(x+60,y+60), Coin(x+90,y+60), Coin(x+120,y+60)
                ]
    if type == 2: # This pattern contatin 8 coins in a row and 3 coins in a col
        coins = [
                    Coin(x,y),    Coin(x+30,y),    Coin(x+60,y),    Coin(x+90,y),    Coin(x+120,y),    Coin(x+150,y),    Coin(x+180,y),    Coin(x+210,y),
                    Coin(x,y+30), Coin(x+30,y+30), Coin(x+60,y+30), Coin(x+90,y+30), Coin(x+120,y+30), Coin(x+150,y+30), Coin(x+180,y+30), Coin(x+210,y+30),
                    Coin(x,y+60), Coin(x+30,y+60), Coin(x+60,y+60), Coin(x+90,y+60), Coin(x+120,y+60), Coin(x+150,y+60), Coin(x+180,y+60), Coin(x+210,y+60)
                ]
    return coins


''' This function reset the coins positions on the screen in a random position. '''
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
    
    # Reset the far right coin position variable
    if coins.type == 1:
        coins.far_right_x = coins.pattern[0].rect.x + 150
    if coins.type == 2:
        coins.far_right_x = coins.pattern[0].rect.x + 240


''' This function draw the coins pattern on the screen. '''
def draw_coins(coins, screen):
    for coins_pattern in coins:
        coins_pattern.draw(screen)


''' This function update the coins position. '''
def update_coins_positions(coins, death, score):
    for coins_pattern in coins:
        coins_pattern.update(death,score)
        

''' This function collect the coins to the player. '''
def coin_collect(player, coins_type, coins_amount):
    for coins in coins_type:
        for coin in coins.pattern:
            if player.rect.colliderect(coin.rect) and coin.show_image:
                COIN_SOUND.play()
                coin.show_image = False
                coins_amount+=1

    return coins_amount
    