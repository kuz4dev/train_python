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
        self.x = cfg.WIDTH + self.radius
        # y метеорита
        self.y = random.randint(self.radius, cfg.HEIGHT - self.radius)
    
    @property
    def rect(self):
        return pygame.Rect(self.x - self.radius // 2, self.y - self.radius // 2, self.radius, self.radius)

    def draw(self):
        cfg.screen.blit(self.image, self.rect)
        
    def move(self):
        self.x -= self.speed

