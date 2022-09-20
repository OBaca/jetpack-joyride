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

        self.missile_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets','missile1.png')), (100,80))
        self.missile_warning_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets','rocket_warning.png')), (60,60))
        self.missile_launch_img = pygame.transform.scale(pygame.image.load(os.path.join('Assets','warning.png')), (60,60))

    def draw(self, screen):
        
        screen.blit(self.missile_img, (self.rect.x,self.rect.y))
        screen.blit(self.missile_warning_img, (self.warning[0],self.warning[1]))
        screen.blit(self.missile_launch_img, (self.launch[0],self.launch[1]))
        
    def missile_movement(self, score, player):
        current_time = pygame.time.get_ticks()

        # show warning missile sign
        if score/self.missile_timing == 1.0:
            self.warning[0] = WIDTH-60
            self.warning[1] = player.rect.y
            self.warning_time = pygame.time.get_ticks() + self.warning_cooldown

        self.warning[1] = player.rect.y

        # show launch missile sign
        if 0 <= current_time - self.warning_time <= 1000:
            self.warning[0] = WIDTH+60
            self.warning[1] = player.rect.y

            self.launch[0] = WIDTH-60
            self.launch[1] = player.rect.y
            self.launch_time = pygame.time.get_ticks() + self.launch_cooldown
            self.rect.y = player.rect.y

        # launch the missile
        if 0 <= current_time - self.launch_time <= 1000:
            self.launch[0] = WIDTH+60
            self.launch[1] = player.rect.y
            self.missile_launch = True
            
        if self.missile_launch:
            self.shoot_missile(score, player)
        

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
        
        # reset the missile to the next starting point
        if self.rect.x + self.rect.width < 0:
            self.missile_launch = False
            self.rect.x = WIDTH
            self.movement = 0
            self.missile_timing = random.randint(score+10, score+150)


def missiles_scenrios(missiles):
    '''
    scenrios:
        1. one targeting missile
        2. 3 missiles spanwed randomly
        3. 6 missiles from the beginning to the top
        4. 6 missiles from the top to the beginning
    '''
    if scenrio == 1:
        missile.homing = True
        

    pass
