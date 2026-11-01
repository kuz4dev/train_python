from game import config as cfg

def reset_game():
    cfg.score = 0
    cfg.speed = 7

    # таймеры
    cfg.boost_end_time = 0
    cfg.obstacle_lifetime = 0

    #голова
    cfg.snake_position = [100, 160]

    #все части змейки
    cfg.snake_body = [
        [100, 100],
        [80, 100]
    ]

    cfg.boost_start = 0

    # списки сущностей
    cfg.current_boost = []
    cfg.current_food = []
    cfg.obstacles = []
    cfg.current_obstacles = []