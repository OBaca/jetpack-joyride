from .constants import *

class Button():
    def __init__(self, rect, image):
        self.rect = rect
        self.image = image
        self.pressed = False
        self.hover = False
        
    
    def draw_button(self, screen, style):
        active = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if self.hover == False:
                self.button_hover_change(style)
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                active = True
        else:
            if self.hover:
                self.button_hover_change(style)

        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
        
        

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return active


    def button_hover_change(self,style):
        if style == 'play':
            if self.hover:
                self.image = PLAY_MENU_NO_HOVER_BUTTON
                self.hover = False
            else:
                self.image = PLAY_MENU_HOVER_BUTTON
                self.hover = True
        if style == 'quit_menu':
            if self.hover:
                self.image = QUIT_MENU_NO_HOVER_BUTTON
                self.hover = False
            else:
                self.image = QUIT_MENU_HOVER_BUTTON
                self.hover = True
        if style == 'costumes':
            if self.hover:
                self.image = COSTUMES_MENU_NO_HOVER_BUTTON
                self.hover = False
            else:
                self.image = COSTUMES_MENU_HOVER_BUTTON
                self.hover = True
        if style == 'retry':
            if self.hover:
                self.image = RETRY_BUTTON
                self.hover = False
            else:
                self.image = RETRY_HOVER_BUTTON
                self.hover = True
        if style == 'resume':
            if self.hover:
                self.image = RESUME_NO_HOVER_BUTTON
                self.hover = False
            else:
                self.image = RESUME_HOVER_BUTTON
                self.hover = True
        if style == 'quit_game':
            if self.hover:
                self.image = QUIT_GAME_BUTTON
                self.hover = False
            else:
                self.image = QUIT_GAME_HOVER_BUTTON
                self.hover = True
        if style == 'speaker-off':
            if self.hover:
                self.image = SPEAKER_OFF_BUTTON
                self.hover = False
            else:
                self.image = SPEAKER_OFF_HOVER_BUTTON
                self.hover = True
        if style == 'speaker-on':
            if self.hover:
                self.image = SPEAKER_ON_BUTTON
                self.hover = False
            else:
                self.image = SPEAKER_ON_HOVER_BUTTON
                self.hover = True
        if style == 'left-arrow':
            if self.hover:
                self.image = LEFT_ARROW
                self.hover = False
            else:
                self.image = LEFT_ARROW_HOVER
                self.hover = True
        if style == 'right-arrow':
            if self.hover:
                self.image = RIGHT_ARROW
                self.hover = False
            else:
                self.image = RIGHT_ARROW_HOVER
                self.hover = True
        if style == 'buy':
            if self.hover:
                self.rect.x = 300
                self.rect.y = 550
                self.rect.height = MENU_BUTTON_WIDTH
                self.rect.width - MENU_BUTTON_WIDTH
                self.image = BUY_BUTTON
                self.hover = False
            else:
                self.rect.x = 305
                self.rect.y = 555
                self.rect.height = MENU_BUTTON_WIDTH - 5
                self.rect.width - MENU_BUTTON_WIDTH + 5
                #self.image = BUY_BUTTON_HOVER
                self.hover = True
        if style == 'select':
            if self.hover:
                self.rect.x = 300
                self.rect.y = 550
                self.rect.height = MENU_BUTTON_WIDTH
                self.rect.width - MENU_BUTTON_WIDTH
                self.image = SELECT_BUTTON
                self.hover = False
            else:
                self.rect.x = 305
                self.rect.y = 555
                self.rect.height = MENU_BUTTON_WIDTH - 5
                self.rect.width - MENU_BUTTON_WIDTH + 5
                #self.image = SELECT_BUTTON_HOVER
                self.hover = True
        if style == 'main-menu':
            if self.hover:
                self.rect.x = 20
                self.rect.y = 550
                self.rect.height = MENU_BUTTON_WIDTH
                self.rect.width - MENU_BUTTON_WIDTH
                self.image = MAIN_MENU_BUTTON
                self.hover = False
            else:
                self.rect.x = 25
                self.rect.y = 555
                self.rect.height = MENU_BUTTON_WIDTH - 5
                self.rect.width - MENU_BUTTON_WIDTH + 5
                #self.image = SELECT_BUTTON_HOVER
                self.hover = True