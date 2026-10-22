import pygame
import os

pygame.init()
pygame.mixer.init()

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
RECORD_DIR = os.path.join(BASE_DIR, '..', 'files', 'record.json')

def load_assets():
    global snake_game_background, bedroom_background, console_image, console_rect, food_image_apple, food_image_strawberry, food_image, obstacle_image, bedroom_rect, boost_image
    
    snake_game_background = pygame.image.load(os.path.join(ASSETS_DIR, "back.jpg")).convert()
    snake_game_background = pygame.transform.scale(snake_game_background, (WIDTH, HEIGHT) )

    bedroom_background = pygame.image.load(os.path.join(ASSETS_DIR, "bedroom.png")).convert()
    bedroom_background = pygame.transform.scale(bedroom_background, (1820, 980))
    bedroom_rect = bedroom_background.get_rect(center = (WIDTH // 2, HEIGHT //2 ))

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

    boost_image = pygame.image.load(os.path.join(ASSETS_DIR, "Arrow_1.png")).convert_alpha()
    boost_image = pygame.transform.scale(boost_image, (BLOCK, BLOCK))

def load_sound():
    global game_cycle_soundtrack, sft_eat, sft_collision, sft_buff, paused_soundtrack

    game_cycle_soundtrack = pygame.mixer.music.load(os.path.join(ASSETS_DIR, "sound", "ZZZ-Camillia-Golden-Week-OST_-Ambient-V2-_Zenless-Zone-Zero_.mp3"))


    paused_soundtrack = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "sound", "TINY_TECH_WHIZ_Norma_Marcel_Remix___Version_2_7_BGM___Zenless_ZZZ.mp3"))
    sft_eat = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "sound", "pepSound2.mp3"))
    sft_collision = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "sound", "pepSound4.mp3"))
    sft_buff = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "sound", "pepSound1.mp3"))


