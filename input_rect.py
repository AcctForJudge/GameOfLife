import pygame, re

pygame.init()
COLOUR_INACTIVE = pygame.Color('lightskyblue3')
COLOUR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 30)

class InputRect:
    def __init__(self, x, y, w, h, text = ''):
        self.rect = pygame.Rect(x,y,w,h)
        self.text = text
        self.colour = COLOUR_INACTIVE
        self.text_surface = FONT.render(text, True, "Black")
        self.active = False
        
    def handle_event(self, event, i = False):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current colour of the input box.
            self.colour = COLOUR_ACTIVE if self.active else COLOUR_INACTIVE
            
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if not i:
                        if (event.unicode.isdigit() or event.unicode == '.') and len(self.text) < 5:
                            self.text += event.unicode
                            if not re.search(r"^(0(\.\d*)?|1(\.0*)?|)$", self.text):
                                self.text = self.text[:-1]
                    else:
                        if event.unicode.isdigit():
                            val = self.text + event.unicode
                            if 1 <= int(val) <= 99 or val == '':
                                self.text += event.unicode
                                  
                            
                # Re-render the text.
                self.text_surface = FONT.render(self.text, True, self.colour)     
                   
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.text_surface, (self.rect.x + 10, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.colour, self.rect, 2)
        
    def get_text(self, i= False):
        return int(self.text) if i else float(self.text)