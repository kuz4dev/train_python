import pygame
import random

pygame.init()

clock = pygame.time.Clock()

#начальное направление 
direction = 'RIGHT'

# размеры экрана и блока
WIDTH = 1000
HEIGHT = 800
BLOCK = 20
SPEED = 10

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

#голова
snake_position = [100, 160]

#все части змейки
snake_body = [
    [100, 100],
    [80, 100]
]

# тестовая еда
food_pos = [
    random.randrange(FIELD_LEFT, FIELD_RIGHT, BLOCK),
    random.randrange(FIELD_UP, FIELD_DOWN, BLOCK)
]

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

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

#изменение направления змейки
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

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

    # постоянная перезапись головы и удаление хвоста для иллюзии движения
    snake_body.insert(0, list(snake_position))
    snake_body.pop()

    # рендер каждой части змеюки
    for one in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(one[0], one[1], BLOCK, BLOCK))

    # проверка на столкновение с границами
    if (snake_position[0] == FIELD_RIGHT and direction == "RIGHT") or (snake_position[0] == FIELD_LEFT and direction == "LEFT") or (
        snake_position[1] == FIELD_UP and direction == "UP") or (snake_position[1] == FIELD_DOWN and direction == "DOWN"):

        running = False

    # рендер тест еды
    pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect(food_pos[0], food_pos[1], BLOCK, BLOCK))

    pygame.display.flip()

    clock.tick(SPEED)

pygame.quit()


# FIXME:
# Добавить комментарии
