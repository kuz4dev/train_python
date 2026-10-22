import pygame
from configuration import config as cfg

class Header:
    def __init__(self, text_color=(255, 255, 255)):
        # размер изображений жизней и очков
        self.image_size = cfg.header_image_size
        # отступ от края экрана для жизней и очков
        self.indent = cfg.header_indent
        #изображение корабля (жизни)
        self.live_image = pygame.transform.scale(cfg.spaceship_image, (self.image_size, self.image_size))
        self.live_image = pygame.transform.rotate(self.live_image, 90)
        #изображение метеорита (счет)
        self.score_image = pygame.transform.scale(cfg.meteorit_image, (self.image_size, self.image_size))
        #цвет текста
        self.text_color = text_color


    def draw(self, lives, score):
        self.draw_lives(lives)
        self.draw_score(score)

    def draw_lives(self, lives): #корабли
        for i in range(lives):
            x = cfg.WIDTH - self.indent - self.image_size - i * (self.image_size + self.indent)
            cfg.screen.blit(self.live_image, (x, self.indent))
        

    def draw_score(self, score):
        #изображение
        cfg.screen.blit(self.score_image, (self.indent, self.indent))
                
        #текст
        score_text = cfg.font.render(f"X {score}", True, self.text_color)
        score_rect = score_text.get_rect(midleft = (self.indent + self.image_size + 10, self.indent + self.image_size // 2))
        cfg.screen.blit(score_text, score_rect)
