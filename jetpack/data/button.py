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
        if style == 'quit':
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


