import pygame
import math

class Button():
    def __init__(self, center, radius, color=(68,116,193)):
            self.color = color
            self.center = center
            self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and math.dist(event.pos, self.center) <= self.radius)