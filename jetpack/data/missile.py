from .constants import *

class Missile():
    def __init__(self, rect, warning_cooldown=2000, warning_time=500):
        self.rect = rect
        self.warning = [WIDTH+60,100]
        self.launch = [WIDTH+60,150]
        self.homing = False
        self.speed = 14
        self.warning_cooldown = warning_cooldown
        self.launch_cooldown = warning_time
        self.warning_time = sys.maxsize
        self.launch_time = sys.maxsize
        self.missile_launch = False
        self.missile_timing = random.randint(50, 150)
        self.scenrio = random.randint(1,3)

        self.missile_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets','missile1.png')), (100,80))
        self.missile_warning_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets','rocket_warning.png')), (60,60))
        self.missile_launch_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets','warning.png')), (60,60))

    def draw(self, screen):
        
        screen.blit(self.missile_img, (self.rect.x,self.rect.y))
        screen.blit(self.missile_warning_img, (self.warning[0],self.warning[1]))
        screen.blit(self.missile_launch_img, (self.launch[0],self.launch[1]))


    # shoot the missile across the map from right to left to the player last position
    def shoot_missile(self, score, player):
        self.rect.x -= self.speed
        
        # homing missile
        if self.homing == True:
            # changing the difficulty of the missile targeting the player
            missile_difficulty = 100
            if 50 <= score <= 200:
                missile_difficulty = 50
            elif 200 < score <= 500:
                missile_difficulty = 30
            elif score > 500:
                missile_difficulty = 0

            # adding movement to the missile according to the player position
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
            self.rect.x = WIDTH
            self.movement = 0
            self.missile_timing = random.randint(score+10, score+150)


        
def missile_movement(missiles, score, player):

    current_time = pygame.time.get_ticks()
    
    # show warning missile sign
    if score/missiles[0].missile_timing == 1.0:
        missiles_scenrios(missiles, score, player, 'warning-start', 1)
        missiles[0].warning_time = pygame.time.get_ticks() + missiles[0].warning_cooldown
        

    # updating the homing missile to the player position
    missiles[0].warning[1] = player.rect.y

    # show the second warning missile sign
    if missiles[0].scenrio == 2:
        if score/ (missiles[0].missile_timing + 5) == 1.0:
            missiles_scenrios(missiles, score, player, 'warning-start', 2)
            missiles[1].warning_time = pygame.time.get_ticks() + missiles[1].warning_cooldown

    if missiles[0].scenrio == 2:
        missiles[1].warning[1] = player.rect.y + missiles[1].rect.height

    # show launch missile sign
    if 0 <= current_time - missiles[0].warning_time <= 1000:
        missiles_scenrios(missiles, score, player, 'warning-end', 1)
        missiles[0].launch_time = pygame.time.get_ticks() + missiles[0].launch_cooldown
    
    # show the second launch missile sign
    if missiles[0].scenrio == 2:
        if 0 <= current_time -  missiles[1].warning_time  <= 1000:
            missiles_scenrios(missiles, score, player, 'warning-end', 2)
            missiles[1].launch_time = pygame.time.get_ticks() + missiles[1].launch_cooldown

    # launch the missile
    if 0 <= current_time - missiles[0].launch_time <= 1000:
        missiles_scenrios(missiles, score, player, 'shoot', 1)

    if missiles[0].scenrio == 2:
        if 0 <= current_time - missiles[1].launch_time <= 1000:
            missiles_scenrios(missiles, score, player, 'shoot', 2)
        
            
    if missiles[0].missile_launch:
        missiles[0].shoot_missile(score, player)
        missiles[0].scenrio = random.randint(1,3)

    if missiles[1].missile_launch:
        missiles[1].shoot_missile(score, player)
        
        



def missiles_scenrios(missiles, score, player, action, scenrio):
    '''
    scenrios:
        1. one targeting missile
        2. two missiles
        3. 6 missiles from the beginning to the top
        4. 6 missiles from the top to the beginning
    '''
    
    if action == 'warning-start':
        if scenrio == 1:
            missiles[0].homing = True
            missiles[0].warning[0] = WIDTH-60
            missiles[0].warning[1] = player.rect.y
        if scenrio == 2:
            missiles[1].homing = True
            missiles[1].warning[0] = WIDTH-60 
            missiles[1].warning[1] = player.rect.y + missiles[1].rect.height
        
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
        

    if action == 'shoot':
        if scenrio == 1:
            missiles[0].launch[0] = WIDTH+60
            missiles[0].launch[1] = player.rect.y
            missiles[0].missile_launch = True
        if scenrio == 2:
            missiles[1].launch[0] = WIDTH+60
            missiles[1].launch[1] = player.rect.y
            missiles[1].missile_launch = True



