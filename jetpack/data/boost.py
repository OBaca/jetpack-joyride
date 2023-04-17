from data.constants import *
from data.manage_text import *

class Boost(object):
    def __init__(self, button):
        self.type = 'red'# Blue / Purple / Heart
        self.amount = 0# 0,....,infinity
        self.on = 0
        self.button = button
    

    '''def draw(self, screen):
        self.on =1'''

    
    '''def show_boost(self, score):
        if score == 50:
            self.on = 0
            return 0
        else:
            # draw the boost to the screen
                
            # if clickable then activate boost
            return 0
    '''

    def activate_speed_boost(self):
        # stop spawning obstacles
    
        # put player in Blue fire skin and dont let the player move
        # @@ interseting - just blit BLUE FIRE and ontop blit the player animation

        # increase the speed of the map

        # increase the score speed

        # if blue boost activated then stop when you reach 250

        # if purple boost activated then stop then you reach 500

        # reset the score speed and the map speed to normal

        # reset player skin

        return 0
        



def boost_menu(boost, screen, player_coins):
        if player_coins >= 250:
            boost.amount +=1
            
            print(boost.amount)
            return player_coins-250
        else:
            not_enough_coins_to_buy(screen)
            return player_coins
    
