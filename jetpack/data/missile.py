from .constants import *


MISSILE_ASSETS = [init_animation('missile',i) for i in range(1,8)]

class Missile():
    ''' This class represent a missile obstacle. '''
    def __init__(self, player_y):
        self.reset(player_y)
        self.warning = [WIDTH+60,100]
        self.launch = [WIDTH+60,150]
        # set images
        self.missile_img = pygame.transform.scale(load_image('missile_animation/missile_off.png'), (100,80))
        self.missile_warning_img = pygame.transform.scale(load_image('missile_animation/rocket_warning.png'), (60,60))
        self.missile_launch_img = pygame.transform.scale(load_image('missile_animation/warning.png'), (60,60))
        # set missile animation
        self.missile_animation(MISSILE_ASSETS)


    ''' This function reset all the missile variables.'''
    def reset(self, player_y, warning_cooldown=2000, warning_time=500):
        self.rect = pygame.Rect(WIDTH+10,player_y, 100, 100)
        self.current_sprite = 0
        # set the missile to follow the play y position.
        self.homing = False
        # cooldown for the missile warning and launch message.
        self.warning_cooldown = warning_cooldown
        self.launch_cooldown = warning_time
        # set the speed and the timing of the missile to spawn.
        self.speed = 14
        self.missile_timing = 70
        self.warning_time = sys.maxsize
        self.launch_time = sys.maxsize
        # indicate  if the missile was launched.
        self.missile_launch = False
        # set a random scenrio to spawn.
        self.scenrio = random.randint(1,2)


    ''' This function draw the missile images on the screen. '''
    def draw(self, screen):
        screen.blit(self.missile_img, (self.rect.x,self.rect.y))
        screen.blit(self.missile_warning_img, (self.warning[0],self.warning[1]))
        screen.blit(self.missile_launch_img, (self.launch[0],self.launch[1]))


    ''' This function creates an animation for the missile. '''
    def update(self):
        self.current_sprite += 0.50
        if self.current_sprite >= len(self.smoke_sprites):
            self.current_sprite = 0
        self.missile_img = self.smoke_sprites[int(self.current_sprite)]


    ''' This function shoot the missile from the right side of the screen to the player position. '''
    def shoot_missile(self, score, player):
        self.rect.x -= self.speed
        # homing missile.
        if self.homing == True:
            # changing the difficulty of the missile targeting the player.
            missile_difficulty = 100
            if 50 <= score <= 200:
                missile_difficulty = 50
            elif 200 < score <= 500:
                missile_difficulty = 30
            elif score > 500:
                missile_difficulty = 0

            # adding movement to the missile according to the player position.
            if player.rect.y >= self.rect.y and self.rect.x - player.rect.x >= missile_difficulty:
                self.rect.y += 1
            elif player.rect.y <= self.rect.y and self.rect.x - player.rect.x >= missile_difficulty:
                self.rect.y -= 1
        else:
            missile_position = self.rect.y
            if missile_position >= self.rect.y:
                self.rect.y += 1
            else:
                self.rect.y -= 1

        # reset the missile to the next starting point
        if self.rect.x + self.rect.width < 0:
            self.missile_launch = False
            self.rect.x = WIDTH + 10
            self.movement = 0
            self.missile_timing = random.randint(score+10, score+200)


    ''' This function set the missile animation. '''
    def missile_animation(self, missile_animation_asset):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(load_image(os.path.join("missile_animation", asset_name)), (self.rect.width+15, self.rect.height+15))

        self.smoke_sprites = [_init_asset(asset_name) for asset_name in missile_animation_asset]

        
''' This function set the timing to activate the missile warning and launch options. '''
def missile_movement(missiles, score, player, silent_music):
    current_time = pygame.time.get_ticks()
    
    # show warning missile sign
    if score/missiles[0].missile_timing == 1.0:
        missiles_scenrios(missiles, player, 'warning-start', 1)
        missiles[0].warning_time = pygame.time.get_ticks() + missiles[0].warning_cooldown
        
    # updating the homing missile to the player position
    missiles[0].warning[1] = player.rect.y

    # show the second warning missile sign
    if missiles[0].scenrio == 2:
        if score/ (missiles[0].missile_timing + 5) == 1.0:
            missiles_scenrios(missiles, player, 'warning-start', 2)
            missiles[1].warning_time = pygame.time.get_ticks() + missiles[1].warning_cooldown


    # update the second missile at scenrio 2 so the image won't interfere the second image.
    if missiles[0].scenrio == 2:
        missiles[1].warning[1] = player.rect.y + missiles[1].rect.height


    # show missile launch sign.
    if 0 <= current_time - missiles[0].warning_time <= 1000:
        missiles_scenrios(missiles, player, 'warning-end', 1)
        missiles[0].launch_time = pygame.time.get_ticks() + missiles[0].launch_cooldown

        # starting the missile warning sound.
        if silent_music == False:
            pygame.mixer.Channel(3).play(MISSILE_WARNING)

    # show the second missile launch missile sign.
    if missiles[0].scenrio == 2:
        if 0 <= current_time -  missiles[1].warning_time  <= 1000:
            missiles_scenrios(missiles, player, 'warning-end', 2)
            missiles[1].launch_time = pygame.time.get_ticks() + missiles[1].launch_cooldown

            # starting the second missile warning sound.
            if silent_music == False:
                pygame.mixer.Channel(5).play(MISSILE_WARNING)


    # launch the missile.
    if 0 <= current_time - missiles[0].launch_time <= 1000:
        # starting the missile launch sound.
        if silent_music == False:
            pygame.mixer.Channel(4).play(MISSILE_LAUNCHED)
        missiles_scenrios(missiles, player, 'shoot', 1)

    # launch the second missile.
    if missiles[0].scenrio == 2:
        if 0 <= current_time - missiles[1].launch_time <= 1000:
            # starting the missile launch sound.
            if silent_music == False:
                pygame.mixer.Channel(6).play(MISSILE_LAUNCHED)
            missiles_scenrios(missiles, player, 'shoot', 2)
         
    # start the animation of the missile and shoot the missile to the player position.
    if missiles[0].missile_launch:
        missiles[0].update()
        missiles[0].shoot_missile(score, player)
        missiles[0].scenrio = random.randint(1,2)
    if missiles[1].missile_launch:
        missiles[1].update()
        missiles[1].shoot_missile(score, player)
        
        
''' This function set the missile position according to the scenrio given. '''
def missiles_scenrios(missiles, player, action, scenrio):
    '''
    scenrios:
        1. one targeting missile
        2. two missiles
    '''
    # start the warning sign phase.
    if action == 'warning-start':
        if scenrio == 1:
            missiles[0].homing = True
            missiles[0].warning[0] = WIDTH-60
            missiles[0].warning[1] = player.rect.y
        if scenrio == 2:
            missiles[1].homing = True
            missiles[1].warning[0] = WIDTH-60 
            missiles[1].warning[1] = player.rect.y + missiles[1].rect.height
        
    # start the launch sign phase.
    if action == 'warning-end':
        if scenrio == 1:
            missiles[0].warning[0] = WIDTH+60
            missiles[0].warning[1] = player.rect.y
            missiles[0].launch[0] = WIDTH-60
            missiles[0].launch[1] = player.rect.y
            missiles[0].rect.y = player.rect.y
        if scenrio == 2:
            missiles[1].warning[0] = WIDTH+60
            missiles[1].warning[1] = player.rect.y + missiles[1].rect.height
            missiles[1].launch[0] = WIDTH-60
            missiles[1].launch[1] = player.rect.y + missiles[1].rect.height
            missiles[1].rect.y = player.rect.y + missiles[1].rect.height
        
    # shoot the missile.
    if action == 'shoot':
        if scenrio == 1:
            missiles[0].launch[0] = WIDTH+60
            missiles[0].launch[1] = player.rect.y
            missiles[0].missile_launch = True
        if scenrio == 2:
            missiles[1].launch[0] = WIDTH+60
            missiles[1].launch[1] = player.rect.y
            missiles[1].missile_launch = True
