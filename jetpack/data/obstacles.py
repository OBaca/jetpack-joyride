from data.constants import *          

''' This function draw all the obstacles to the screen. '''
def draw_obstacles(zappers,lasers,missiles, screen):
    for i in range(len(zappers)):
        zappers[i].draw_zapper(screen)
    for i in range(len(lasers)):   
        lasers[i].draw_laser(screen)
    for i in range(len(missiles)):
        missiles[i].draw(screen)


''' This function reset all the obstacles positions. '''
def reset_obstacle_pos(zappers, lasers):
    for obstacle in zappers:
        obstacle.reset()
    for laser in lasers:
        laser.reset()


''' This function check if the player died from an obstacle. '''
def check_hit_obstacles(player, zappers, lasers, missiles):
    for zapper in zappers:
        if player.rect.colliderect(zapper.rect):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))

    for laser in lasers:
        if player.rect.colliderect(laser.post_rect):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))

    for missile in missiles:
        if player.rect.colliderect(missile.rect):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
