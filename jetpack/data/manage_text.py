from data.constants import *

''' This function show on the screen the high score. '''
def show_high_score(screen, high_score):
    high_score_text = SCORE_FONT.render('HIGH SCORE: ' + str(high_score), 1, BLACK)
    screen.blit(high_score_text, (10,50))


''' This function show on the screen the score. '''
def show_score(screen, score):
    score_text = SCORE_FONT.render('SCORE: ' + str(score), 1, (202,193,53))
    screen.blit(score_text, (10,10))


''' This function show on the screen the current game coin amount. '''
def show_coins(screen, coins):
    coin_text = SCORE_FONT.render('COINS: ' + str(coins), 1, (202,193,53))
    screen.blit(coin_text, (10,90))
    

''' This function show on the screen the total amount of coins the user have. '''
def show_menu_coins(screen,coins_amount):
    coin_text = SCORE_FONT.render('COINS: ' + str(coins_amount), 1, (202,193,53))
    screen.blit(coin_text, (10,60))


''' This function show the game over text on the screen. '''
def show_game_over_text(screen):
    screen.blit(GAME_OVER_TEXT, (WIDTH//2 - (GAME_OVER_TEXT.get_width()//2) ,HEIGHT//2 - (GAME_OVER_TEXT.get_height()//2)))


''' This function show on the screen the text "not enough coins".  '''
def not_enough_coins_to_buy(screen):
    coin_text = SCORE_FONT.render('Not enough coins' , 1, (202,193,53))
    screen.blit(coin_text, (300,300))
