from data.constants import *

class Lasers(object):
    def __init__(self, pre_rect, post_rect):
        self.pre_rect = pre_rect
        self.post_rect = post_rect
        self.turn_on = sys.maxsize
        self.turn_off = sys.maxsize
        self.cooldown = 4000
        self.scenrio = 1
        #self.left_laser = pygame.transform.scale(LASER_LEFT, (self.left_rect.width, self.left_rect.height))
        #self.right_laser = pygame.transform.scale(LASER_RIGHT, (self.right_rect.width, self.right_rect.height))
        self.pre_lasers = pygame.transform.scale(PRE_LASERS, (self.pre_rect.width, self.pre_rect.height))
        self.post_lasers = pygame.transform.scale(POST_LASERS, (self.post_rect.width, self.post_rect.height))

    def reset(self):
        self.turn_on = sys.maxsize
        self.turn_off = sys.maxsize

    def draw_laser(self, screen):
        # if active is True we going to show the turn off lasers
        # when the active is False we going to turn on the lasers
        screen.blit(self.pre_lasers, (self.pre_rect.x,self.pre_rect.y))
        screen.blit(self.post_lasers, (self.post_rect.x,self.post_rect.y))

        
def lasers_scenrios( lasers, action, scenrio):
    '''
    3 scenrios:
    1. one at the top one at the bottom
    2. 3 at the top 3 at the bottom
    3. 3 in the middle
    '''
    if scenrio == 1:
        if action == 'start-pre-lasers':
            #top lasers
            lasers[0].pre_rect.y = 25   
            #bottom lasers
            lasers[1].pre_rect.y = HEIGHT - 65

        if action == 'start-post-lasers':
            #top lasers
            lasers[0].pre_rect.y = HIDDEN_LASERS_Y  
            lasers[0].post_rect.y = 25
            #bottom lasers
            lasers[1].pre_rect.y = HIDDEN_LASERS_Y  
            lasers[1].post_rect.y = HEIGHT - 65

        if action == 'turn-off-lasers':
            #top lasers
            lasers[0].post_rect.y = HIDDEN_LASERS_Y
            #bottom lasers
            lasers[1].post_rect.y = HIDDEN_LASERS_Y
        
    if scenrio == 2:
        if action == 'start-pre-lasers':
            #top lasers
            lasers[0].pre_rect.y = 25 
            lasers[2].pre_rect.y = 25 + LASER_GAP
            #bottom lasers
            lasers[1].pre_rect.y = HEIGHT - 65
            lasers[3].pre_rect.y = HEIGHT - (65 + LASER_GAP)

        if action == 'start-post-lasers':
            #top lasers
            lasers[0].pre_rect.y = HIDDEN_LASERS_Y
            lasers[2].pre_rect.y = HIDDEN_LASERS_Y
            lasers[0].post_rect.y = 25
            lasers[2].post_rect.y = 25 + LASER_GAP

            #bottom lasers
            lasers[1].pre_rect.y = HIDDEN_LASERS_Y
            lasers[3].pre_rect.y = HIDDEN_LASERS_Y
            lasers[1].post_rect.y = HEIGHT - 65
            lasers[3].post_rect.y = HEIGHT - (65 + LASER_GAP)

        if action == 'turn-off-lasers':
            #top lasers
            lasers[0].post_rect.y = HIDDEN_LASERS_Y
            lasers[2].post_rect.y = HIDDEN_LASERS_Y
            #bottom lasers
            lasers[1].post_rect.y = HIDDEN_LASERS_Y
            lasers[3].post_rect.y = HIDDEN_LASERS_Y

    if scenrio == 3:
        if action == 'start-pre-lasers':
            #mid lasers
            lasers[0].pre_rect.y = HEIGHT//2 + LASER_GAP  
            lasers[1].pre_rect.y = HEIGHT//2
            lasers[2].pre_rect.y = HEIGHT//2 - LASER_GAP

        if action == 'start-post-lasers':
            #top lasers
            lasers[0].pre_rect.y = HIDDEN_LASERS_Y
            lasers[1].pre_rect.y = HIDDEN_LASERS_Y
            lasers[2].pre_rect.y = HIDDEN_LASERS_Y

            lasers[0].post_rect.y = HEIGHT//2 + LASER_GAP   
            lasers[1].post_rect.y = HEIGHT//2
            lasers[2].post_rect.y = HEIGHT//2 - LASER_GAP

        if action == 'turn-off-lasers':
            lasers[0].post_rect.y = HIDDEN_LASERS_Y  
            lasers[1].post_rect.y = HIDDEN_LASERS_Y
            lasers[2].post_rect.y = HIDDEN_LASERS_Y
            

# lasers algorithem to show a warning laser for 4 seconds and then the laser will turn on .
def lasers_placement(score, lasers, laser_timing, silent_music):
    current_time = pygame.time.get_ticks()
    # lasers placement
    if score/laser_timing == 1.0:
        if silent_music == False:
            START_OF_LASER.play()
        lasers_scenrios( lasers,'start-pre-lasers',lasers[0].scenrio)
        lasers[0].turn_on = pygame.time.get_ticks() + lasers[0].cooldown  

    elif 0 <= current_time - lasers[0].turn_on <= 1000:
        if silent_music == False:
            START_OF_LASER.stop()
            LASER_ON.play()
        lasers_scenrios( lasers,'start-post-lasers',lasers[0].scenrio)
        lasers[0].turn_off = pygame.time.get_ticks() + (lasers[0].cooldown)  

    elif 0 <= current_time - lasers[0].turn_off <= 1000:
        if silent_music == False:
            LASER_ON.stop()
        lasers_scenrios( lasers,'turn-off-lasers',lasers[0].scenrio)
            
        laser_timing = random.randint(score+50, score+200) 
        lasers[0].scenrio = random.randint(1,4)
        

    return laser_timing
