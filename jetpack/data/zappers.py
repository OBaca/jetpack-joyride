from data.constants import *

class Zappers(object):
    def __init__(self, rect, style, image): #x, y, width, height,
        self.rect = rect
        self.speed = 2
        self.increase_speed = 0
        self.style = style
        self.image = image
        self.positions = ['top', 'mid-top','mid-bottom','bottom']
        

    def reset(self):
        
        self.speed = 2
        if self.style == 'along':
            self.rect.x = random.randint(WIDTH, WIDTH+200)
            self.rect.y = random.randint(FIX_IMAGE_LIMIT, HEIGHT-140)
        if self.style == 'across':
            self.rect.x = random.randint(WIDTH, WIDTH+200)
            self.rect.y = random.randint(FIX_IMAGE_LIMIT, HEIGHT- FIX_IMAGE_LIMIT -40)


    def draw_zapper(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))

# place the different zappers on the screen
def zappers_placement(zappers, lasers, death, score):
    
    position = 'x'
    
    # setting the zappers speed increase timing
    zappers_speed_timing = 50
    if score >= 300:
        zappers_speed_timing = 80
    if score >= 1300:
        zappers_speed_timing = 100

    # small across and along zappers that are spawned together.
    for zapper in zappers:
        if score%zappers_speed_timing == 0:
            zapper.increase_speed += 0.5
            if zapper.increase_speed >= 10:
                zapper.speed += 1
                zapper.increase_speed = 0

        # the zappers are moving only if the player is alive
        if death == False:
            zapper.rect.x -= zapper.speed
        # check if the lasers is running so we won't place zapper with a laser and reset the zapper positions
        if zapper.rect.x + zapper.rect.width <0 and lasers[0].is_running == False:
            zapper.positions = ['top', 'mid-top','mid-bottom','bottom']
            while position == 'x':
                position = random.choice(zapper.positions )
                print(position)
            zapper.positions = [p.replace(position, 'x') for p in zapper.positions]

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
          