import pygame
import os
import random
import sys
from math import isclose
from os.path import abspath


pygame.init()
pygame.font.init() # import fonts
pygame.mixer.init() # import sound fx


# constants
FPS = 60     # game fps
BLACK = (0,0,0)
FIX_IMAGE_LIMIT = 50   
HIDDEN_LASERS_Y = -60
LASER_GAP = 55
COIN_SIZE = 30
PLAYER_HIT = pygame.USEREVENT + 1
DEFAULT_PLAYER_X_COLLISION = 10
DEFAULT_PLAYER_Y_COLLISION = 10

# screen resolution
WIDTH, HEIGHT = 900, 650  

# buttons scale
MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT = 200,80 
ARROW_BUTTON_WH = 50

# absolute file path
dir_path = os.path.dirname(os.path.realpath(__file__))
assets_dir_path = os.path.join(dir_path, "../Assets")


''' This function load an image. '''
def load_image(file_name):
    return pygame.image.load(os.path.join(assets_dir_path, file_name ))

''' This function load a sound. '''
def load_sound(file_name):
    return pygame.mixer.Sound(os.path.join(assets_dir_path ,file_name))

''' This function load an image animation. '''
def init_animation(name, num):
    return str(name + str(num) + '.png')

# images
    # obstacles images
OBS_IMG1 = load_image('zappers_animation/vertical_zapper1.png')
OBS_IMG2 = load_image('zappers_animation/horizontal_zapper1.png')
PRE_LASERS = load_image('lasers_animation/pre_lasers.png')
    # default pictures for the players
JETPACK_OFF_MALE = pygame.transform.scale(load_image('boy_animation_jetpack/player.png'), (60, 75))
JETPACK_OFF_FEMALE = pygame.transform.scale(load_image('skins/playerGirl.png'), (75, 90))
JETPACK_OFF_SHREK = pygame.transform.scale(load_image('skins/shrek.png'), (75,90))
    # backgrounds
MENU_BG_IMG = pygame.transform.scale(load_image('backgrounds/main_menu_bg.png'), (WIDTH,HEIGHT))
COSTUMES_BG_IMG = pygame.transform.scale(load_image('backgrounds/costumes_bg2.png'), (WIDTH,HEIGHT))
GAME_BG = pygame.transform.scale(load_image('backgrounds/bg/map1.png'), (2048,650)) #2000
    # skins to display in the costumes shop
DEFAULT_MALE = pygame.transform.scale(load_image('boy_animation_jetpack/player.png'), (150,200))
DEFAULT_FEMALE = pygame.transform.scale(load_image('skins/playerGirl.png'), (150,200))
SHREK_SKIN = pygame.transform.scale(load_image('skins/shrek.png'), (250,200))
    # text font
M_TEXT = load_image('texts/ingame_text/M.png')
BEST_TEXT = pygame.transform.scale(load_image('texts/ingame_text/best.png'), (80,30))
COIN_IMG = pygame.transform.scale(load_image('coins/coin1.png'),(30,30))



# buttons images
    # costumes shop buttons
BUY_BUTTON = pygame.transform.scale(load_image('buttons/buy_button_new.png'), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
SELECT_BUTTON = pygame.transform.scale(load_image('buttons/select_button_new.png'), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
SELECTED_BUTTON = pygame.transform.scale(load_image('buttons/skin_selected_button_new.png'), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
MAIN_MENU_BUTTON = pygame.transform.scale(load_image('buttons/main_menu_button.png'), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
RIGHT_ARROW = pygame.transform.scale(load_image('buttons/right_arrow.png'), (50,50))
RIGHT_ARROW_HOVER = pygame.transform.scale(load_image('buttons/right_arrow_hover.png'), (50,50))
LEFT_ARROW = pygame.transform.scale(load_image('buttons/left_arrow.png'), (50,50))
LEFT_ARROW_HOVER = pygame.transform.scale(load_image('buttons/left_arrow_hover.png'), (50,50))
    # main menu buttons
QUIT_MENU_NO_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/quit_button_no_hover.png'), (MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT))
QUIT_MENU_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/quit_button_hover.png'), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
PLAY_MENU_NO_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/play_button_no_hover.png'), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
PLAY_MENU_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/play_button_hover.png'), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
COSTUMES_MENU_NO_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/costumes_no_hover.png'), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
COSTUMES_MENU_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/costumes_hover2.png'), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
    # game paused buttons
SPEAKER_OFF_BUTTON = pygame.transform.scale(load_image('buttons/speakerOFF_button.png'), (60,60))
SPEAKER_OFF_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/speakerOFF_hover_button.png'), (60,60))
SPEAKER_ON_BUTTON = pygame.transform.scale(load_image('buttons/speakerON_button.png'), (60,60))
SPEAKER_ON_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/speakerON_hover_button.png'), (60,60))
RESUME_NO_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/resume_button.png'), (150,100))
RESUME_HOVER_BUTTON =pygame.transform.scale(load_image('buttons/resume_button_hover.png'), (150,100))
RETRY_BUTTON = pygame.transform.scale(load_image('buttons/retry_button.png'), (150,100))
RETRY_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/retry_button_hover.png'), (150,100))
QUIT_GAME_BUTTON = pygame.transform.scale(load_image('buttons/quit_game_button.png'), (150,100))
QUIT_GAME_HOVER_BUTTON = pygame.transform.scale(load_image('buttons/quit_game_button_hover.png'), (150,100))


# fonts / pre-made texts
SCORE_FONT = pygame.font.SysFont('New Athletic M54', 40)
GAME_OVER_TEXT = load_image('texts/game_over_img.png')
PRICE1000 = pygame.transform.scale(load_image('texts/1000price.png'), (100,100))
PRESS_SPACE = pygame.transform.scale(load_image('texts/press_space_hover.png'), (400,50))
PRESS_AD = pygame.transform.scale(load_image('texts/leftandright.png'), (400,50))

# sound settings
    #obstacles sound fx
START_OF_LASER = load_sound('Sounds/startLaser.mp3')
LASER_ON = load_sound('Sounds/laserOn.mp3')
MISSILE_WARNING = load_sound('Sounds/missile_warning.mp3')
MISSILE_LAUNCHED = load_sound('Sounds/missile_launched.mp3')
    #extras
MAN_SCREAM = load_sound('Sounds/man-scream.mp3')
COIN_SOUND = load_sound('Sounds/coin_sound.mp3')
    #game music
MENU_MUSIC = load_sound('Sounds/remix.mp3')
GAME_OVER_SOUND = load_sound('Sounds/game-over-sound.mp3')
GAME_MUSIC = load_sound('Sounds/game_music.mp3')
