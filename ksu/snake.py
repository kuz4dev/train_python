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

# -> font.font script b/ Climate Crisis/ impact
pause_font = pygame.font.SysFont(None, 60)

#голова
snake_position = [100, 160]

#все части змейки
snake_body = [
    [100, 100],
    [80, 100]
]
food_event = pygame.USEREVENT +1 
pygame.time.set_timer(food_event, 5000)
current_food = []

#периодическое появление еды
def get_food():
    if len(current_food) < 4:
        food_pos = [
            random.randrange(FIELD_LEFT, FIELD_RIGHT, BLOCK), 
            random.randrange(FIELD_UP, FIELD_DOWN, BLOCK)
            ]
        current_food.append(food_pos)

# тестовая еда
# food_pos = [
#     random.randrange(FIELD_LEFT, FIELD_RIGHT, BLOCK),
#     random.randrange(FIELD_UP, FIELD_DOWN, BLOCK)
# ]

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

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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

                if event.type == pygame.USEREVENT:
                    get_food()


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

        # постоянная перезапись головы и удаление хвоста для иллюзии движения
        snake_body.insert(0, list(snake_position))

        # for food in current_food:
        #     if food[0] == snake_position[0] and food[1] == snake_position[1]:
        #         current_food.remove(food)
                
        #     else:
        snake_body.pop()

        # рендер каждой части змеюки
        for one in snake_body:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(one[0], one[1], BLOCK, BLOCK))

        # проверка на столкновение с границами
        if (snake_position[0] == FIELD_RIGHT - BLOCK and direction == "RIGHT") or (snake_position[0] == FIELD_LEFT and direction == "LEFT") or (
            snake_position[1] == FIELD_UP and direction == "UP") or (snake_position[1] == FIELD_DOWN - BLOCK and direction == "DOWN"):

            running = False

        for piece in current_food:
            pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect(current_food[0], current_food[1], BLOCK, BLOCK))

        # # рендер тест еды
        # pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect(food_pos[0], food_pos[1], BLOCK, BLOCK))

    if paused:
        # -text
        paused_text = pause_font.render("Пауза!", True, (82,87,91))
        pause_rect = paused_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(paused_text, pause_rect)

    pygame.display.flip()

    clock.tick(SPEED)

pygame.quit()

