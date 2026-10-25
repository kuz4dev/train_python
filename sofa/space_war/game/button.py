import pygame
import os

from configuration import config as cfg

class Button():
    def __init__(self, text, y = cfg.button_y, x = cfg.button_x, text_color=(255, 255, 255), indent = 20):
        self.font = cfg.font
        self.text = text
        self.text_color = text_color
        
        text_width, text_height = self.font.size(text)
        self.width = max(cfg.button_width, text_width + indent)
        self.height = max(cfg.button_height, text_height + indent)
        self.x = x
        self.y = y
        
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, color=(37, 10, 20)):
        pygame.draw.rect(cfg.screen, color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        cfg.screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos))
 