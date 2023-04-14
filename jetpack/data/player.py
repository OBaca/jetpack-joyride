from data.constants import *

# players type
players_selection = {'default-male-player':0, 'default-female-player':1, 'shrek':2}

# jetpack animation assets
DEFAULT_MALE_ASSETS = [init_animation('jetpack',i) for i in range(1,5)]
DEFAULT_FEMALE_ASSETS = [init_animation('playerGirl',i) for i in range(2,6)]
SHREK_ASSETS = [init_animation('shrek',i) for i in range(1,5)]

# death animation assets
DEFAULT_MALE_HURT_ASSETS = [init_animation('playerHurt',i) for i in range(1,19)]
DEFAULT_FEMALE_HURT_ASSETS = [init_animation('playerGirl_hurt',i) for i in range(1,14)]
SHREK_HURT_ASSETS = [init_animation('shrek',i) for i in range(1,7)]

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
        self.up_vel = 0
        self.down_vel = 0 
        self.max_vel = 7
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


    ''' This function is increasing speed to the velocity of the player when the player jetpack is on. '''
    def player_up_velocity(self):
        self.up_vel += 0.5
        return min(self.up_vel, self.max_vel)
    

    ''' This function is increasing speed to the velocity of the player when the player jetpack is off. '''
    def player_down_velocity(self):
        self.down_vel += 0.5
        return min(self.down_vel, self.gravity)


    ''' This function manage the player movement. '''
    def player_movement(self, pressed_key, start_time):
        # a/d or left/right - the movement of the player to the left or the right.
        if (pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]) and self.rect.x > 0 and self.death == False:
            self.rect.x -= self.vel
        elif (pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]) and self.rect.x + self.rect.width < WIDTH and self.death == False:
            self.rect.x += self.vel

        # space/W/up key - to jump and animate jetpack animation.
        if (pressed_key[pygame.K_SPACE] or pressed_key[pygame.K_w] or pressed_key[pygame.K_UP] ) and self.rect.y > 0 and self.death == False:
            self.rect.y -= self.player_up_velocity()
            self.update_jetpack()
            self.down_vel = 0

        # implement gravity to the player with a jetpack "feel".
        #elif pygame.time.get_ticks() - start_time > 110:
        if self.rect.y + self.rect.height < HEIGHT - FIX_IMAGE_LIMIT:
            self.rect.y += self.player_down_velocity()

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

    ''' set player alive and death animation. '''
    def set_player_animation(self, type):
        if self.type == 0:
            self.default_male_jetpack_animation(DEFAULT_MALE_ASSETS)
            self.player_boy_hurt_animation(DEFAULT_MALE_HURT_ASSETS)
        if self.type == 1:
            self.default_female_jetpack_animation(DEFAULT_FEMALE_ASSETS)
            self.player_girl_hurt_animation(DEFAULT_FEMALE_HURT_ASSETS)
        if self.type == 2:
            self.shrek_jetpack_animation(SHREK_ASSETS)
            self.shrek_hurt_animation(SHREK_HURT_ASSETS)

    ''' This function creates animation to the default male player. '''
    def default_male_jetpack_animation(self, animation_asset):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                load_image(os.path.join('boy_animation_jetpack', asset_name)),(self.rect.width+15, self.rect.height+15))

        self.sprites = [_init_asset(asset_name) for asset_name in animation_asset]


    ''' This function creates animation to the default female player. ''' 
    def default_female_jetpack_animation(self, animation_asset):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                load_image(os.path.join('girl_animation_jetpack', asset_name)),(self.rect.width+15, self.rect.height+15))

        self.sprites = [_init_asset(asset_name) for asset_name in animation_asset]


    ''' This function creates animation for the skin shrek. '''
    def shrek_jetpack_animation(self, animation_asset):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                load_image(os.path.join('shrek_animation_jetpack', asset_name)),(self.rect.width+15, self.rect.height+15))

        self.sprites = [_init_asset(asset_name) for asset_name in animation_asset]
 

    ''' This function creates animation to the default male player when he dies. '''
    def player_boy_hurt_animation(self, animation_asset):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                load_image(os.path.join('player_hurt', asset_name)),(self.rect.width, self.rect.height))

        self.death_sprites = [_init_asset(asset_name) for asset_name in animation_asset]
 

    ''' This function creates animation to the default female player when she dies. '''
    def player_girl_hurt_animation(self, animation_asset):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                load_image(os.path.join('player_girl_hurt', asset_name)),(self.rect.width+20, self.rect.height+20))

        self.death_sprites = [_init_asset(asset_name) for asset_name in animation_asset]
 
 
    ''' This function creates animation for the skin shrek when he dies. '''
    def shrek_hurt_animation(self, animation_asset):
        def _init_asset(asset_name: str):
            return pygame.transform.scale(
                load_image(os.path.join('shrek_hurt', asset_name)),(self.rect.width+20, self.rect.height+20))

        self.death_sprites = [_init_asset(asset_name) for asset_name in animation_asset]
        