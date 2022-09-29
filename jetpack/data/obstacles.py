from data.constants import *          

def draw_obstacles(zappers,lasers,missiles, screen):
    for i in range(len(zappers)):
        zappers[i].draw_zapper(screen)
    for i in range(len(lasers)):   
        lasers[i].draw_laser(screen)
    for i in range(len(missiles)):
        missiles[i].draw(screen)


def reset_obstacle_pos(zappers, lasers):
    for obstacle in zappers:
        obstacle.reset()
    for laser in lasers:
        laser.reset()

# check if the player hit one of the obstacles
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
