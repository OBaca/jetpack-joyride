from data.constants import *

class Map():
    ''' This class represent the map of the game. '''
    def __init__(self):
        self.reset()


    ''' This function reset all the variables of the class Map'''
    def reset(self):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bg.png')), (WIDTH,HEIGHT))
        self.imageX = 0
        self.imageX2 = self.image.get_width()
        self.speed = 1.2
        self.speed_increase = 0


    ''' This function update the map location so it will look like an infinity map. '''
    def update(self, death):
        # the map is moving only if the player is alive
        if death == False:
            self.imageX -= self.speed + self.speed_increase
            self.imageX2 -= self.speed + self.speed_increase
            if self.imageX < self.image.get_width() *-1:
                self.imageX = self.image.get_width()
            if self.imageX2 < self.image.get_width() *-1:
                self.imageX2 = self.image.get_width()
        

    ''' This function draw the map to the screen. '''
    def redraw_map(self, screen):
        screen.blit(self.image, (self.imageX,0))
        screen.blit(self.image, (self.imageX2,0))
       

    ''' This function increase the map speed. '''
    def increase_speed(self, death):
        if self.speed_increase < 6:
            self.speed_increase += 0.001
        