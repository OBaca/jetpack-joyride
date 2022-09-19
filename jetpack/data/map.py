from data.constants import *

class Map():
    def __init__(self):
        self.reset()

    def reset(self):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bg.png')), (WIDTH,HEIGHT))
        self.imageX = 0
        self.imageX2 = self.image.get_width()
        self.speed = 0

    def update(self):
        self.imageX -= 1.1 - self.speed
        self.imageX2 -= 1.1 - self.speed
        if self.imageX < self.image.get_width() *-1:
            self.imageX = self.image.get_width()
        if self.imageX2 < self.image.get_width() *-1:
            self.imageX2 = self.image.get_width()
        

    def redraw_map(self, screen):
        screen.blit(self.image, (self.imageX,0))
        screen.blit(self.image, (self.imageX2,0))
       

def increase_speed(map):
    if map.speed < 6:
        map.speed -= 0.001

