import pygame
import os

# размеры экрана и блока
WIDTH = 1000
HEIGHT = 800
BLOCK = 20
speed = 7

# окно конца игры
game_over = False

# окно начала
start_screen = True

#сама игра
running = False

# пауза
paused = False

#счет
score = 0

# отступы от краев экрана для сетки
rl_edge = 80
upper_edge = 100
down_edge = 80

# координаты сетки
FIELD_LEFT = rl_edge
FIELD_RIGHT = WIDTH - rl_edge
FIELD_UP = upper_edge
FIELD_DOWN = HEIGHT - down_edge

# таймеры
boost_end_time = 0
obstacle_lifetime = 0

#голова
snake_position = [100, 160]

#все части змейки
snake_body = [
    [100, 100],
    [80, 100]
]

# ускорения
SPEED_BOOST = 5
boost_start = 0

# списки сущностей
current_boost = []
current_food = []
obstacles = []
current_obstacles = []

#счет
score = 0

# папки - пути
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, '..', 'snake_assets')

snake_game_background = pygame.image.load(os.path.join(ASSETS_DIR, "snake_background.jpg")).convert()
snake_game_background = pygame.transform.scale(snake_game_background, (WIDTH, HEIGHT) )

bedroom_backgroung = pygame.image.load(os.path.join(ASSETS_DIR, "bedroom.png")).convert()
bedroom_backgroung = pygame.transform.scale(bedroom_backgroung, (WIDTH, HEIGHT))

console_image = pygame.image.load(os.path.join(ASSETS_DIR, "GameWatch.png")).convert_alpha()
console_image = pygame.transform.scale(console_image, (WIDTH - 400, HEIGHT - 250))

# #конечный задний фон
# over_background_image = pygame.image.load(os.path.join(ASSETS_DIR, "over_background.jpg")).convert()
# over_background_image = pygame.transform.scale(over_background_image, (WIDTH, HEIGHT))

# #корабль
# spaceship_image = pygame.image.load(os.path.join(ASSETS_DIR, "spaceship.png")).convert_alpha()
# spaceship_image = pygame.transform.scale(spaceship_image, (spaceship_width, spaceship_height))