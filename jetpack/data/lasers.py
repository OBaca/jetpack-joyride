from data.constants import *

LASERS_ASSETS = ["lasers1.png", "lasers2.png", "lasers3.png", "lasers4.png", "lasers5.png",
                        "lasers6.png", "lasers7.png", "lasers8.png", "lasers9.png", "lasers10.png"
                        , "lasers11.png", "lasers12.png"]

class Lasers(object):
    ''' This class represent a laser obstacle. '''
    def __init__(self):
        self.reset()
        # initialize images for the lasers
        self.pre_lasers = pygame.transform.scale(PRE_LASERS, (self.pre_rect.width, self.pre_rect.height))
        self.post_lasers = pygame.transform.scale(pygame.image.load(os.path.join('Assets\lasers_animation', 'lasers1.png')), (self.post_rect.width, self.post_rect.height))
        self.lasers_animation()


    ''' This function reset all the variables in the class Lasers. '''
    def reset(self):
        # initialize lasers positions
        self.pre_rect = pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50)
        self.post_rect = pygame.Rect(0, HIDDEN_LASERS_Y, 900, 50)
        # timers to turn on and off the lasers
        self.turn_on = sys.maxsize
        self.turn_off = sys.maxsize
        # laser cooldown
        self.cooldown = 4000
        self.laser_timing = 150     # laser timing to start the lasers
        # indicate which scenrio we activate
        self.scenrio = 1
        self.is_running = False
        self.current_sprite = 0


    ''' This function draws the lasers to the screen'''
    def draw_laser(self, screen):
        screen.blit(self.pre_lasers, (self.pre_rect.x,self.pre_rect.y))
        screen.blit(self.post_lasers, (self.post_rect.x,self.post_rect.y))


    ''' This function creates an animation for the post lasers. '''
    def update_post_lasers(self):
        self.current_sprite += 0.25
        if self.current_sprite >= len(self.animation_sprite):
            self.current_sprite = 0
        self.post_lasers = self.animation_sprite[int(self.current_sprite)]


    ''' This function set the image animation for the lasers'''
    def lasers_animation(self):
        def _init_asset(asset_name: str):
            return pygame.image.load(os.path.join(os.getcwd() + "\Assets\lasers_animation", asset_name))

        self.animation_sprite = [_init_asset(asset_name) for asset_name in LASERS_ASSETS]


''' This function set timing for the lasers to turn on and off. '''
def lasers_placement(score, lasers, silent_music):
    current_time = pygame.time.get_ticks()

    # if the lasers is on we are going to start the laser animation
    if lasers[0].is_running:
        for laser in lasers:
            laser.update_post_lasers()

    # show the laser warning for 4 seconds
    if score/lasers[0].laser_timing == 1.0:
        lasers[0].is_running = True
        # play the sound of the lasers warning
        if silent_music == False:
            pygame.mixer.Channel(2).play(START_OF_LASER)

        # activate the laser scenrio
        lasers_scenrios( lasers,'start-pre-lasers',lasers[0].scenrio)
        lasers[0].turn_on = pygame.time.get_ticks() + lasers[0].cooldown  


    # turn on the lasers for 4 seconds
    elif 0 <= current_time - lasers[0].turn_on <= 1000:
        # play the sound of the lasers
        if silent_music == False:
            START_OF_LASER.stop()
            pygame.mixer.Channel(2).play(LASER_ON)

        # activate the laser scenrio
        lasers_scenrios( lasers,'start-post-lasers',lasers[0].scenrio)
        lasers[0].turn_off = pygame.time.get_ticks() + (lasers[0].cooldown)  


    # turn off the lasers and reset to spawn randomly
    elif 0 <= current_time - lasers[0].turn_off <= 1000:
        if silent_music == False:
            LASER_ON.stop()
        lasers_scenrios( lasers,'turn-off-lasers',lasers[0].scenrio)
        lasers[0].is_running = False
        # reset the timing of the laser and the scenrio
        lasers[0].laser_timing = random.randint(score+50, score+200) 
        lasers[0].scenrio = random.randint(1,3)
        

''' This function reset the lasers variables'''
def reset_lasers(lasers, score):
    for laser in lasers:
        laser.reset()
        laser.laser_timing = random.randint(score+50, score+200) 


''' This function set the positions for the lasers by the chosen scenrio. '''
def lasers_scenrios( lasers, action, scenrio):
    # Scenrio 1: one at the top and one at the bottom
    if scenrio == 1:
        if action == 'start-pre-lasers':
            # top lasers
            lasers[0].pre_rect.y = 25   
            # bottom lasers
            lasers[1].pre_rect.y = HEIGHT - 65

        if action == 'start-post-lasers':
            for laser in lasers:
                laser.pre_rect.y = HIDDEN_LASERS_Y

            lasers[0].post_rect.y = 25
            lasers[1].post_rect.y = HEIGHT - 65

        if action == 'turn-off-lasers':
            for laser in lasers:
                laser.post_rect.y = HIDDEN_LASERS_Y

    
    # Scenrio 2: three at the top and three at the bottom
    if scenrio == 2:
        if action == 'start-pre-lasers':
            # top lasers
            lasers[0].pre_rect.y = 25 
            lasers[2].pre_rect.y = 25 + LASER_GAP
            # bottom lasers
            lasers[1].pre_rect.y = HEIGHT - 65
            lasers[3].pre_rect.y = HEIGHT - (65 + LASER_GAP)

        if action == 'start-post-lasers':
            for laser in lasers:
                laser.pre_rect.y = HIDDEN_LASERS_Y
            # top lasers
            lasers[0].post_rect.y = 25
            lasers[2].post_rect.y = 25 + LASER_GAP
            # bottom lasers
            lasers[1].post_rect.y = HEIGHT - 65
            lasers[3].post_rect.y = HEIGHT - (65 + LASER_GAP)

        if action == 'turn-off-lasers':
            for laser in lasers:
                laser.post_rect.y = HIDDEN_LASERS_Y


    # Scenrio 3: three at the middle
    if scenrio == 3:
        if action == 'start-pre-lasers':
            lasers[0].pre_rect.y = HEIGHT//2 + LASER_GAP  
            lasers[1].pre_rect.y = HEIGHT//2
            lasers[2].pre_rect.y = HEIGHT//2 - LASER_GAP

        if action == 'start-post-lasers':
            for laser in lasers:
                laser.pre_rect.y = HIDDEN_LASERS_Y

            lasers[0].post_rect.y = HEIGHT//2 + LASER_GAP   
            lasers[1].post_rect.y = HEIGHT//2
            lasers[2].post_rect.y = HEIGHT//2 - LASER_GAP

        if action == 'turn-off-lasers':
            for laser in lasers:
                laser.post_rect.y = HIDDEN_LASERS_Y
