from .constants import *

class Button():
    def __init__(self, rect, image):
        self.rect = rect
        self.image = image
        self.pressed = False
        

    
    def draw_button(self, screen):
        active = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                active = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return active




