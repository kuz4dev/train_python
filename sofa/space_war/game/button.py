import pygame
import os

from configuration import config as cfg

class Button():
    def __init__(self, text):
        self.width = cfg.button_width
        self.height = cfg.button_height
        self.x = cfg.button_x
        self.y = cfg.button_y
        self.font = cfg.font
        self.text = text
        self.text_color = (255, 255, 255)


    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(cfg.screen, (37, 10, 20), self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        cfg.screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos))
 