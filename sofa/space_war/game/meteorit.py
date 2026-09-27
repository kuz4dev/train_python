from configuration import config as cfg
import pygame
import random

class Meteorit:
    def __init__(self):
        #радиус метеорита
        self.radius = cfg.meteorit_radius
        #скорость метеорита
        self.speed = cfg.meteorit_speed
        #картинка
        self.image = cfg.meteorit_image
        # x метеорита
        self.x = cfg.meteorit_x - self.radius
        # y метеорита
        self.y = random.randint(100, 600)
    
    @property
    def rect(self):
        return self.image.get_rect(center = (self.x, self.y))
    
    def draw(self):
        cfg.screen.blit(self.image, (self.x - self.radius, self.y - self.radius))
        
    def move(self):
        self.x -= self.speed

