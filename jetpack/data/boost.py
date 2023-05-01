from data.constants import *
from data.manage_text import *
from data.coins import *

class Boost(object):
    def __init__(self, button, type):
        self.type = type # Blue / Purple / Heart
        self.amount = 0# 0,....,infinity
        self.activate = False
        self.button = button
        self.price = price_check(self)
    


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
                return 1
                

    # resetting the rectange to the menu.
    boost.button.rect = RED_FIRE_BOOST_MENU_RECT
    return 1 if boost.activate else 0
                
                
''' This function activate speed boost. '''
def activate_boost( map, coins, lasers, missiles, score_timing_start):
                # speed the map
                map.speed = 8
                # speed the coins
                change_coin_speed(coins, 8)

                for laser in lasers:
                    laser.laser_timing = score_timing_start + 170
                for missile in missiles:
                    missile.missile_timing = score_timing_start + 70


''' This function deactivate speed boost. '''
def deactivate_boost(red_fire_boost, map, coins, zappers):
                red_fire_boost.activate = False
                # map reset speed
                map.speed=1.2
                map.speed_increase=0
                # coin reset speed
                change_coin_speed(coins, 2)
                # zapper spawning
                for zapper in zappers:
                    zapper.reset()
