from .constants import *

class Button():
    '''
    Button class represent a button in the game
    '''
    def __init__(self, rect, image_not_hover, image_hover):
        self.rect = rect
        self.image = image_not_hover
        self.image_hover = image_hover
        self.image_not_hover = image_not_hover
        self.pressed = False    # to check if the player pressed the button
        self.hover = False      # to know if we changed the image to the image with an hover effect
        
    '''
    This function draw the button on the screen
    '''
    def draw_button(self, screen, style):
        active = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            # if we put the mouse on the button we will change the image to an image with an hover effect
            if self.hover == False:
                self.button_hover_change(style)
        
            # if we pressed the button
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                active = True
        # if the mouse not on the button we change the button to a normal image (without hover effect)
        else:
            if self.hover:
                self.button_hover_change(style)
                

        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
        
        # show the button on the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return active

    ''' This function change the button size in the costumes menu if the mouse on it. '''
    def button_size_change(self,style):
        if style == 'buy' or style == 'select' or style == 'main-menu':
            self.rect.height = MENU_BUTTON_HEIGHT if self.hover else MENU_BUTTON_HEIGHT - 5
            self.rect.width - MENU_BUTTON_WIDTH if self.hover else MENU_BUTTON_WIDTH + 5
            self.rect.y = 550 if self.hover else 555

            if style == 'buy' or style == 'select':
                self.rect.x = 300 if self.hover else 305

            if style == 'main-menu':
                self.rect.x = 20 if self.hover else 25
        
        

    ''' This function gets a style variable and choose the correct image with an hover effect or not. '''
    def button_hover_change(self, style):
        self.button_size_change(style)
        self.hover = not self.hover
        self.image = self.image_hover if self.hover else self.image_not_hover
        
        
        
        
        
