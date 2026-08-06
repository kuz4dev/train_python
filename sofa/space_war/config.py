import os
import pygame

pygame.init()

clock = pygame.time.Clock()

# Папка, где лежит сам скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Папка с ассетами
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

#ширина окна
WIDTH = 800
#высота окна
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
#название игры
pygame.display.set_caption("Леталки!")


#широта корабля
confines_width = 800
#высота корабля
confines_height = 500
#широта положения корабля
confines_x = WIDTH
#высота положения корабля
confines_y = HEIGHT // 2

#широта корабля
spaceship_width = 110
#высота корабля
spaceship_height = 100
#широта положения корабля
spaceship_x = WIDTH - 790
#высота положения корабля
spaceship_y = HEIGHT - spaceship_height - 30
#скорость корабля
spaceship_speed = 8

#широта метеорита
meteorit_x = WIDTH - 30
#высота метеорита
meteorit_y = HEIGHT
#радиус метеорита
meteorit_radius = 15 * 4
#скорость метеорита
meteorit_speed = 5

#радиус снаряда
bullet_radius = 25
#скорость снаряда
bullet_speed = 7

bullets = []
meteorits = []
spawn_timer = 0
# Интервал между появлением метеоритов в миллисекундах
spawn_interval = 80  

#cчет
score = 0
#жизни
lives = 3

font_path = pygame.font.Font(os.path.join(ASSETS_DIR,"pixelmplusbold.ttf"), 15)

paused = False
music = True
running = False
initial_window = True