from .constants import *

class Zombie(object):
    def __init__(self, right, x):
        if right:
            self.rect = pygame.Rect(x,460,100,100)
        else:
            self.rect = pygame.Rect(x,460,100,100)

        self.zombie_walking_animation()
        self.current_sprite = 0
        self.image = self.walking_right[self.current_sprite]
        if right:
            self.increase_x = 1
        else:
            self.increase_x = -1
        
        self.timing_speed = 0
        self.speed = random.choice([0.4,0.7,1])
        self.right = right

        
    
    def update(self):
        sprites = []
        if self.right:
            sprites = self.walking_right
        else:
            sprites = self.walking_left

        self.timing_speed += self.speed
        if self.timing_speed > 1:
            self.rect.x += self.increase_x
            self.timing_speed = 0

        self.current_sprite += 0.25

        if self.current_sprite >= len(self.walking_right):
            self.current_sprite = 0
        
        self.image = sprites[int(self.current_sprite)]

        if self.right:
            if self.rect.x > WIDTH:
                self.rect.x = self.rect.width*(-1)
                self.speed = random.choice([0.4,0.7,1])
        else:
            if self.rect.x < 0:
                self.rect.x = WIDTH
                self.speed = random.choice([0.4,0.7,1])

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))


    def zombie_walking_animation(self):
        self.walking_right = []
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_000.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_001.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_002.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_003.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_004.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_005.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_006.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_007.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_008.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_009.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_010.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_011.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_012.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_013.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_014.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_015.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_016.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_017.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_018.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_019.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_020.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_021.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_022.png')), (self.rect.width,self.rect.height)))
        self.walking_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_023.png')), (self.rect.width,self.rect.height)))

        self.walking_left = []
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_000.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_001.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_002.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_003.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_004.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_005.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_006.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_007.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_008.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_009.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_010.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_011.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_012.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_013.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_014.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_015.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_016.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_017.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_018.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_019.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_020.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_021.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_022.png')), (self.rect.width,self.rect.height)), True, False))
        self.walking_left.append(pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('Assets\zombie_walking', '0_Golem_Walking_023.png')), (self.rect.width,self.rect.height)), True, False))
            


def zombie_spawn_menu(zombies, screen):
    for zombie in zombies:
        zombie.draw(screen)
        zombie.update()