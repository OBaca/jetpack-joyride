from .constants import *

class Missile():
    def __init__(self, rect):
        self.rect = rect
        self.warning = [WIDTH+60,100]
        self.launch = [WIDTH+60,150]
        self.homing = False
        self.speed = 14
        self.warning_cooldown = 2000
        self.launch_cooldown = 500
        self.warning_time = sys.maxsize
        self.launch_time = sys.maxsize
        self.missile_launch = False
        self.missile_timing = 20 #random.randint(50, 150)
        self.scenrio = 1

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
        missiles_scenrios(missiles[0], score, player, 'warning-start')
        missiles[0].warning_time = pygame.time.get_ticks() + missiles[0].warning_cooldown

    # updating the homing missile to the player position
    if missiles[0].scenrio == 1:
        missiles[0].warning[1] = player.rect.y

    # show launch missile sign
    if 0 <= current_time - missiles[0].warning_time <= 1000:
        missiles_scenrios(missiles[0], score, player, 'warning-end')
        missiles[0].launch_time = pygame.time.get_ticks() + missiles[0].launch_cooldown
        

    # launch the missile
    if 0 <= current_time - missiles[0].launch_time <= 1000:
        missiles_scenrios(missiles[0], score, player, 'shoot')
        
            
    if missiles[0].missile_launch:
        missiles[0].shoot_missile(score, player)
        missiles[0].scenrio = random.randint(1,5)
        



def missiles_scenrios(missiles, score, player, action):
    '''
    scenrios:
        1. one targeting missile
        2. 3 missiles spanwed randomly
        3. 6 missiles from the beginning to the top
        4. 6 missiles from the top to the beginning
    '''
    scenrio = random.randint(1,5)
    if missiles[0].scenrio == 1:
        if action == 'warning-start':
            missiles[0].homing = True
            missiles[0].warning[0] = WIDTH-60
            missiles[0].warning[1] = player.rect.y
            missiles[0].missile_movement(score, player)
        
        if action == 'warning-end':
            missiles[0].warning[0] = WIDTH+60
            missiles[0].warning[1] = player.rect.y
            missiles[0].launch[0] = WIDTH-60
            missiles[0].launch[1] = player.rect.y
            missiles[0].rect.y = player.rect.y

        if action == 'shoot':
            missiles[0].launch[0] = WIDTH+60
            missiles[0].launch[1] = player.rect.y
            missiles[0].missile_launch = True



    if missiles[0].scenrio == 2:
        missiles[0].homing - False



    pass
