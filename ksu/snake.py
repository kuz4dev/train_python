import pygame
import random

pygame.init()

clock = pygame.time.Clock()

#счет
score = 0

#начальное направление 
direction = 'RIGHT'

# размеры экрана и блока
WIDTH = 1000
HEIGHT = 800
BLOCK = 20
SPEED = 7

# отступы от краев экрана для сетки
rl_edge = 80
upper_edge = 100
down_edge = 80

# координаты сетки
FIELD_LEFT = rl_edge
FIELD_RIGHT = WIDTH - rl_edge
FIELD_UP = upper_edge
FIELD_DOWN = HEIGHT - down_edge

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Змейка")

# -> font.font script b/ Climate Crisis/ impact
pause_font = pygame.font.SysFont(None, 40)

#голова
snake_position = [100, 160]

#все части змейки
snake_body = [
    [100, 100],
    [80, 100]
]

obstacles = [
    
]

#ивент на время для еды
food_event = pygame.USEREVENT +1 
pygame.time.set_timer(food_event, 4000)
current_food = []

#периодическое появление еды. не больше 4 за раз
def get_food():
    if len(current_food) < 5:
        food_pos = [
            random.randrange(FIELD_LEFT + 2 * BLOCK, FIELD_RIGHT - 2 * BLOCK, BLOCK), 
            random.randrange(FIELD_UP + 2 * BLOCK, FIELD_DOWN - 2 * BLOCK, BLOCK)
            ]
        if food_pos not in current_food:
            current_food.append(food_pos)

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


running = True

# пауза
paused = False

game_over = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == food_event and not paused:
            get_food() 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
        

            if not paused:

            #изменение направления змейки
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
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
            
        

        screen.fill((161,241,247))

        # сетка
        draw_grid()

        ingame_score = pause_font.render(f"SCORE: {score}", True, (82,87,91))
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
            

        #рендер еды
        for piece in current_food:
            pygame.draw.rect(screen, (174,139,253) , pygame.Rect(piece[0], piece[1], BLOCK, BLOCK))

    #окно паузы
    if paused:
        # -text
        paused_text = pause_font.render("Пауза!", True, (82,87,91))
        pause_rect = paused_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(paused_text, pause_rect)

    pygame.display.flip()

    clock.tick(SPEED)

while game_over:

    screen.fill((161,241,247))

    go_show_score = pause_font.render(f"Игра закончена! Ваш счет: {score}", True, (82,87,91))
    go_score_rect = go_show_score.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(go_show_score, go_score_rect)

    exit_go_text = pause_font.render("Нажмите X для выхода", True, (82,87,91))
    go_exit_rect = exit_go_text.get_rect(center = (WIDTH // 2, HEIGHT - 50) )
    screen.blit(exit_go_text, go_exit_rect)

    # game_over_text = pause_font.render(f"Игра закончена! Ваш счет: {score} \n Нажмите X для выхода", True, (82,87,91) )

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_over = False

    pygame.display.flip()
    
    clock.tick(SPEED)

pygame.quit()

# todo:
# подсчет очков +
# окно геймовера +
# препятствия
# мб ускорение на j с потерей длины если лень не будет

# музыка базовая, ускорение
# шрифт из файла
# звук при паузе, геймовере, кратком столкновении со стеной

# картинки и змейку градиентную если получится