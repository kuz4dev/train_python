import pygame
import random
import os
import config as cfg

pygame.init()

clock = pygame.time.Clock()

#счет
score = 0

# папки - пути
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'snake_assets')

screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))

pygame.display.set_caption("Змейка")

score_font = pygame.font.Font(os.path.join(ASSETS_DIR, 'DigitalNumbers-Regular.ttf'), 30)

pause_font = pygame.font.Font(os.path.join(ASSETS_DIR, 'en-us.ttf'), 25)

#ивент на время для еды
food_event = pygame.USEREVENT +1 
pygame.time.set_timer(food_event, 2500)

boost_event = pygame.USEREVENT +2 
pygame.time.set_timer(boost_event, 45000)

obstacle_event = pygame.USEREVENT + 3
pygame.time.set_timer(obstacle_event, 25000)

# препятствие
def get_obstacle():
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
def get_food():
    if len(cfg.current_food) < 5:
        food_pos = [
            random.randrange(cfg.FIELD_LEFT + 2 * cfg.BLOCK, cfg.FIELD_RIGHT - 2 * cfg.BLOCK, cfg.BLOCK), 
            random.randrange(cfg.FIELD_UP + 2 * cfg.BLOCK, cfg.FIELD_DOWN - 2 * cfg.BLOCK, cfg.BLOCK)
            ]
        if food_pos not in (cfg.snake_body and cfg.current_boost and cfg.current_food and cfg.current_obstacles) and food_pos != next_pos:
            cfg.current_food.append(food_pos)

# появление еды
def boost_spawn():
    if len(cfg.current_boost) < 2:
        boost_pos = [
            random.randrange(cfg.FIELD_LEFT + 2 * cfg.BLOCK, cfg.FIELD_RIGHT - 2 * cfg.BLOCK, cfg.BLOCK), 
            random.randrange(cfg.FIELD_UP + 2 * cfg.BLOCK, cfg.FIELD_DOWN - 2 * cfg.BLOCK, cfg.BLOCK)
        ]
        if (boost_pos not in (cfg.snake_body and cfg.current_boost and cfg.current_food and cfg.current_obstacles)) and next_pos != boost_pos : 
            cfg.current_boost.append(boost_pos)


# сетка
def draw_grid():
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

#сама игра
running = False

# пауза
paused = False

# окно конца игры
game_over = False

# окно начала
start_screen = True


while start_screen:
    screen.fill((161,241,247))
    
    opening_text = pause_font.render(f"Нажмите пробел для начала игры", True, (82,87,91))
    opening_text_rect = opening_text.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2))
    screen.blit(opening_text, opening_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_screen = False
                running = True

    pygame.display.flip()
    
    clock.tick(cfg.speed)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == food_event and not paused:
            get_food() 

        if event.type == boost_event and not paused:
            boost_spawn()

        if event.type == obstacle_event and not paused:
            get_obstacle()
            cfg.obstacle_lifetime = pygame.time.get_ticks() + 20000

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
        

            if not paused:

            #изменение направления змейки
                if event.key == pygame.K_w and cfg.direction != 'DOWN':
                    cfg.direction = 'UP'
                elif event.key == pygame.K_s and cfg.direction != 'UP':
                    cfg.direction = 'DOWN'
                elif event.key == pygame.K_a and cfg.direction != 'RIGHT':
                    cfg.direction = 'LEFT'
                elif event.key == pygame.K_d and cfg.direction != 'LEFT':
                    cfg.direction = 'RIGHT'

    if not paused:
        # движение
        if cfg.direction == 'UP':
            cfg.snake_position[1] -= cfg.BLOCK

        elif cfg.direction == 'DOWN':
            cfg.snake_position[1] += cfg.BLOCK

        elif cfg.direction == 'LEFT':
            cfg.snake_position[0] -= cfg.BLOCK

        elif cfg.direction == 'RIGHT':
            cfg.snake_position[0] += cfg.BLOCK

        if cfg.direction == 'UP':
            next_pos = [cfg.snake_position[0], cfg.snake_position[1] - cfg.BLOCK]
        elif cfg.direction == 'DOWN':
            next_pos = [cfg.snake_position[0], cfg.snake_position[1] + cfg.BLOCK]
        elif cfg.direction == 'LEFT':
            next_pos = [cfg.snake_position[0] - cfg.BLOCK, cfg.snake_position[1]]
        elif cfg.direction == 'RIGHT':
            next_pos = [cfg.snake_position[0] + cfg.BLOCK, cfg.snake_position[1]]
            
               
        if cfg.boost_end_time and pygame.time.get_ticks() >= cfg.boost_end_time:
            cfg.speed -= cfg.SPEED_BOOST
            cfg.boost_end_time = 0

        if (cfg.obstacle_lifetime and pygame.time.get_ticks() >= cfg.obstacle_lifetime) and len(cfg.current_obstacles) == 4:
            print("функция заработала")
            cfg.current_obstacles.pop(0)
            cfg.obstacle_lifetime = 0

        screen.fill((161,241,247))

        # сетка
        draw_grid()

        ingame_score = score_font.render(f"SCORE: {str(score).zfill(15)}", True, (82,87,91))
        ingame_score_rect = ingame_score.get_rect(center = (cfg.WIDTH // 2, 50))
        screen.blit(ingame_score, ingame_score_rect)

        # постоянная перезапись головы и удаление хвоста для иллюзии движения
        cfg.snake_body.insert(0, list(cfg.snake_position))

        ate = False

        #проверка на столкновение с едой
        for food in cfg.current_food:
            if food == cfg.snake_position:
                cfg.current_food.remove(food)
                ate = True
                score += 5000
                break
        
        #удаление хвоста
        if not ate:
            cfg.snake_body.pop()

        # рендер каждой части змеюки
        for one in cfg.snake_body:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(one[0], one[1], cfg.BLOCK, cfg.BLOCK))

        #рендер еды
        for piece in cfg.current_food:
            pygame.draw.rect(screen, (174,139,253) , pygame.Rect(piece[0], piece[1], cfg.BLOCK, cfg.BLOCK))

        for boost in cfg.current_boost:
            pygame.draw.rect(screen, (172,253,139) , pygame.Rect(boost[0], boost[1], cfg.BLOCK, cfg.BLOCK))

        for obs in cfg.current_obstacles:
            for block in obs:
                pygame.draw.rect(screen, (32,62,15), pygame.Rect(block[0], block[1], cfg.BLOCK, cfg.BLOCK))

        for obs in cfg.current_obstacles:
            for block in obs:
                if next_pos == block:
                    game_over = True
                    running = False

        # проверка на столкновение с границами
        if (cfg.snake_position[0] == cfg.FIELD_RIGHT - cfg.BLOCK and cfg.direction == "RIGHT") or (cfg.snake_position[0] == cfg.FIELD_LEFT and cfg.direction == "LEFT") or (
            cfg.snake_position[1] == cfg.FIELD_UP and cfg.direction == "UP") or (cfg.snake_position[1] == cfg.FIELD_DOWN - cfg.BLOCK and cfg.direction == "DOWN"):

            #sound

            # crash_time = pygame.USEREVENT +2
            # pygame.time.set_timer(crash_time, 2500)
            # if event.type == crash_time:
            
            game_over = True
            running = False

        # врезание змейки в себя
        if cfg.snake_position in cfg.snake_body[1:]:
            game_over = True
            running = False

        # врезание в змейку и ускорение-возвращение
        for boost in cfg.current_boost:
            if boost == cfg.snake_position:
                cfg.current_boost.remove(boost)
                cfg.speed += cfg.SPEED_BOOST

                cfg.boost_end_time = pygame.time.get_ticks() + 10000
                break
            


    #окно паузы
    if paused:
        # -text
        paused_text = pause_font.render("Пауза!", True, (82,87,91))
        pause_rect = paused_text.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2))
        screen.blit(paused_text, pause_rect)

    pygame.display.flip()

    clock.tick(cfg.speed)


# окно конца игры
while game_over:

    screen.fill((161,241,247))

    go_show_score = pause_font.render(f"Игра закончена! Ваш счет: {score}", True, (82,87,91))
    go_score_rect = go_show_score.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2))
    screen.blit(go_show_score, go_score_rect)

    exit_go_text = pause_font.render("Нажмите X для выхода", True, (82,87,91))
    go_exit_rect = exit_go_text.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT - 50) )
    screen.blit(exit_go_text, go_exit_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_over = False
                

    pygame.display.flip()
    
    clock.tick(cfg.speed)

pygame.quit()

# todo:

# музыка базовая, ускорение
# шрифт из файла
# звук при паузе, геймовере, кратком столкновении со стеной

# картинки и змейку градиентную если получится