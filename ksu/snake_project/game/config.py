import pygame
import os

pygame.init()

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

def load_assets():
    global snake_game_background, bedroom_background, console_image, console_rect, food_image_apple, food_image_strawberry, food_image, obstacle_image
    
    snake_game_background = pygame.image.load(os.path.join(ASSETS_DIR, "snake_background.jpg")).convert()
    snake_game_background = pygame.transform.scale(snake_game_background, (WIDTH, HEIGHT) )

    bedroom_background = pygame.image.load(os.path.join(ASSETS_DIR, "bedroom.png")).convert()
    bedroom_background = pygame.transform.scale(bedroom_background, (1820, 980))

    console_image = pygame.image.load(os.path.join(ASSETS_DIR, "GameWatch.png")).convert_alpha()
    console_image = pygame.transform.scale(console_image, (900, 600))
    console_rect = console_image.get_rect(center = (WIDTH // 2, HEIGHT //2 ))

    food_image_apple = pygame.image.load(os.path.join(ASSETS_DIR, "apple.png")).convert_alpha()
    food_image_apple = pygame.transform.scale(food_image_apple, (BLOCK, BLOCK))

    obstacle_image = pygame.image.load(os.path.join(ASSETS_DIR, "Tile_45.png")).convert_alpha()
    obstacle_image = pygame.transform.scale(obstacle_image, (BLOCK, BLOCK))

    food_image_strawberry = pygame.image.load(os.path.join(ASSETS_DIR, "strawberry.png")).convert_alpha()
    food_image_strawberry = pygame.transform.scale(food_image_strawberry, (BLOCK, BLOCK))
    
    food_image = [food_image_apple, food_image_strawberry]

