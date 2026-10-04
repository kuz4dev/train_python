import pygame
import os

from configuration import config as cfg

class Button():
    def __init__(self):
        self.width = cfg.button_width
        self.height = cfg.button_height
        self.x = cfg.button_x
        self.y = cfg.button_y
        self.font = pygame.font.Font(os.path.join(ASSETS_DIR, "pixelmplusbold.ttf"), 16)
        self.text_color = (255, 255, 255)


    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect((100, 255, 222), (self.x, self.y, self.width, self.height))

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
            return False

 