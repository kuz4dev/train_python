import pygame
import random
import os

pygame.init()

clock = pygame.time.Clock()

#счет
score = 0

#начальное направление 
direction = 'RIGHT'

# папки - пути
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'snake_assets')

# размеры экрана и блока
WIDTH = 1000
HEIGHT = 800
BLOCK = 20
speed = 7

# отступы от краев экрана для сетки
rl_edge = 80
upper_edge = 100
down_edge = 80

# координаты сетки
FIELD_LEFT = rl_edge
FIELD_RIGHT = WIDTH - rl_edge
FIELD_UP = upper_edge
FIELD_DOWN = HEIGHT - down_edge

boost_end_time = 0
obstacle_lifetime = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Змейка")

score_font = pygame.font.Font(os.path.join(ASSETS_DIR, 'DigitalNumbers-Regular.ttf'), 30)

pause_font = pygame.font.Font(os.path.join(ASSETS_DIR, 'en-us.ttf'), 25)

#голова
snake_position = [100, 160]

#все части змейки
snake_body = [
    [100, 100],
    [80, 100]
]

#ивент на время для еды
food_event = pygame.USEREVENT +1 
pygame.time.set_timer(food_event, 2500)
current_food = []

SPEED_BOOST = 5
boost_start = 0

boost_event = pygame.USEREVENT +2 
pygame.time.set_timer(boost_event, 45000)
current_boost = []

obstacles = []
current_obstacles = []

obstacle_event = pygame.USEREVENT + 3
pygame.time.set_timer(obstacle_event, 25000)

# препятствие
def get_obstacle():
    if len(current_obstacles) < 4:

        base_obstacle_block = [
            random.randrange(FIELD_LEFT + 4 * BLOCK, FIELD_RIGHT - 4 * BLOCK, BLOCK), 
            random.randrange(FIELD_UP + 4 * BLOCK, FIELD_DOWN - 4 * BLOCK, BLOCK)
            ]
        
        obstacles_list = [ [ [base_obstacle_block[0] - 20, base_obstacle_block[1]], base_obstacle_block ], [base_obstacle_block, [base_obstacle_block[0] +20, base_obstacle_block[1]] ],
        [base_obstacle_block, [base_obstacle_block[0] +20, base_obstacle_block[1]], [base_obstacle_block[0], base_obstacle_block[1] + 20], [base_obstacle_block[0] + 20, base_obstacle_block[1] + 20] ],
        [base_obstacle_block, [base_obstacle_block[0] +20, base_obstacle_block[1]], [base_obstacle_block[0], base_obstacle_block[1] + 20], [base_obstacle_block[0] + 20, base_obstacle_block[1] + 20], 
        [base_obstacle_block[0] + 20, base_obstacle_block[1] - 20] ], [base_obstacle_block, [base_obstacle_block[0] - 20, base_obstacle_block[1]], [base_obstacle_block[0] +20, base_obstacle_block[1]] ] ]

        figure = random.choice(obstacles_list)

        if (figure not in (snake_body and current_boost and current_food)) and next_pos not in figure:
            current_obstacles.append(figure)
    

#периодическое появление еды. не больше 4 за раз
def get_food():
    if len(current_food) < 5:
        food_pos = [
            random.randrange(FIELD_LEFT + 2 * BLOCK, FIELD_RIGHT - 2 * BLOCK, BLOCK), 
            random.randrange(FIELD_UP + 2 * BLOCK, FIELD_DOWN - 2 * BLOCK, BLOCK)
            ]
        if food_pos not in (snake_body and current_boost and current_food and current_obstacles) and food_pos != next_pos:
            current_food.append(food_pos)

# появление еды
def boost_spawn():
    if len(current_boost) < 2:
        boost_pos = [
            random.randrange(FIELD_LEFT + 2 * BLOCK, FIELD_RIGHT - 2 * BLOCK, BLOCK), 
            random.randrange(FIELD_UP + 2 * BLOCK, FIELD_DOWN - 2 * BLOCK, BLOCK)
        ]
        if (boost_pos not in (snake_body and current_boost and current_food and current_obstacles)) and next_pos != boost_pos : 
            current_boost.append(boost_pos)


# сетка
def draw_grid():
    #горизонтальные линии. -80 - отступ
    y = upper_edge
    while y <= HEIGHT - down_edge:
        pygame.draw.line(screen, (161,206,247), (rl_edge, y), (WIDTH - rl_edge, y), 2)
        y += BLOCK

    #вертикальные
    x = rl_edge
    while x <= WIDTH - rl_edge:
        pygame.draw.line(screen, (161,206,247), (x, upper_edge), (x, HEIGHT - down_edge), 2)
        x += BLOCK

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
    opening_text_rect = opening_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(opening_text, opening_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_screen = False
                running = True

    pygame.display.flip()
    
    clock.tick(speed)


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
            obstacle_lifetime = pygame.time.get_ticks() + 20000

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
        

            if not paused:

            #изменение направления змейки
                if event.key == pygame.K_w and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_s and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_a and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_d and direction != 'LEFT':
                    direction = 'RIGHT'

    if not paused:
        # движение
        if direction == 'UP':
            snake_position[1] -= BLOCK

        elif direction == 'DOWN':
            snake_position[1] += BLOCK

        elif direction == 'LEFT':
            snake_position[0] -= BLOCK

        elif direction == 'RIGHT':
            snake_position[0] += BLOCK

        if direction == 'UP':
            next_pos = [snake_position[0], snake_position[1] - BLOCK]
        elif direction == 'DOWN':
            next_pos = [snake_position[0], snake_position[1] + BLOCK]
        elif direction == 'LEFT':
            next_pos = [snake_position[0] - BLOCK, snake_position[1]]
        elif direction == 'RIGHT':
            next_pos = [snake_position[0] + BLOCK, snake_position[1]]
            
               
        if boost_end_time and pygame.time.get_ticks() >= boost_end_time:
            speed -= SPEED_BOOST
            boost_end_time = 0

        if (obstacle_lifetime and pygame.time.get_ticks() >= obstacle_lifetime) and len(current_obstacles) == 4:
            print("функция заработала")
            current_obstacles.pop(0)
            obstacle_lifetime = 0

        screen.fill((161,241,247))

        # сетка
        draw_grid()

        ingame_score = score_font.render(f"SCORE: {str(score).zfill(15)}", True, (82,87,91))
        ingame_score_rect = ingame_score.get_rect(center = (WIDTH // 2, 50))
        screen.blit(ingame_score, ingame_score_rect)

        # постоянная перезапись головы и удаление хвоста для иллюзии движения
        snake_body.insert(0, list(snake_position))

        ate = False

        #проверка на столкновение с едой
        for food in current_food:
            if food == snake_position:
                current_food.remove(food)
                ate = True
                score += 5000
                break
        
        #удаление хвоста
        if not ate:
            snake_body.pop()

        # рендер каждой части змеюки
        for one in snake_body:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(one[0], one[1], BLOCK, BLOCK))

        #рендер еды
        for piece in current_food:
            pygame.draw.rect(screen, (174,139,253) , pygame.Rect(piece[0], piece[1], BLOCK, BLOCK))

        for boost in current_boost:
            pygame.draw.rect(screen, (172,253,139) , pygame.Rect(boost[0], boost[1], BLOCK, BLOCK))

        for obs in current_obstacles:
            for block in obs:
                pygame.draw.rect(screen, (32,62,15), pygame.Rect(block[0], block[1], BLOCK, BLOCK))

        for obs in current_obstacles:
            for block in obs:
                if next_pos == block:
                    game_over = True
                    running = False

        # проверка на столкновение с границами
        if (snake_position[0] == FIELD_RIGHT - BLOCK and direction == "RIGHT") or (snake_position[0] == FIELD_LEFT and direction == "LEFT") or (
            snake_position[1] == FIELD_UP and direction == "UP") or (snake_position[1] == FIELD_DOWN - BLOCK and direction == "DOWN"):

            #sound

            # crash_time = pygame.USEREVENT +2
            # pygame.time.set_timer(crash_time, 2500)
            # if event.type == crash_time:
            
            game_over = True
            running = False

        # врезание змейки в себя
        if snake_position in snake_body[1:]:
            game_over = True
            running = False

        # врезание в змейку и ускорение-возвращение
        for boost in current_boost:
            if boost == snake_position:
                current_boost.remove(boost)
                speed += SPEED_BOOST

                boost_end_time = pygame.time.get_ticks() + 10000
                break
            


    #окно паузы
    if paused:
        # -text
        paused_text = pause_font.render("Пауза!", True, (82,87,91))
        pause_rect = paused_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(paused_text, pause_rect)

    pygame.display.flip()

    clock.tick(speed)


# окно конца игры
while game_over:

    screen.fill((161,241,247))

    go_show_score = pause_font.render(f"Игра закончена! Ваш счет: {score}", True, (82,87,91))
    go_score_rect = go_show_score.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(go_show_score, go_score_rect)

    exit_go_text = pause_font.render("Нажмите X для выхода", True, (82,87,91))
    go_exit_rect = exit_go_text.get_rect(center = (WIDTH // 2, HEIGHT - 50) )
    screen.blit(exit_go_text, go_exit_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_over = False
                

    pygame.display.flip()
    
    clock.tick(speed)

pygame.quit()

# todo:
# таймер на удаление препятствий и проверка на столкновение с ними

# музыка базовая, ускорение
# шрифт из файла
# звук при паузе, геймовере, кратком столкновении со стеной

# картинки и змейку градиентную если получится