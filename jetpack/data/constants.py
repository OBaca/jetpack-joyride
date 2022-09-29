import pygame
import os
import random
import sys
from math import isclose

pygame.font.init() # import fonts
pygame.mixer.init() # import sound fx

# constants
WIDTH, HEIGHT = 900, 650
MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT = 200,80
ARROW_BUTTON_WH = 50
FPS = 60
BLACK = (0,0,0)
FIX_IMAGE_LIMIT = 50
HIDDEN_LASERS_Y = -60
LASER_GAP = 55
COIN_SIZE = 30

PLAYER_HIT = pygame.USEREVENT + 1

# images
OBS_IMG1 = pygame.image.load(os.path.join('Assets', 'obstacle2.png'))
OBS_IMG2 = pygame.image.load(os.path.join('Assets', 'obstacle3.png'))
PRE_LASERS = pygame.image.load(os.path.join('Assets', 'lasers1.png'))


SPEAKER_OFF_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'speakerOFF_button.png')), (60,60))
SPEAKER_OFF_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'speakerOFF_hover_button.png')), (60,60))
SPEAKER_ON_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'speakerON_button.png')), (60,60))
SPEAKER_ON_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'speakerON_hover_button.png')), (60,60))

RESUME_NO_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons','resume_button.png')), (150,100))
RESUME_HOVER_BUTTON =pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons','resume_button_hover.png')), (150,100))
RETRY_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons','retry_button.png')), (150,100))
RETRY_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons','retry_button_hover.png')), (150,100))
QUIT_GAME_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons','quit_game_button.png')), (150,100))
QUIT_GAME_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons','quit_game_button_hover.png')), (150,100))
JETPACK_OFF_MALE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'player.png')), (60, 75))
JETPACK_OFF_FEMALE = pygame.transform.scale(pygame.image.load(os.path.join('Assets\skins', 'playerGirl.png')), (75, 90))


QUIT_MENU_NO_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("Assets\\buttons", 'quit_button_no_hover.png')), (MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT))
QUIT_MENU_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'quit_button_hover.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))

PLAY_MENU_NO_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'play_button_no_hover.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
PLAY_MENU_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'play_button_hover.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))

COSTUMES_MENU_NO_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'costumes_no_hover.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
COSTUMES_MENU_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'costumes_hover2.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))

MENU_BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'main_menu_bg.png')), (WIDTH,HEIGHT))
COSTUMES_BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'costumes_bg2.png')), (WIDTH,HEIGHT))
GAME_OVER_TEXT = pygame.image.load(os.path.join('Assets', 'game_over_img.png'))

RIGHT_ARROW = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'right_arrow.png')), (50,50))
RIGHT_ARROW_HOVER = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'right_arrow_hover.png')), (50,50))

LEFT_ARROW = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'left_arrow.png')), (50,50))
LEFT_ARROW_HOVER = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'left_arrow_hover.png')), (50,50))

# skins in the costumes shop
DEFAULT_MALE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'player.png')), (150,200))
DEFAULT_FEMALE = pygame.transform.scale(pygame.image.load(os.path.join('Assets\skins', 'playerGirl.png')), (150,200))
SHREK_SKIN = pygame.transform.scale(pygame.image.load(os.path.join('Assets\skins', 'shrek.png')), (250,200))

BUY_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'buy_button_new.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
SELECT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'select_button_new.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
SELECTED_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'skin_selected_button_new.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
MAIN_MENU_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'main_menu_button.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
PRICE1000 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', '1000price.png')), (100,100))

# fonts
SCORE_FONT = pygame.font.SysFont('New Athletic M54', 40)


# sound settings
START_OF_LASER = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'startLaser.mp3'))
LASER_ON = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'laserOn.mp3'))
GAME_MUSIC = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'remix.mp3'))
MISSILE_WARNING = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'missile_warning.mp3'))
MISSILE_LAUNCHED = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'missile_launched.mp3'))
COIN_SOUND = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'coin_sound.mp3'))
MENU_MUSIC = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'remix.mp3'))
MAN_SCREAM = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'man-scream.mp3'))
GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'game-over-sound.mp3'))
HERE_WE_GO_AGAIN = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'here-we-go-again.mp3'))
GAME_MUSIC = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'game_music.mp3'))
