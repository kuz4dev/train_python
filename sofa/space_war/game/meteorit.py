from configuration import config as cfg
import pygame
import random

class Meteorit:
    def __init__(self):
        #радиус метеорита
        self.radius = cfg.meteorit_radius
        #скорость метеорита
        self.speed = random.randint(3, 7)
        #картинка
        self.image = cfg.meteorit_image
        # x метеорита
        self.x = cfg.WIDTH + self.radius
        # y метеорита
        self.y = random.randint(self.radius + cfg.header_image_size + 2 * cfg.header_indent, cfg.HEIGHT - self.radius)
        # угол поворота метеорита   
        self.angle = random.randint(0, 360)
        # скорость вращения метеорита и выбор направления вращения
        self.rotation_speed = random.choice([-1, 1]) * self.speed
    
    @property
    def rect(self):
        return pygame.Rect(self.x - self.radius // 2, self.y - self.radius // 2, self.radius, self.radius)

    def draw(self):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated.get_rect(center=(self.x, self.y))
        cfg.screen.blit(rotated, rotated_rect)
        
    def move(self):
        self.x -= self.speed
        self.angle = (self.angle + self.rotation_speed) % 360
        
