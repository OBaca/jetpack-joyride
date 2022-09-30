from data.constants import *
from data.player import *
from data.obstacles import *
from data.map import *
from data.lasers import *
from data.button import *
from data.missile import *
from data.coin import *
from data.coins import *
from data.zappers import *
from data.manage_files import *
from data.manage_text import *


''' This function returns the image by the type value that given. '''
def get_player_image_game(type):
    if type == 0:
        return JETPACK_OFF_MALE
    if type == 1:
        return JETPACK_OFF_FEMALE
    if type == 2:
        pass


''' This function manage the game loop. '''
def game(coins_amount, player, screen):
    # map creation.
    map = Map()
    # obstacle creations
    zappers = []
    zappers.append(Zappers(pygame.Rect(random.randint(WIDTH, WIDTH+200),random.randint(FIX_IMAGE_LIMIT, HEIGHT-140),40,140) ,  'along', OBS_IMG1)) 
    zappers.append(Zappers(pygame.Rect(random.randint(WIDTH, WIDTH+200),random.randint(FIX_IMAGE_LIMIT, HEIGHT- FIX_IMAGE_LIMIT -40),140,40) , 'across', OBS_IMG2))  
    lasers = [Lasers(), Lasers(), Lasers(), Lasers()]
    missiles = [Missile(player.rect.y), Missile(player.rect.y)]
    # coins creations
    coins = [Coins(1, get_pattern(1, WIDTH, 350)), 
                Coins(2, get_pattern(2, random.randint(WIDTH, WIDTH+40) , random.choice([150, 350, 500])))]
    
    
    # buttons
    resume_button = Button(pygame.Rect(WIDTH//2 - 75, HEIGHT//2 - 120, 150, 100), RESUME_NO_HOVER_BUTTON)
    retry_button = Button(pygame.Rect(WIDTH//2 - 75, HEIGHT//2, 150, 100), RETRY_BUTTON)
    quit_button = Button(pygame.Rect(WIDTH//2 - 75, HEIGHT//2 + 120, 150, 100), QUIT_GAME_BUTTON)
    speaker_off_button = Button(pygame.Rect(WIDTH//2 - 75, HEIGHT//2 - 200, 100, 50), SPEAKER_OFF_BUTTON)
    speaker_on_button = Button(pygame.Rect(WIDTH//2 + 15, HEIGHT//2 - 200, 100, 50), SPEAKER_ON_BUTTON)

    # music volume
    START_OF_LASER.set_volume(0.3)
    GAME_MUSIC.set_volume(0.2)
    LASER_ON.set_volume(0.3)
    MISSILE_WARNING.set_volume(0.3)
    MISSILE_LAUNCHED.set_volume(0.3)
    COIN_SOUND.set_volume(0.3)
    GAME_OVER_SOUND.set_volume(0.3)
    
    music_replaying = False
    game_startover = True
    run = True
    clock = pygame.time.Clock()

    while run:
        # music playback
        if music_replaying == False:
            pygame.mixer.Channel(0).play(GAME_MUSIC, -1)
            music_replaying = True

        # game settings variables
        if game_startover:
            game_startover = False
            score_speed = 1
            score = 0
            high_score = get_high_score()
            pause_game = False
            silent_music = False
            death_end_time = 0
            start_time = 0

            # 1. reset lasers positions
            reset_lasers(lasers, score)

            # 2. reset map location
            map.reset()

            # 3. reset player location
            player.reset(get_player_image_game(player.type), player.type)

            # 4. reset obstacle positions
            reset_obstacle_pos(zappers, lasers)

            # 5. reset coins system
            for coin in coins:
                coin.reset()
            current_coin_amount = 0

            # 6. reset missiles positions
            for missile in missiles:
                missile.reset(player.rect.y)

            # reset music sounds.
            START_OF_LASER.stop()
            LASER_ON.stop()
            MISSILE_WARNING.stop()
            MISSILE_LAUNCHED.stop()
            
        # draw the map to the screen.
        map.redraw_map(screen)

        # pause game menu.
        if pause_game:
            # resume button
            if resume_button.draw_button(screen, 'resume'):
                pause_game = False

            # retry button
            if retry_button.draw_button(screen, 'retry'):
                game_startover = True
                continue
    
            # quit button
            if quit_button.draw_button(screen, 'quit_game'):
                pygame.quit()
                sys.exit()

            # turn off music and sfx
            if speaker_off_button.draw_button(screen, 'speaker-off'):
                pygame.mixer.pause()
                silent_music = True

            # turn on music and sfx
            if speaker_on_button.draw_button(screen, 'speaker-on'):
                pygame.mixer.unpause()
                silent_music = False

        # game logic
        else:
            # start of map movement.
            map.update(player.death)
                        
            pressed_key = pygame.key.get_pressed()

            # start of player movement.
            player.player_movement(pressed_key, start_time)

            # adding score when the player is alive
            if player.death == False:
                score_speed += 0.1
                score = int(score_speed)
            
            # start death animation.
            if player.death_scene( death_end_time):
                run = False
            
            # draw objects on the screen.
            player.draw(screen, map)
            draw_coins(coins, screen)
            draw_obstacles(zappers,lasers,missiles, screen)

            # calling the obstacles only when the player is alive.
            if player.death == False:
                # place lasers algorithm.
                lasers_placement(score,lasers,silent_music)

                # place missiles algorithm.
                missile_movement(missiles, score, player, silent_music)

                # place zappers algorithm.
                update_zappers(zappers)
                zappers_placement(zappers, lasers, player.death, score)
            
            # place coins algorithm.
            update_coins_positions(coins, player.death, score)

            # check for collision.
            check_hit_obstacles(player, zappers, lasers, missiles)

            # show texts on the screen.
            if player.death:
                show_game_over_text(screen)
            show_score(screen, score)
            high_score = update_high_score(high_score, score)
            show_high_score(screen, high_score)
            current_coin_amount = coin_collect(player, coins, current_coin_amount)
            show_coins(screen, current_coin_amount)
            
            # increase the map speed.
            map.increase_speed(player.death)

            clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_game = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    # set the jetpack "feel" to the game.
                    player.image = get_player_image_game(player.type)
                    start_time = pygame.time.get_ticks()
                    
            # activate player death music and time.
            if event.type == PLAYER_HIT:
                if player.death == False:
                    death_end_time = pygame.time.get_ticks() + 5000
                    pygame.mixer.Channel(6).play(GAME_OVER_SOUND)
                    if player.type == 0:
                        pygame.mixer.Channel(7).play(MAN_SCREAM)
                player.death = True
                
        pygame.display.update()

    # update the amount of coins earned in the current game upon death.
    update_coins(current_coin_amount + coins_amount)
    # returning to the main menu because the game is over