from game import config as cfg
import random
import pygame

# препятствие
def get_obstacle(next_pos):
    if len(cfg.current_obstacles) < 4:

        base_obstacle_block = [
            random.randrange(cfg.FIELD_LEFT + 4 * cfg.BLOCK, cfg.FIELD_RIGHT - 4 * cfg.BLOCK, cfg.BLOCK), 
            random.randrange(cfg.FIELD_UP + 4 * cfg.BLOCK, cfg.FIELD_DOWN - 4 * cfg.BLOCK, cfg.BLOCK)
            ]
        
        obstacles_list = [ [ [base_obstacle_block[0] - 20, base_obstacle_block[1]], base_obstacle_block ], [base_obstacle_block, [base_obstacle_block[0] +20, base_obstacle_block[1]] ],
        [base_obstacle_block, [base_obstacle_block[0] +20, base_obstacle_block[1]], [base_obstacle_block[0], base_obstacle_block[1] + 20], [base_obstacle_block[0] + 20, base_obstacle_block[1] + 20] ],
        [base_obstacle_block, [base_obstacle_block[0] +20, base_obstacle_block[1]], [base_obstacle_block[0], base_obstacle_block[1] + 20], [base_obstacle_block[0] + 20, base_obstacle_block[1] + 20], 
        [base_obstacle_block[0] + 20, base_obstacle_block[1] - 20] ], [base_obstacle_block, [base_obstacle_block[0] - 20, base_obstacle_block[1]], [base_obstacle_block[0] +20, base_obstacle_block[1]] ] ]

        figure = random.choice(obstacles_list)

        if (figure not in (cfg.snake_body and cfg.current_boost and cfg.current_food)) and next_pos not in figure:
            cfg.current_obstacles.append(figure)
    

#периодическое появление еды. не больше 4 за раз
def get_food(next_pos):
    if len(cfg.current_food) < 5:
        food_pos = [
            random.randrange(cfg.FIELD_LEFT + 2 * cfg.BLOCK, cfg.FIELD_RIGHT - 2 * cfg.BLOCK, cfg.BLOCK), 
            random.randrange(cfg.FIELD_UP + 2 * cfg.BLOCK, cfg.FIELD_DOWN - 2 * cfg.BLOCK, cfg.BLOCK)
            ]
        if food_pos not in (cfg.snake_body and cfg.current_boost and cfg.current_food and cfg.current_obstacles) and food_pos != next_pos:
            cfg.current_food.append(food_pos)

# появление еды
def boost_spawn(next_pos):
    if len(cfg.current_boost) < 2:
        boost_pos = [
            random.randrange(cfg.FIELD_LEFT + 2 * cfg.BLOCK, cfg.FIELD_RIGHT - 2 * cfg.BLOCK, cfg.BLOCK), 
            random.randrange(cfg.FIELD_UP + 2 * cfg.BLOCK, cfg.FIELD_DOWN - 2 * cfg.BLOCK, cfg.BLOCK)
        ]
        if (boost_pos not in (cfg.snake_body and cfg.current_boost and cfg.current_food and cfg.current_obstacles)) and next_pos != boost_pos : 
            cfg.current_boost.append(boost_pos)

# сетка
def draw_grid(screen):
    #горизонтальные линии. -80 - отступ
    y = cfg.upper_edge
    while y <= cfg.HEIGHT - cfg.down_edge:
        pygame.draw.line(screen, (161,206,247), (cfg.rl_edge, y), (cfg.WIDTH - cfg.rl_edge, y), 2)
        y += cfg.BLOCK

    #вертикальные
    x = cfg.rl_edge
    while x <= cfg.WIDTH - cfg.rl_edge:
        pygame.draw.line(screen, (161,206,247), (x, cfg.upper_edge), (x, cfg.HEIGHT - cfg.down_edge), 2)
        x += cfg.BLOCK