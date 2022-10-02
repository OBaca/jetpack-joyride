from .constants import *

class Zombie(object):
    ''' This class represent a zombie in the game. '''
    def __init__(self, right, x):   
        self.rect = pygame.Rect(x,460,100,100)
        self.zombie_walking_animation()
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
            if self.rect.x < 0:
                self.rect.x = WIDTH
                self.speed = random.choice([0.4,0.7,1])


    ''' This function draw the zombie to the screen. '''
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))


    ''' This function set the zombie walking animation (walking left/ walking right). '''
    def zombie_walking_animation(self):
        ZOMBIE_WALKING_ASSETS = ["0_Golem_Walking_001.png", "0_Golem_Walking_002.png", "0_Golem_Walking_003.png", "0_Golem_Walking_004.png", "0_Golem_Walking_005.png", "0_Golem_Walking_006.png"
                                    , "0_Golem_Walking_007.png", "0_Golem_Walking_008.png", "0_Golem_Walking_009.png", "0_Golem_Walking_010.png", "0_Golem_Walking_011.png", "0_Golem_Walking_012.png"
                                    , "0_Golem_Walking_013.png", "0_Golem_Walking_014.png", "0_Golem_Walking_015.png", "0_Golem_Walking_016.png", "0_Golem_Walking_017.png", "0_Golem_Walking_018.png"
                                    , "0_Golem_Walking_019.png", "0_Golem_Walking_020.png", "0_Golem_Walking_021.png", "0_Golem_Walking_022.png", "0_Golem_Walking_023.png"]

        def _init_asset(asset_name: str, flip):
            if flip:
                return pygame.transform.flip(pygame.transform.scale(
                    pygame.image.load(os.path.join("Assets\zombie_walking", asset_name)),(self.rect.width, self.rect.height)), True, False)
            else:
                return pygame.transform.scale(
                    pygame.image.load(os.path.join("Assets\zombie_walking", asset_name)),(self.rect.width, self.rect.height))

        self.walking_right = [_init_asset(asset_name, False) for asset_name in ZOMBIE_WALKING_ASSETS]
        self.walking_left = [_init_asset(asset_name, True) for asset_name in ZOMBIE_WALKING_ASSETS]
        

''' This function spawn the zombies in the main menu screen. '''
def zombie_spawn_menu(zombies, screen):
    for zombie in zombies:
        zombie.draw(screen)
        zombie.update()
        