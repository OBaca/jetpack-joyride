from data.zombie import *
from data.game import *
from data.costumes import *
from data.button import *
from data.boost import *


# screen settings
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jetpack Joyride')
pygame.display.set_icon(JETPACK_OFF_MALE)

''' This function manage the main menu screen. '''
def main_menu():
    clock = pygame.time.Clock()
    #click is to know if a user pressed a button(used to check for double clicks between two different scenes).
    click = False   
    # buttons
    play_button = Button(pygame.Rect(100,550,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT),  PLAY_MENU_NO_HOVER_BUTTON, PLAY_MENU_HOVER_BUTTON)
    costumes_button = Button(pygame.Rect(350,550,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT),  COSTUMES_MENU_NO_HOVER_BUTTON, COSTUMES_MENU_HOVER_BUTTON)
    quit_button = Button(pygame.Rect(600,550,MENU_BUTTON_WIDTH,MENU_BUTTON_HEIGHT),  QUIT_MENU_NO_HOVER_BUTTON, QUIT_MENU_HOVER_BUTTON)
    red_fire_boost_button = Button(RED_FIRE_BOOST_MENU_RECT, RED_FIRE_BOOST_NO_HOVER_BUTTON, RED_FIRE_BOOST_HOVER_BUTTON)
    blue_fire_boost_button = Button(pygame.Rect(90,200,70,160), BLUE_FIRE_BOOST_NO_HOVER_BUTTON, BLUE_FIRE_BOOST_HOVER_BUTTON)

    # initialize the player and zombies.
    player = Player(JETPACK_OFF_MALE, 0) 
    zombies = [Zombie(True, -120), Zombie(False, WIDTH), Zombie(True, -130), Zombie(False, WIDTH+10)]
    
    # initialize boosts.
    red_fire_boost = Boost(red_fire_boost_button, 'red')
    blue_fire_boost = Boost(blue_fire_boost_button, 'blue')

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
                game(coins_amount, player, SCREEN, red_fire_boost)
                music_replaying = False

        # when you press the quit button you will exit the game.
        elif quit_button.draw_button(SCREEN, 'quit_menu'):
            pygame.quit()
            sys.exit()
        
        # when you press the costumes button you will move to the costumes screen.
        elif costumes_button.draw_button(SCREEN, 'costumes'):
            if click:
                costumes_menu(player, SCREEN)




        # TEST TEST TEST TEST TEST TEST
        elif red_fire_boost_button.draw_button(SCREEN, 'red-fire'):
            if click:
                coins_amount = boost_menu(red_fire_boost, SCREEN, coins_amount)
                update_coins(coins_amount)
                
        elif blue_fire_boost_button.draw_button(SCREEN, 'blue-fire'):
            if click:
                coins_amount = boost_menu(blue_fire_boost, SCREEN, coins_amount)
                update_coins(coins_amount)
        




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

        # show player coins on the screen.
        show_coins(SCREEN, coins_amount, 10, 60, True)

        #show boosts price on the screen.
            # red boost price and amount
        show_coins(SCREEN, red_fire_boost.price, 20, 370, False) 
        show_text(SCREEN, red_fire_boost.amount, 12, 202, (255,255,255))
            # blue boost price and amount
        show_coins(SCREEN, blue_fire_boost.price, 100, 370, False)
        show_text(SCREEN, blue_fire_boost.amount, 92, 202, (255,255,255))


        clock.tick(FPS)
        pygame.display.update()


# program start.
def main():
    main_menu()

if __name__ == "__main__":
    main()
