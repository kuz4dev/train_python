import os

# папки - пути
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR_IMG = os.path.join(BASE_DIR, 'assets', 'images')
ASSETS_DIR_SOUNDS = os.path.join(BASE_DIR, 'assets', 'sounds')

# размеры окна
WIDTH = 800
HEIGHT = 600

# параметры волка
wolf_width = 100
wolf_height = 150
wolf_x = WIDTH // 2 - wolf_width // 2
wolf_y = HEIGHT - wolf_height - 30
wolf_speed = 7

# параметры яиц
egg_x = WIDTH // 2
egg_y = 50
egg_radius = 15
egg_speed = 5

# яйца на экране
eggs = []

# таймер спауна яиц
spawn_timer = 0

# Интервал между появлением яиц в миллисекундах
spawn_interval = 60

# жизни и очки
score = 0
lives = 3

# усложнение игры
speedup_timer = 0
speedup_interval = 300
speedup_amount = 0.5

# цветовая схема
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# параметры корзины
basket_width = 60
basket_height = 20