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
        if self.type == 2 or self.type == 3:
            self.far_right_x = self.pattern[0].rect.x + 240
        # Resetting all the single coins coordinates.
        reset_coin_positions(self)


    ''' This function updates the speed of the coins and reset the coins pattern as soon as the coins disapear. '''
    def update(self, death, score, score_timing_start):
        # Setting the coins speed that relies on the score progress.
        coins_speed_timing = 50
        if score >= score_timing_start+300:
            coins_speed_timing = 80
        if score >= score_timing_start+1300:
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
    def draw(self, screen, score_timing_start):
        for coin in self.pattern:
            coin.draw(screen)
            coin.update()
        

''' This function return a chosen type we want to be as the coins pattern'''
def get_pattern( type, x, y):
    coins = []
    if type == 1:  # This pattern contain 5 coins in a row and 3 coins in a col
        coins = [ Coin(x,y) for i in range (15) ]
    if type == 2: # This pattern contatin 8 coins in a row and 3 coins in a col
        coins = [ Coin(x,y) for i in range (24) ]
    if type == 3: # This pattern creates an hearth shape coins
        coins = [ Coin(x,y) for i in range (14) ]
    return coins


''' This function reset the coins positions on the screen in a random position. '''
def reset_coin_positions(coins):

    limit = 0
    if coins.type == 1:
        limit = 6
    if coins.type == 2:
        limit = 9
    
    count_x = 1
    count_y = 1
    x = random.randint(WIDTH+WIDTH//2, WIDTH*3)
    y = random.choice([150, 350, 500])

    if coins.type == 1 or coins.type == 2:
        for coin in coins.pattern:
            coin.show_image = True
            if count_x == limit:
                count_x = 1
                count_y += 1
            coin.rect.x = x + (30*count_x)
            coin.rect.y = y + (30*count_y)
            count_x += 1
    
    if coins.type == 3:
        y = random.choice([200, 350, 450])
        heart_shape_positions = [
                        (30,0),(60,0),(120,0),(150,0),
                        (0,30),(90,30),(180,30), 
                        (0,60),(180,60), 
                        (30,90),(150,90), 
                        (60,120),(120,120),
                        (90,150)
                    ]
        i=0
        for coin in coins.pattern:
            coin.show_image = True
            coin.rect.x = x + heart_shape_positions[i][0]
            coin.rect.y = y+ heart_shape_positions[i][1]
            i=i+1
    
    # Reset the far right coin position variable
    far_right_x_reset = 0
    if coins.type == 1: far_right_x_reset = 150
    if coins.type == 2: far_right_x_reset = 240
    if coins.type == 3: far_right_x_reset = 210
    coins.far_right_x = coins.pattern[0].rect.x + far_right_x_reset


''' This function change coins speed'''
def change_coin_speed(coins_list, speed):
    for coins in coins_list:
        for coin in coins.pattern:
            coin.speed = speed


''' This function draw the coins pattern on the screen. '''
def draw_coins(coins, screen,score_timing_start):
    for coins_pattern in coins:
        coins_pattern.draw(screen,score_timing_start)


''' This function update the coins position. '''
def update_coins_positions(coins, death, score,score_timing_start):
    for coins_pattern in coins:
        coins_pattern.update(death,score,score_timing_start)
        

''' This function collect the coins to the player. '''
def coin_collect(player, coins_type, coins_amount):
    for coins in coins_type:
        for coin in coins.pattern:
            if player.rect.colliderect(coin.rect) and coin.show_image:
                COIN_SOUND.play()
                coin.show_image = False
                coins_amount+=1

    return coins_amount
    