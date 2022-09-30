from data.constants import *

# players type
players_selection = {'default-male-player':0, 'default-female-player':1, 'shrek':2}

class Player(object):
    ''' This class represent the player in the game. '''
    def __init__(self, image, type):
        self.reset(image, type)
        
        
    ''' This function reset the player variables. '''
    def reset(self, image, type):
        # the type of the player
        self.type = type
        self.rect = pygame.Rect(100,450,60,75)
        self.vel = 7
        self.gravity = 8
        self.image = image
        # death sprite index
        self.current_death_sprite = 0
        # indicate if the player died
        self.death = False
        # player animation index
        self.current_sprite = 0
        # set player alive and death animation.
        if self.type == 0:
            self.default_male_jetpack_animation()
            self.player_boy_hurt_animation()
        if self.type == 1:
            self.default_female_jetpack_animation()
            self.player_girl_hurt_animation()


    ''' This function draw the player to the screen. '''
    def draw(self, screen, map):
        screen.blit(self.image, (self.rect.x,self.rect.y))


    ''' This function creates an animation to the jetpack. '''
    def update_jetpack(self):
        self.current_sprite += 0.25
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0  
        self.image = self.sprites[int(self.current_sprite)]


    ''' This function animate the death scene. '''
    def death_scene(self, death_end_time):
        if self.death:
            current_time = pygame.time.get_ticks()
            # activate player death animation
            if self.current_death_sprite < len(self.death_sprites)-1:
                self.current_death_sprite += 0.7
            if self.rect.y+self.rect.height < HEIGHT - FIX_IMAGE_LIMIT:
                self.rect.y += 1
            if self.rect.x < WIDTH - (FIX_IMAGE_LIMIT*3):
                self.rect.x += 3 
            
            self.current_death_sprite = (len(self.death_sprites)-1)
        
            self.image = self.death_sprites[int(self.current_death_sprite)]

            if 0 <= current_time - death_end_time <= 1000:
                return True


    ''' This function manage the player movement. '''
    def player_movement(self, pressed_key, start_time):
        # a/d -> left/right movement.
        if pressed_key[pygame.K_a] and self.rect.x > 0 and self.death == False:
            self.rect.x -= self.vel
        elif pressed_key[pygame.K_d] and self.rect.x + self.rect.width < WIDTH and self.death == False:
            self.rect.x += self.vel

        # space key to jump and animate jetpack animation.
        if pressed_key[pygame.K_SPACE] and self.rect.y > 0 and self.death == False:
            self.rect.y -= self.vel
            self.update_jetpack()

        # implement gravity to the player with a jetpack "feel".
        elif pygame.time.get_ticks() - start_time > 110:
            if self.rect.y + self.rect.height < HEIGHT - FIX_IMAGE_LIMIT:
                self.rect.y += self.gravity

        # fix the player image to the screen frame
        elif self.rect.y + self.rect.height + self.vel >= HEIGHT - FIX_IMAGE_LIMIT:
            self.rect.y = HEIGHT - self.rect.height - FIX_IMAGE_LIMIT
        if self.rect.y <= 0:
            self.rect.y = 1

        # implement movement to the player's jetpack.
        if pygame.time.get_ticks() - start_time < 110:
            self.rect.y -= self.vel
            self.rect.x += 2


    ''' This function creates animation to the default male player. '''
    def default_male_jetpack_animation(self):
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\boy_animation_jetpack', 'jetpack1.png')), (self.rect.width+15, self.rect.height+15)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\boy_animation_jetpack', 'jetpack2.png')), (self.rect.width+15, self.rect.height+15)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\boy_animation_jetpack', 'jetpack3.png')), (self.rect.width+15, self.rect.height+15)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\boy_animation_jetpack', 'jetpack4.png')), (self.rect.width+15, self.rect.height+15)))


    ''' This function creates animation to the default female player. ''' 
    def default_female_jetpack_animation(self):
        self.sprites = []
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\girl_animation_jetpack', 'playerGirl2.png')), (self.rect.width+15, self.rect.height+15)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\girl_animation_jetpack', 'playerGirl3.png')), (self.rect.width+15, self.rect.height+15)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\girl_animation_jetpack', 'playerGirl4.png')), (self.rect.width+15, self.rect.height+15)))
        self.sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\girl_animation_jetpack', 'playerGirl5.png')), (self.rect.width+15, self.rect.height+15)))
        

    ''' This function creates animation to the default male player when he dies. '''
    def player_boy_hurt_animation(self):
        self.death_sprites = []
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt1.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt2.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt3.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt4.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt5.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt6.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt7.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt8.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt9.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt10.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt11.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt12.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt13.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt14.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt15.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt16.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt17.png')), (self.rect.width, self.rect.height)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_hurt', 'playerHurt18.png')), (self.rect.width, self.rect.height)))


    ''' This function creates animation to the default female player when she dies. '''
    def player_girl_hurt_animation(self):
        self.death_sprites = []
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt1.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt2.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt3.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt4.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt5.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt6.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt7.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt8.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt9.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt10.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt11.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt12.png')), (self.rect.width+20, self.rect.height+20)))
        self.death_sprites.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\player_girl_hurt', 'playerGirl_hurt13.png')), (self.rect.width+20, self.rect.height+20)))
