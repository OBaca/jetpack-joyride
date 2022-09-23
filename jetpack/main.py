from data.constants import *
from data.player import *
from data.obstacles import *
from data.map import *
from data.lasers import *
from data.button import *
from data.missile import *

pygame.init()


# screen settings
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Jetpack Joyride')



def show_score(screen, score):
    score_text = SCORE_FONT.render('SCORE: ' + str(score), 1, BLACK)
    screen.blit(score_text, (10,10))


def main():
    map = Map()
    # to make a shrek avatar, 150X200 // 60X75
    player = Player() 
    obstacles = []
    obstacles.append(Zappers(pygame.Rect(random.randint(WIDTH, WIDTH+200),random.randint(FIX_IMAGE_LIMIT, HEIGHT-140),40,140) ,  'along', OBS_IMG1))  #300,500,40,140,
    obstacles.append(Zappers(pygame.Rect(random.randint(WIDTH, WIDTH+200),random.randint(FIX_IMAGE_LIMIT, HEIGHT- FIX_IMAGE_LIMIT -40),140,40) , 'across', OBS_IMG2))  #300,450,140, 40,
    
    lasers = [
                Lasers(pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50), pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50) ),
                Lasers(pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50), pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50) ),
                Lasers(pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50), pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50) ),
                Lasers(pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50), pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50) )
            ]
    missiles = [
                Missile(pygame.Rect(WIDTH,player.rect.y, 100, 100)),
                Missile(pygame.Rect(WIDTH,player.rect.y, 100, 100))
                ]
    

    resume_button = Button(pygame.Rect(WIDTH//2 - 75, HEIGHT//2 - 120, 150, 100), RESUME_BUTTON)
    retry_button = Button(pygame.Rect(WIDTH//2 - 75, HEIGHT//2, 150, 100), RETRY_BUTTON)
    quit_button = Button(pygame.Rect(WIDTH//2 - 75, HEIGHT//2 + 120, 150, 100), QUIT_BUTTON)
    speaker_off_button = Button(pygame.Rect(WIDTH//2 - 75, HEIGHT//2 - 200, 100, 50), SPEAKER_OFF_BUTTON)
    speaker_on_button = Button(pygame.Rect(WIDTH//2 + 15, HEIGHT//2 - 200, 100, 50), SPEAKER_ON_BUTTON)


    score_speed = 1
    score = 0
    pause_game = False
    silent_music = False
    
    
    
    active = True   # to check if the player can still play
    run = True
    clock = pygame.time.Clock()
    while run:
        map.redraw_map(SCREEN)
        if pause_game:
            
            # resume button
            if resume_button.draw_button(SCREEN):
                pause_game = False

            # retry button
            if retry_button.draw_button(SCREEN):
                # 1. reset score
                score = 0
                score_speed = 1
                reset_lasers(lasers, score)
                # 2. reset map location
                map.reset()
                # 3. reset player location
                player.reset()
                # 4. reset obstacle positions
                reset_obstacle_pos(obstacles, lasers)
                
                # need to fix reset when you pause the game and try to press on the retry button while lasers ON
                continue
    
            # quit button
            if quit_button.draw_button(SCREEN):
                run = False
            # turn off music and sfx
            if speaker_off_button.draw_button(SCREEN):
                pygame.mixer.pause()
                silent_music = True
            # turn on music and sfx
            if speaker_on_button.draw_button(SCREEN):
                pygame.mixer.unpause()
                silent_music = False

        else:
            
            map.update()
                        
            pressed_key = pygame.key.get_pressed()
            player.player_movement(pressed_key)

            # adding score
            score_speed += 0.1
            score = int(score_speed)
            
            
            player.draw(SCREEN, map)

            draw_obstacles(obstacles,lasers,missiles, SCREEN)

            # place lasers algorithm
            lasers_placement(score,lasers,silent_music)

            # place missiles algorithem
            missile_movement(missiles, score, player)

            
            obstacle_placement(obstacles)
            check_hit_obstacles(player, obstacles)

            
            # show score
            show_score(SCREEN, score)

            increase_speed(map)

            clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_game = True
                

            if event.type == PLAYER_HIT:
                print('game over')
                # need to add animation of the player falling over
                # and make a game over screen ( try again )
                # showing high score, and current score, and updating the high score
                    

        pygame.display.update()


    pygame.quit()


if __name__ == "__main__":
    main()


