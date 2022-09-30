from data.zombie import *
from data.game import *
from data.costumes import *


# screen settings
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jetpack Joyride')
pygame.display.set_icon(JETPACK_OFF_MALE)

''' This function manage the main menu screen. '''
def main_menu():
    clock = pygame.time.Clock()
    click = False   # to know if a user pressed a button.
    # buttons
    play_button = Button(pygame.Rect(100,550,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT),  PLAY_MENU_NO_HOVER_BUTTON)
    costumes_button = Button(pygame.Rect(350,550,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT),  COSTUMES_MENU_NO_HOVER_BUTTON)
    quit_button = Button(pygame.Rect(600,550,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT),  QUIT_MENU_NO_HOVER_BUTTON)
    
    # initialize the player and zombies.
    player = Player(JETPACK_OFF_MALE, 0) 
    zombies = [Zombie(True, -120), Zombie(False, WIDTH), Zombie(True, -130), Zombie(False, WIDTH+10)]
    
    # music settings.
    pygame.mixer.music.set_volume(0.4)
    music_channel = pygame.mixer.find_channel()
    music_replaying = False
    
    # main menu loop.
    while True:
        coins_amount = get_coins()

        # start of the main menu music.
        if music_replaying == False:
            music_channel.play(MENU_MUSIC, -1)
            music_replaying = True
        
        # set background
        SCREEN.fill((255,255,255))
        SCREEN.blit(MENU_BG_IMG, (0,0))

        # when you press the play button you will start the game.
        if play_button.draw_button(SCREEN, 'play'):
            if click:
                music_channel.pause()
                game(coins_amount, player, SCREEN)
                music_replaying = False

        # when you press the quit button you will exit the game.
        elif quit_button.draw_button(SCREEN, 'quit_menu'):
            pygame.quit()
            sys.exit()
        
        # when you press the costumes button you will move to the costumes screen.
        elif costumes_button.draw_button(SCREEN, 'costumes'):
            if click:
                costumes_menu(player, SCREEN)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # spawn zombies to the main menu.
        zombie_spawn_menu(zombies, SCREEN)

        # show coins on the screen.
        show_menu_coins(SCREEN,coins_amount)

        clock.tick(FPS)
        pygame.display.update()


# program start.
def main():
    main_menu()

if __name__ == "__main__":
    main()
