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
POST_LASERS = pygame.image.load(os.path.join('Assets', 'lasers2.png'))

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
JETPACK_OFF = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'player.png')), (60, 75))

QUIT_MENU_NO_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("Assets\\buttons", 'quit_button_no_hover.png')), (MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT))
QUIT_MENU_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'quit_button_hover.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))

PLAY_MENU_NO_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'play_button_no_hover.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
PLAY_MENU_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'play_button_hover.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))

COSTUMES_MENU_NO_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'costumes_no_hover.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))
COSTUMES_MENU_HOVER_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\buttons', 'costumes_hover2.png')), (MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT))

MENU_BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'main_menu_bg.png')), (WIDTH,HEIGHT))
# fonts
SCORE_FONT = pygame.font.SysFont('comicsans', 40)

# sound settings
START_OF_LASER = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'startLaser.mp3'))
LASER_ON = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'laserOn.mp3'))
GAME_MUSIC = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'remix.mp3'))
MISSILE_WARNING = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'missile_warning.mp3'))
MISSILE_LAUNCHED = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'missile_launched.mp3'))
COIN_SOUND = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'coin_sound.mp3'))
MENU_MUSIC = pygame.mixer.Sound(os.path.join('Assets\Sounds', 'remix.mp3'))