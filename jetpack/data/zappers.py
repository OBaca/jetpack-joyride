from data.constants import *


ZAPPER_VERTICAL_ASSETS = [init_animation('vertical_zapper',i) for i in range(1,5)]
ZAPPER_HORIZONTAL_ASSETS = [init_animation('horizontal_zapper',i) for i in range(1,5)]

class Zappers(object):
    ''' This class represent the zapper obstacle. '''
    def __init__(self, rect, style, image):
        self.rect = rect
        self.speed = 2
        self.increase_speed = 0
        self.style = style
        self.image = image
        self.current_vertical_sprite = 0
        self.current_horizontal_sprite = 0
        self.positions = ['top', 'mid-top','mid-bottom','bottom']
        self.update_animation(ZAPPER_VERTICAL_ASSETS, ZAPPER_HORIZONTAL_ASSETS)
        

    ''' This function creates the animation for the vertical zapper. '''
    def update_vertical(self):
        self.current_vertical_sprite += 0.25
        if self.current_vertical_sprite >= len(self.vertical_sprite):
            self.current_vertical_sprite = 0     
        self.image = self.vertical_sprite[int(self.current_vertical_sprite)]


    ''' This function creates the animation for the horizontal zapper. '''
    def update_horizontal(self):
        self.current_horizontal_sprite += 0.25
        if self.current_horizontal_sprite >= len(self.horizontal_sprite):
            self.current_horizontal_sprite = 0    
        self.image = self.horizontal_sprite[int(self.current_horizontal_sprite)]


    ''' This function reset the class variables. '''
    def reset(self):
        self.speed = 2
        y_spawner = FIX_IMAGE_LIMIT - 40 if self.style == 'vertical' else 140
        self.rect.x = random.randint(WIDTH, WIDTH+200)
        self.rect.y = random.randint(FIX_IMAGE_LIMIT, HEIGHT - y_spawner)


    ''' This function draws the zapper obstacle to the screen. '''
    def draw_zapper(self, screen):
        screen.blit(self.image, (self.rect.x-10,self.rect.y-9))


    ''' This function set the animation for the zappers. '''
    def update_animation(self, vertical_animation_asset, horizontal_animation_asset):
        
        def _init_asset(asset_name: str):
            return load_image(os.path.join("zappers_animation", asset_name))

        self.vertical_sprite = [_init_asset(asset_name) for asset_name in vertical_animation_asset]
        self.horizontal_sprite = [_init_asset(asset_name) for asset_name in horizontal_animation_asset]

''' This function spawn the different zappers on the screen. '''
def zappers_placement(zappers, lasers, death, score):
    position = 'x' 
    RESET_Y_POSITION = {'top': 10, 'mid-top': 150, 'mid-bottom': 300, 'bottom': 450}
    # setting the zappers speed difficulty
    zappers_speed_timing = 50
    if score >= 300:
        zappers_speed_timing = 80
    if score >= 1300:
        zappers_speed_timing = 100

    # small vertical and horizontal zappers that are spawned together.
    for zapper in zappers:
        # increasing the speed of the zappers.
        if score%zappers_speed_timing == 0:
            zapper.increase_speed += 0.5
            if zapper.increase_speed >= 10:
                zapper.speed += 1
                zapper.increase_speed = 0

        # the zappers are moving only if the player is alive
        if death == False:
            zapper.rect.x -= zapper.speed
            
        # check if the lasers is running so we won't place zapper with a laser.
        if zapper.rect.x + zapper.rect.width + 5 <0 and lasers[0].is_running == False:
            zapper.positions = ['top', 'mid-top','mid-bottom','bottom']
            while position == 'x':
                position = random.choice(zapper.positions )
            zapper.positions = [p.replace(position, 'x') for p in zapper.positions]
            
            # reset the zapper positions
            zapper.rect.y = RESET_Y_POSITION[position]
            zapper.rect.x = random.randint (WIDTH, WIDTH+400)
            
        
''' This function update the animation for the zappers. '''
def update_zappers(zappers):
    for zapper in zappers:
        if zapper.style == 'vertical':
            zapper.update_vertical()
        if zapper.style == 'horizontal':
            zapper.update_horizontal()
