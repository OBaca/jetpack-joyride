from data.constants import *
from data.manage_text import *

class Boost(object):
    def __init__(self, button, type):
        self.type = type # Blue / Purple / Heart
        self.amount = 0# 0,....,infinity
        self.activate = False
        self.button = button
        self.price = price_check(self)
    


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
        # show boosts available
        ''' V '''  
        # stop spawning obstacles
        ''' V '''
        # put player in red fire skin and dont let the player move
        # @@ interseting - just blit red FIRE and ontop blit the player animation
        ''' X '''
        # increase the speed of the map
        ''' V '''
        # increase the score speed
        ''' V '''
        # if red boost activated then stop when you reach 150
        ''' V '''
        # reset the score speed and the map speed to normal
        ''' X '''
        # reset player skin
        ''' X '''
        return 0
        


''' This function check if a player can buy a boost and save it.'''
def boost_menu(boost, screen, player_coins):
        if player_coins >= 250:
            boost.amount +=1
            return player_coins-250
        else:
            not_enough_coins_to_buy(screen)
            return player_coins
    

''' This function check the price for the different boosts.'''
def price_check(boost):
    if boost.type == 'red':
        return 200
    if boost.type == 'blue':
        return 400
    else: 0
         

''' This function shows the boosts to the player at the beginning of the game.'''
def show_boost_list(screen, boost, score):
    # setting the rectangle to the game.
    boost.button.rect = RED_FIRE_BOOST_GAME_RECT

    
    if score <= 50 and boost.activate == False:
        # check if the player clicked on the boost to activate it.
        if boost.button.draw_button(screen, 'red-fire'):
            if boost.amount>0:
                boost.amount -= 1
                boost.activate = True
                print("activate boost")
                return 1
                


        
    # resetting the rectange to the menu.
    boost.button.rect = RED_FIRE_BOOST_MENU_RECT

    return 1 if boost.activate else 0
                
                
