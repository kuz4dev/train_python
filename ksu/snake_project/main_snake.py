import pygame
import os

from game import config as cfg
from screens import (
    show_start,
    show_end,
    game_cycle,
)

pygame.init()

#ивент на время для еды
food_event = pygame.USEREVENT +1 
pygame.time.set_timer(food_event, 2500)

boost_event = pygame.USEREVENT +2 
pygame.time.set_timer(boost_event, 45000)

obstacle_event = pygame.USEREVENT + 3
pygame.time.set_timer(obstacle_event, 25000)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))

pygame.display.set_caption("Змейка")

cfg.load_assets()

score_font = pygame.font.Font(os.path.join(cfg.ASSETS_DIR, 'DigitalNumbers-Regular.ttf'), 30)

pause_font = pygame.font.Font(os.path.join(cfg.ASSETS_DIR, 'en-us.ttf'), 18)

show_start(screen, pause_font, clock)

game_cycle(screen, score_font, pause_font, clock, food_event, boost_event, obstacle_event)
                
show_end(screen, pause_font, clock)

pygame.quit()


# звук при паузе, геймовере, кратком столкновении со стеной

# картинки и змейку градиентную если получится

# TODO: вынести подгрузку ассетов в конфиг, также туда вынести scree и clock