from data.constants import *

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
        self.update_animation()
        

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
        y_spawner = FIX_IMAGE_LIMIT - 40 if self.style == 'across' else 140
        self.rect.x = random.randint(WIDTH, WIDTH+200)
        self.rect.y = random.randint(FIX_IMAGE_LIMIT, HEIGHT - y_spawner)


    ''' This function draws the zapper obstacle to the screen. '''
    def draw_zapper(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))


    ''' This function set the animation for the zappers. '''
    def update_animation(self):
        ZAPPER_VERTICAL_ASSETS = ["vertical_zapper1.png", "vertical_zapper2.png", "vertical_zapper3.png", "vertical_zapper4.png"]
        ZAPPER_HORIZONTAL_ASSETS = ["horizontal_zapper1.png", "horizontal_zapper2.png", "horizontal_zapper3.png", "horizontal_zapper4.png"]

        def _init_asset(asset_name: str):
            return pygame.image.load(os.path.join("Assets\zappers_animation", asset_name))

        self.vertical_sprite = [_init_asset(asset_name) for asset_name in ZAPPER_VERTICAL_ASSETS]
        self.horizontal_sprite = [_init_asset(asset_name) for asset_name in ZAPPER_HORIZONTAL_ASSETS]

''' This function spawn the different zappers on the screen. '''
def zappers_placement(zappers, lasers, death, score):
    position = 'x' 
    RESET_X_POSITION = {'top': 10, 'mid-top': 150, 'mid-bottom': 300, 'bottom': 450}
    # setting the zappers speed difficulty
    zappers_speed_timing = 50
    if score >= 300:
        zappers_speed_timing = 80
    if score >= 1300:
        zappers_speed_timing = 100

    # small vertical and horizontal zappers that are spawned together.
    for zapper in zappers:
        # increasing the spead of the zappers.
        if score%zappers_speed_timing == 0:
            zapper.increase_speed += 0.5
            if zapper.increase_speed >= 10:
                zapper.speed += 1
                zapper.increase_speed = 0

        # the zappers are moving only if the player is alive
        if death == False:
            zapper.rect.x -= zapper.speed
            
        # check if the lasers is running so we won't place zapper with a laser.
        if zapper.rect.x + zapper.rect.width <0 and lasers[0].is_running == False:
            zapper.positions = ['top', 'mid-top','mid-bottom','bottom']
            while position == 'x':
                position = random.choice(zapper.positions )
            zapper.positions = [p.replace(position, 'x') for p in zapper.positions]
            
            # reset the zapper positions
            zapper.rect.y = RESET_X_POSITION[position]
            zapper.rect.x = random.randint (WIDTH, WIDTH+400)
            
        
''' This function update the animation for the zappers. '''
def update_zappers(zappers):
    for zapper in zappers:
        if zapper.style == 'along':
            zapper.update_vertical()
        if zapper.style == 'across':
            zapper.update_horizontal()
