from data.constants import *

class Player(object):
    def __init__(self): # x, y, width, height
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        '''
        self.reset()
        #self.collision = (self.x, self.y, self.rect.width, self.rect.height)

    
    def reset(self):
        self.rect = pygame.Rect(100,450,60,75)
        self.vel = 9
        self.gravity = 8
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'player.png')), (self.rect.width, self.rect.height))
    

    def draw(self, screen, map):
        screen.blit(map.image, (map.imageX,0))
        screen.blit(map.image, (map.imageX2,0))
        #self.collision = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(screen, BLACK, self.collision)
        screen.blit(self.image, (self.rect.x,self.rect.y))

        

        
    
    # handling the player movements
    def player_movement(self, pressed_key):
        # a/d -> left/right movement
        if pressed_key[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.vel
        elif pressed_key[pygame.K_d] and self.rect.x + self.rect.width < WIDTH:
            self.rect.x += self.vel
        # space key to launch the launcher
        if pressed_key[pygame.K_SPACE] and self.rect.y > 0:
            self.rect.y -= self.vel
        # insert gravity to the player
        elif self.rect.y + self.rect.height < HEIGHT - FIX_IMAGE_LIMIT:
            self.rect.y += self.gravity
        # player image fix to the screen frame
        elif self.rect.y + self.rect.height + self.vel >= HEIGHT - FIX_IMAGE_LIMIT:
            self.rect.y = HEIGHT - self.rect.height - FIX_IMAGE_LIMIT
        if self.rect.y <= 0:
            self.rect.y = 1


def check_hit_obstacles(player, obstacles):
    for obstacle in obstacles:
        if player.rect.colliderect(obstacle.rect):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))