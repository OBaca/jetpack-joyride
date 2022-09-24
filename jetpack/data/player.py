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
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\jetpackAnimation', 'jetpack1.png')), (self.rect.width+15, self.rect.height+15)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\jetpackAnimation', 'jetpack2.png')), (self.rect.width+15, self.rect.height+15)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\jetpackAnimation', 'jetpack3.png')), (self.rect.width+15, self.rect.height+15)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\jetpackAnimation', 'jetpack4.png')), (self.rect.width+15, self.rect.height+15)))
        self.current_sprite = 0

    
    def reset(self):
        self.rect = pygame.Rect(100,450,60,75)
        self.vel = 7
        self.gravity = 8
        self.image = JETPACK_OFF
    

    def draw(self, screen, map):
        screen.blit(map.image, (map.imageX,0))
        screen.blit(map.image, (map.imageX2,0))
        #self.collision = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(screen, BLACK, self.collision)
        screen.blit(self.image, (self.rect.x,self.rect.y))

    def update_jetpack(self):
        self.current_sprite += 0.25

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        self.image = self.sprites[int(self.current_sprite)]

        
    
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
            self.update_jetpack()
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

def coin_collect(player, coins):
    for coin in coins.pattern:
        if player.rect.colliderect(coin.rect) and coin.show_image:
            COIN_SOUND.play()
            coin.show_image = False
            print("coin collected")
