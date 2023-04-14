from data.constants import *

NUMBERS_NAME = [init_animation('',i) for i in range(0,10)]

''' This function show on the screen the high score. '''
def show_high_score(screen, high_score):
    numbers = []
    for num in NUMBERS_NAME:
        numbers.append(pygame.transform.scale(load_image(os.path.join("texts/numbers_score/", num)),(16,32)))
    high_score_str = str(high_score)
    score_surf = pygame.Surface((len(high_score_str) * numbers[0].get_width(), numbers[0].get_height()), pygame.SRCALPHA)
    for i, digit in enumerate(high_score_str):
        score_surf.blit(numbers[int(digit)], (i * numbers[0].get_width(), 0))

    screen.blit(score_surf, (10, 55))
    screen.blit(BEST_TEXT, ((len(high_score_str)* 20)+3,55))

''' This function show on the screen the score. '''
def show_score(screen, score):
    numbers = []
    for num in NUMBERS_NAME:
        numbers.append(load_image(os.path.join("texts/numbers_score/", num)))
    score_str = str(score)
    score_surf = pygame.Surface((len(score_str) * numbers[0].get_width(), numbers[0].get_height()), pygame.SRCALPHA)
    for i, digit in enumerate(score_str):
        score_surf.blit(numbers[int(digit)], (i * numbers[0].get_width(), 0))

    screen.blit(score_surf, (10, 10))
    screen.blit(M_TEXT, ((len(score_str)*28)+3,10))


''' This function show on the screen the current game coin amount. '''
def show_coins(screen, coins, y_pos):
    numbers = []
    for num in NUMBERS_NAME:
        numbers.append(load_image(os.path.join("texts/numbers_coin/", num)))
    coin_str = str(coins)
    coin_surf = pygame.Surface((len(coin_str) * numbers[0].get_width(), numbers[0].get_height()), pygame.SRCALPHA)
    for i, digit in enumerate(coin_str):
        coin_surf.blit(numbers[int(digit)], (i * numbers[0].get_width(), 0))

    screen.blit(coin_surf, (10, y_pos))
    screen.blit(COIN_IMG, ((len(coin_str)*22)+3,y_pos))
    

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

''' This function print a text on the screen to tell the user how to play the game'''
def how_to_play(screen, score):
    if score < 40:
        screen.blit(PRESS_SPACE, (250,160))
        screen.blit(PRESS_AD, (250,100))
