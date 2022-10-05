from .constants import *

COIN_ASSETS = ["coin1.png", "coin2.png", "coin3.png", "coin4.png", "coin5.png",
                        "coin6.png", "coin7.png", "coin8.png", "coin9.png", "coin10.png"]


class Coin(pygame.sprite.Sprite):
    '''
    This class represent a single coin currency in the game.
    '''
    def __init__(self, x, y):
        self.coin_animation(COIN_ASSETS)
        self.reset( x, y)

    
    ''' This function reset all the variables of the coin.   '''
    def reset(self, x, y):
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = pygame.Rect(x,y,self.image.get_width(),self.image.get_height())
        self.show_image = True
        self.speed = 2
        self.increase_speed = 0


    ''' This function creates an animation for the coin to spin.  '''
    def update(self):
        self.current_sprite += 0.25
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        self.image = self.sprites[int(self.current_sprite)]


    ''' This function draw a single coin to the screen.  '''
    def draw(self, screen):
        if self.show_image:
            screen.blit(self.image, (self.rect.x,self.rect.y))


    ''' This function set the image animation to a single coin.  '''
    def coin_animation(self, coin_animation_asset):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                pygame.image.load(os.path.join(os.getcwd() + "\Assets\coins", asset_name)),(COIN_SIZE, COIN_SIZE))

        self.sprites = [_init_asset(asset_name) for asset_name in coin_animation_asset]
