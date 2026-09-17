import os
import pygame

pygame.init()

clock = pygame.time.Clock()

# Папка, где лежит сам скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Папка с ассетами
ASSETS_DIR = os.path.join(BASE_DIR, "..", "assets")

#ширина окна
WIDTH = 800
#высота окна
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

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

paused = False
music = True
running = False
initial_window = True
showing_game_over = False



#шрифты
font = pygame.font.Font(os.path.join(ASSETS_DIR, "pixelmplusbold.ttf"), 16)
game_over = pygame.font.Font(os.path.join(ASSETS_DIR, "pixelmplusbold.ttf"), 25)

#начальный задний фон
start_background_image = pygame.image.load(os.path.join(ASSETS_DIR, "start_background.jpg")).convert()
start_background_image = pygame.transform.scale(start_background_image, (WIDTH, HEIGHT))

#во время игры задний фон
background_image = pygame.image.load(os.path.join(ASSETS_DIR, "background.png")).convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#конечный задний фон
over_background_image = pygame.image.load(os.path.join(ASSETS_DIR, "over_background.jpg")).convert()
over_background_image = pygame.transform.scale(over_background_image, (WIDTH, HEIGHT))

#корабль
spaceship_image = pygame.image.load(os.path.join(ASSETS_DIR, "spaceship.png")).convert_alpha()
spaceship_image = pygame.transform.scale(spaceship_image, (spaceship_width, spaceship_height))

#метеорит
meteorit_image = pygame.image.load(os.path.join(ASSETS_DIR, "meteorit.png")).convert_alpha()
meteorit_image = pygame.transform.scale(meteorit_image, (meteorit_radius, meteorit_radius))

#пуля
bullet_image = pygame.image.load(os.path.join(ASSETS_DIR, "bullet.png")).convert_alpha()
bullet_image = pygame.transform.scale(bullet_image, (bullet_radius, bullet_radius))

