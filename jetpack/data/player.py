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
        # set player animation
        self.set_player_animation(self.type)

    ''' This function draw the player to the screen. '''
    def draw(self, screen):
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
            # activate player death animation.
            if self.current_death_sprite < len(self.death_sprites)-1:
                self.current_death_sprite += 0.7
            # fix player from going out of the screen and to fall down to the ground.
            if self.rect.y+self.rect.height < HEIGHT - FIX_IMAGE_LIMIT:
                self.rect.y += 1
            # move the character as he falls forward.
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
        # fix player 'lagging' issue when his head hit the upper screen.
        if self.rect.y <= 0:
            self.rect.y = 1

        # implement movement to the player's jetpack.
        if pygame.time.get_ticks() - start_time < 110:
            if self.rect.y > 0:
                self.rect.y -= self.vel
            if self.rect.x+self.rect.width < WIDTH:
                self.rect.x += 2

    ''' set player alive and death animation. '''
    def set_player_animation(self, type):
        if self.type == 0:
            self.default_male_jetpack_animation()
            self.player_boy_hurt_animation()
        if self.type == 1:
            self.default_female_jetpack_animation()
            self.player_girl_hurt_animation()
        if self.type == 2:
            self.shrek_jetpack_animation()
            self.shrek_hurt_animation()

    ''' This function creates animation to the default male player. '''
    def default_male_jetpack_animation(self):
        DEFAULT_MALE_ASSETS = ["jetpack1.png", "jetpack2.png", "jetpack3.png", "jetpack4.png"]

        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                pygame.image.load(os.path.join(os.getcwd() +'\Assets\\boy_animation_jetpack', asset_name)),(self.rect.width+15, self.rect.height+15))

        self.sprites = [_init_asset(asset_name) for asset_name in DEFAULT_MALE_ASSETS]


    ''' This function creates animation to the default female player. ''' 
    def default_female_jetpack_animation(self):
        DEFAULT_FEMALE_ASSETS = ["playerGirl2.png", "playerGirl3.png", "playerGirl4.png", "playerGirl5.png"]

        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                pygame.image.load(os.path.join(os.getcwd() +'\Assets\girl_animation_jetpack', asset_name)),(self.rect.width+15, self.rect.height+15))

        self.sprites = [_init_asset(asset_name) for asset_name in DEFAULT_FEMALE_ASSETS]


    ''' This function creates animation for the skin shrek. '''
    def shrek_jetpack_animation(self):
        SHREK_ASSETS = ["shrek2.png", "shrek3.png", "shrek4.png", "shrek1.png"]

        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                pygame.image.load(os.path.join(os.getcwd() +'\Assets\shrek_animation_jetpack', asset_name)),(self.rect.width+15, self.rect.height+15))

        self.sprites = [_init_asset(asset_name) for asset_name in SHREK_ASSETS]
 

    ''' This function creates animation to the default male player when he dies. '''
    def player_boy_hurt_animation(self):
        DEFAULT_MALE_HURT_ASSETS = ["playerHurt1.png", "playerHurt2.png", "playerHurt3.png", "playerHurt4.png", "playerHurt5.png", "playerHurt6.png"
                                    , "playerHurt7.png", "playerHurt8.png", "playerHurt9.png", "playerHurt10.png", "playerHurt11.png", "playerHurt12.png"
                                    , "playerHurt13.png", "playerHurt14.png", "playerHurt15.png", "playerHurt16.png", "playerHurt17.png", "playerHurt18.png"]

        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                pygame.image.load(os.path.join(os.getcwd() +'\Assets\player_hurt', asset_name)),(self.rect.width, self.rect.height))

        self.death_sprites = [_init_asset(asset_name) for asset_name in DEFAULT_MALE_HURT_ASSETS]
 

    ''' This function creates animation to the default female player when she dies. '''
    def player_girl_hurt_animation(self):
        DEFAULT_FEMALE_HURT_ASSETS = ["playerGirl_hurt1.png", "playerGirl_hurt2.png", "playerGirl_hurt3.png", "playerGirl_hurt4.png", "playerGirl_hurt5.png", "playerGirl_hurt6.png"
                                    , "playerGirl_hurt7.png", "playerGirl_hurt8.png", "playerGirl_hurt9.png", "playerGirl_hurt10.png", "playerGirl_hurt11.png", "playerGirl_hurt12.png"
                                    , "playerGirl_hurt13.png" ]
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                pygame.image.load(os.path.join(os.getcwd() +'\Assets\player_girl_hurt', asset_name)),(self.rect.width+20, self.rect.height+20))

        self.death_sprites = [_init_asset(asset_name) for asset_name in DEFAULT_FEMALE_HURT_ASSETS]
 
 
    ''' This function creates animation for the skin shrek when he dies. '''
    def shrek_hurt_animation(self):
        SHREK_HURT_ASSETS = ["shrek1.png", "shrek2.png", "shrek3.png", "shrek4.png", "shrek5.png", "shrek6.png" ]
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                pygame.image.load(os.path.join(os.getcwd() +'\Assets\shrek_hurt', asset_name)),(self.rect.width+20, self.rect.height+20))

        self.death_sprites = [_init_asset(asset_name) for asset_name in SHREK_HURT_ASSETS]