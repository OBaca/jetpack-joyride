from .constants import *

# animation
ZOMBIE_WALKING_ASSETS = [init_animation('0_Golem_Walking_',i) for i in range(0,24)]

class Zombie(object):
    ''' This class represent a zombie in the game. '''
    def __init__(self, right, x):   
        self.rect = pygame.Rect(x,460,100,100)
        self.zombie_walking_animation(ZOMBIE_WALKING_ASSETS)
        self.current_sprite = 0
        self.image = self.walking_right[self.current_sprite]
        # set the side the player move to.
        self.increase_x = 1 if right else -1
        # set speed settings
        self.timing_speed = 0
        self.speed = random.choice([0.4,0.7,1])
        # if right is True - the Zombie is walking from the left to the right
        self.right = right  

        
    ''' This function creates an animation for the zombie to walk.'''
    def update(self):
        sprites = []
        # set the sprite to the side the zombie is walking
        sprites = self.walking_right if self.right else self.walking_left
        
        self.timing_speed += self.speed
        if self.timing_speed > 1:
            self.rect.x += self.increase_x
            self.timing_speed = 0

        # zombie animation.
        self.current_sprite += 0.25
        if self.current_sprite >= len(self.walking_right):
            self.current_sprite = 0
        self.image = sprites[int(self.current_sprite)]

        #  respawn zombie position.
        if self.right:
            if self.rect.x > WIDTH:
                self.rect.x = self.rect.width*(-1)
                self.speed = random.choice([0.4,0.7,1])
        else:
            if self.rect.x < -60:
                self.rect.x = WIDTH
                self.speed = random.choice([0.4,0.7,1])


    ''' This function draw the zombie to the screen. '''
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))


    ''' This function set the zombie walking animation (walking left/ walking right). '''
    def zombie_walking_animation(self, zombie_walking_animation_assets):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                load_image(os.path.join("zombie_walking", asset_name)),(self.rect.width, self.rect.height))
        def _flip_asset(asset_name):
            return pygame.transform.flip(asset_name, True, False)
        
        self.walking_right = [_init_asset(asset_name) for asset_name in zombie_walking_animation_assets]
        self.walking_left = [_flip_asset(_init_asset(asset_name)) for asset_name in zombie_walking_animation_assets]
        

''' This function spawn the zombies in the main menu screen. '''
def zombie_spawn_menu(zombies, screen):
    for zombie in zombies:
        zombie.draw(screen)
        zombie.update()
        