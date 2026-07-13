import pygame
import random

pygame.init()

clock = pygame.time.Clock()

direction = 'RIGHT'

WIDTH = 1000
HEIGHT = 800
BLOCK = 20
rl_edge = 80
upper_edge = 100
down_edge = 80


screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Змейка")

snake_position = [100, 60]

snake_body = [
    [100, 60],
    [80, 60]
              ]

food_pos = [random.randrange(0, WIDTH // BLOCK) * BLOCK,
            random.randrange(0, WIDTH // BLOCK) * BLOCK
            ]

def draw_grid():
    #горизонтальные линии. -80 - отступ
    y = upper_edge
    while y <= HEIGHT - down_edge:
        pygame.draw.line(screen, (240,235,249), (rl_edge, y), (WIDTH - rl_edge, y), 2)
        y += BLOCK

    

    


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

    draw_grid()

    snake_body.insert(0, list(snake_position))
    snake_body.pop()

    for one in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(one[0], one[1], BLOCK, BLOCK))

    pygame.draw.rect(screen, (255, 255, 255) , pygame.Rect(food_pos[0], food_pos[1], BLOCK, BLOCK))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
