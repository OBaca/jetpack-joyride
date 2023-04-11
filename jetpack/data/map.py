from data.constants import *

BG_ANIMATION = [init_animation('map', i) for i in range(1,12)]

class Map():
    ''' This class represent the map of the game. '''
    def __init__(self, background_image):
        self.reset(background_image)


    ''' This function reset all the variables of the class Map'''
    def reset(self, background_image):
        self.image = background_image
        self.image2 = background_image
        self.image_indx = 0
        self.image_indx2 = 1
        self.imageX = 0
        self.imageX2 = self.image.get_width()
        self.speed = 1.2
        self.speed_increase = 0
        self.set_map_sprite(BG_ANIMATION)


    ''' This function update the map location so it will look like an infinity map. '''
    def update(self, death):
        if death == False:
            self.imageX -= self.speed + self.speed_increase
            self.imageX2 -= self.speed + self.speed_increase
            if self.imageX < (self.map_sprite[self.image_indx].get_width() *-1) :
                self.imageX = self.image.get_width()
                self.image_indx= self.image_indx2+1
                if self.image_indx > 10:
                    self.image_indx = 0
            if self.imageX2 < (self.map_sprite[self.image_indx2].get_width() *-1) :
                self.imageX2 = self.image2.get_width()
                self.image_indx2= self.image_indx+1
                if self.image_indx2 > 10:
                    self.image_indx2 = 0
                

    ''' This function set the maps in the game'''
    def set_map_sprite(self, animation_asset):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(load_image(os.path.join("backgrounds/bg", asset_name)), (2048,650))

        self.map_sprite = [_init_asset(asset_name) for asset_name in animation_asset]


    ''' This function draw the map to the screen. '''
    def redraw_map(self, screen):
        screen.blit(self.map_sprite[self.image_indx], (self.imageX,0))
        screen.blit(self.map_sprite[self.image_indx2], (self.imageX2,0))
       

    ''' This function increase the map speed. '''
    def increase_speed(self, death):
        if self.speed_increase < 6:
            self.speed_increase += 0.001
        