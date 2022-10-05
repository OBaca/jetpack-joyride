from data.constants import *
from data.player import *
from data.manage_files import *
from data.manage_text import *
from data.button import *

''' This function return the image by the type given. '''
def get_player_image_costumes(type):
    if type == 0:
        return DEFAULT_MALE
    if type == 1:
        return DEFAULT_FEMALE
    if type == 3:
        return SHREK_SKIN


''' This function manage the costumes shop screen. '''
def costumes_menu(player, screen):
    clock = pygame.time.Clock()
    click = False   # to know if we clicked the button.

    # buttons settings
    left_arrow = Button(pygame.Rect(250,450,ARROW_BUTTON_WH,ARROW_BUTTON_WH), LEFT_ARROW  ,LEFT_ARROW_HOVER)
    right_arrow = Button(pygame.Rect(500,450,ARROW_BUTTON_WH,ARROW_BUTTON_WH), RIGHT_ARROW ,RIGHT_ARROW_HOVER)
    buy_button = Button(pygame.Rect(300,550,MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT), BUY_BUTTON ,BUY_BUTTON)
    select_button = Button(pygame.Rect(300,550,MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT), SELECT_BUTTON, SELECT_BUTTON)
    main_menu_button = Button(pygame.Rect(20,550,MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT), MAIN_MENU_BUTTON, MAIN_MENU_BUTTON)

    # players skins dictionary
    players_selection = {'default-male-player':0, 'default-female-player':1, 'shrek':2}
    current_player = 0
    display_message = False
    start_time = 0

    ''' Costumes shop loop. '''
    while True:
        # costumes screen background.
        screen.fill((255,255,255))
        screen.blit(COSTUMES_BG_IMG, (0,0))

        # get the coins we have.
        coins_amount = get_coins()

        # showing the left arrow selection key.
        if left_arrow.draw_button(screen, 'left-arrow'):
            current_player -= 1
            if current_player < 0:
                current_player = len(players_selection)-1
    
        # showing the right arrow selection key.
        elif right_arrow.draw_button(screen, 'right-arrow'):
            current_player += 1
            if current_player == len(players_selection):
                current_player = 0
        
        # if we dont own the skin, the buy button will be shown.
        elif player.type != current_player and check_skins_inventory(str(current_player)) == False:
            if buy_button.draw_button(screen, 'buy'):
                if click:
                    # updating the coins amount if the player bought the skin.
                    if current_player == players_selection['shrek']:
                        if coins_amount > 1000:
                            buy_skin(str(players_selection['shrek']))
                            update_coins(coins_amount - 1000)
                        else:
                            start_time = pygame.time.get_ticks()
                            display_message = True
                            
            # showing the skin price.
            if current_player == players_selection['shrek']:
                screen.blit(PRICE1000, (430,490))

        # if we own the skin we can select it.
        elif player.type != current_player and check_skins_inventory(str(current_player)):
            if select_button.draw_button(screen, 'select'):
                if click:
                    player.type = current_player
                    player.image = get_player_image_costumes(current_player)

        # return to the main menu when you click the main-menu button.
        if main_menu_button.draw_button(screen, 'main-menu'):
            if click:
                return

        # showing the current skin we are using.
        if player.type == current_player: 
            screen.blit(SELECTED_BUTTON, (300,550))
            
        
        click = False
        for event in pygame.event.get():
                # exit the game when you press the 'X' button.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # indicate if we press a button.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

        # showing the skins
        if current_player == players_selection['default-male-player']:
            screen.blit(DEFAULT_MALE, (320,350))
        elif current_player == players_selection['default-female-player']:
            screen.blit(DEFAULT_FEMALE, (320,350))
        elif current_player == players_selection['shrek']:
            screen.blit(SHREK_SKIN, (300,350))

        # if we dont have enough money to buy a skin.
        if display_message:
            not_enough_coins_to_buy(screen)
        # the message will be showen for 3 seconds.
        if pygame.time.get_ticks() - start_time > 3000: 
            display_message = False

        # show the coins the user have.
        show_menu_coins(screen, coins_amount)
        clock.tick(FPS)
        pygame.display.update()
