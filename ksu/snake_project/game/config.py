# размеры экрана и блока
WIDTH = 1000
HEIGHT = 800
BLOCK = 20
speed = 7

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

