from data.constants import *

class Zappers(object):
    ''' This class represent the zapper obstacle. '''
    def __init__(self, rect, style, image):
        self.rect = rect
        self.speed = 2
        self.increase_speed = 0
        self.style = style
        self.image = image
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
        if self.style == 'along':
            self.rect.x = random.randint(WIDTH, WIDTH+200)
            self.rect.y = random.randint(FIX_IMAGE_LIMIT, HEIGHT-140)
        if self.style == 'across':
            self.rect.x = random.randint(WIDTH, WIDTH+200)
            self.rect.y = random.randint(FIX_IMAGE_LIMIT, HEIGHT- FIX_IMAGE_LIMIT -40)


    ''' This function draws the zapper obstacle to the screen. '''
    def draw_zapper(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))


    ''' This function set the animation for the zappers. '''
    def update_animation(self):
        self.vertical_sprite = []
        self.vertical_sprite.append(pygame.image.load(os.path.join('Assets\\zappers_animation', 'vertical_zapper1.png')))
        self.vertical_sprite.append(pygame.image.load(os.path.join('Assets\\zappers_animation', 'vertical_zapper2.png')))
        self.vertical_sprite.append(pygame.image.load(os.path.join('Assets\\zappers_animation', 'vertical_zapper3.png')))
        self.vertical_sprite.append(pygame.image.load(os.path.join('Assets\\zappers_animation', 'vertical_zapper4.png')))
        self.current_vertical_sprite = 0

        self.horizontal_sprite = []
        self.horizontal_sprite.append(pygame.image.load(os.path.join('Assets\\zappers_animation', 'horizontal_zapper1.png')))
        self.horizontal_sprite.append(pygame.image.load(os.path.join('Assets\\zappers_animation', 'horizontal_zapper2.png')))
        self.horizontal_sprite.append(pygame.image.load(os.path.join('Assets\\zappers_animation', 'horizontal_zapper3.png')))
        self.horizontal_sprite.append(pygame.image.load(os.path.join('Assets\\zappers_animation', 'horizontal_zapper4.png')))
        self.current_horizontal_sprite = 0


''' This function spawn the different zappers on the screen. '''
def zappers_placement(zappers, lasers, death, score):
    position = 'x'   
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
            if position == 'top':
                zapper.rect.y = 10
                zapper.rect.x = random.randint (WIDTH, WIDTH+400)
            if position == 'mid-top':
                zapper.rect.y = 150
                zapper.rect.x = random.randint (WIDTH, WIDTH+400)
            if position == 'mid-bottom':
                zapper.rect.y = 300
                zapper.rect.x = random.randint (WIDTH, WIDTH+400)
            if position == 'bottom':
                zapper.rect.y = 450
                zapper.rect.x = random.randint (WIDTH, WIDTH+400)    
          

''' This function update the animation for the zappers. '''
def update_zappers(zappers):
    for zapper in zappers:
        if zapper.style == 'along':
            zapper.update_vertical()
        if zapper.style == 'across':
            zapper.update_horizontal()
