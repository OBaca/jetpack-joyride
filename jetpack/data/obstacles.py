from data.constants import *

class Zappers(object):
    def __init__(self, rect, style, image): #x, y, width, height,
        self.rect = rect
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        '''
        self.speed = 2
        self.style = style
        self.image = image
        self.obs_pos = [300, WIDTH+150, WIDTH+350, WIDTH+500]
        #self.collision = (self.x,self.y,self.width,self.height)
        

    def reset(self):
        if self.style == 'along':
            self.rect.x = random.randint(WIDTH, WIDTH+200)
            self.rect.y = random.randint(FIX_IMAGE_LIMIT, HEIGHT-140)
        if self.style == 'across':
            self.rect.x = random.randint(WIDTH, WIDTH+200)
            self.rect.y = random.randint(FIX_IMAGE_LIMIT, HEIGHT- FIX_IMAGE_LIMIT -40)


    def draw_obstacle(self, screen):
        #pygame.draw.rect(screen,BLACK,self.collision)
        screen.blit(self.image, (self.rect.x,self.rect.y))

        '''
        pos_x, pos_y = 10, 10
        if self.style == 'across':
            pos_x, pos_y = 5, 10
        if self.style == 'along':
            pos_x, pos_y = 10, 5
        #self.rect = pygame.Rect(self.rect.x + pos_x, self.rect.y + pos_y, self.rect.width, self.rect.height)
        #self.collision = (self.x + pos_x, self.y + pos_y, self.width, self.height)
        #screen.blit(self.image, (self.x,self.y))
        '''
        
        

# place the different obstacles on the screen
def obstacle_placement(obstacles):
    positions = ['top', 'mid-top','mid-bottom','bottom']
    position = 'x'
    # small across and along obstacles that are spawned together.
    for obstacle in obstacles:
        obstacle.rect.x -= obstacle.speed
        if obstacle.rect.x + obstacle.rect.width <0:
            while position == 'x':
                position = random.choice(positions)
            positions = [p.replace(position, 'x') for p in positions]
            if position == 'top':
                obstacle.rect.y = 10
                obstacle.rect.x = random.randint (WIDTH, WIDTH+300)
            if position == 'mid-top':
                obstacle.rect.y = HEIGHT//4
                obstacle.rect.x = random.randint (WIDTH, WIDTH+300)
            if position == 'mid-bottom':
                obstacle.rect.y = HEIGHT//2
                obstacle.rect.x = random.randint (WIDTH, WIDTH+300)
            if position == 'bottom':
                obstacle.rect.y = 450
                obstacle.rect.x = random.randint (WIDTH, WIDTH+300)    
            

def draw_obstacles(obstacles,lasers, screen):
    for i in range(len(obstacles)):
        obstacles[i].draw_obstacle(screen)
    for i in range(len(lasers)):   
        lasers[i].draw_laser(screen)


def reset_obstacle_pos(obstacles, lasers):
    for obstacle in obstacles:
        obstacle.reset()
    for laser in lasers:
        laser.reset()

