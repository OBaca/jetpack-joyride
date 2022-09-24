from .constants import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin1.png')), (COIN_SIZE,COIN_SIZE)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin2.png')), (COIN_SIZE,COIN_SIZE)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin3.png')), (COIN_SIZE,COIN_SIZE)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin4.png')), (COIN_SIZE,COIN_SIZE)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin5.png')), (COIN_SIZE,COIN_SIZE)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin6.png')), (COIN_SIZE,COIN_SIZE)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin7.png')), (COIN_SIZE,COIN_SIZE)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin8.png')), (COIN_SIZE,COIN_SIZE)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin9.png')), (COIN_SIZE,COIN_SIZE)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\coins', 'coin10.png')), (COIN_SIZE,COIN_SIZE)))
        self.reset( x, y)

    def reset(self, x, y):
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = pygame.Rect(x,y,self.image.get_width(),self.image.get_height())
        self.show_image = True
    
    def update(self):
        self.current_sprite += 0.25

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        self.image = self.sprites[int(self.current_sprite)]


    def draw(self, screen):
        if self.show_image:
            screen.blit(self.image, (self.rect.x,self.rect.y))

