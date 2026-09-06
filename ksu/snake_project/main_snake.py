import pygame
import os

from game import config as cfg
from game import (
    get_obstacle,
    get_food,
    boost_spawn,
    draw_grid,
    Snake,
)
from screens import (
    show_start,
)

pygame.init()

clock = pygame.time.Clock()

snake = Snake()

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


show_start(screen, pause_font, clock)


while cfg.running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cfg.running = False 

        if event.type == food_event and not cfg.paused:
            get_food(next_pos) 

        if event.type == boost_event and not cfg.paused:
            boost_spawn(next_pos)

        if event.type == obstacle_event and not cfg.paused:
            get_obstacle(next_pos)
            cfg.obstacle_lifetime = pygame.time.get_ticks() + 20000

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                cfg.paused = not cfg.paused
        

            if not cfg.paused:

                #изменение направления змейки
                if event.key == pygame.K_w:
                    snake.change_direction('UP')
                elif event.key == pygame.K_s:
                    snake.change_direction('DOWN')
                elif event.key == pygame.K_a:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_d:
                    snake.change_direction('RIGHT')

                # следующая позиция змейки
                if snake.direction == 'UP':
                    next_pos = [snake.position[0], snake.position[1] - cfg.BLOCK]
                elif snake.direction == 'DOWN':
                    next_pos = [snake.position[0], snake.position[1] + cfg.BLOCK]
                elif snake.direction == 'LEFT':
                    next_pos = [snake.position[0] - cfg.BLOCK, snake.position[1]]
                elif snake.direction == 'RIGHT':
                    next_pos = [snake.position[0] + cfg.BLOCK, snake.position[1]]

    if not cfg.paused:
        # движение
        if snake.direction == 'UP':
            snake.set_position([snake.position[0], snake.position[1] - cfg.BLOCK])

        elif snake.direction == 'DOWN':
            snake.set_position([snake.position[0], snake.position[1] + cfg.BLOCK])

        elif snake.direction == 'LEFT':
            snake.set_position([snake.position[0] - cfg.BLOCK, snake.position[1]])

        elif snake.direction == 'RIGHT':
            snake.set_position([snake.position[0] + cfg.BLOCK, snake.position[1]])

        # выключение ускорения
        if cfg.boost_end_time and pygame.time.get_ticks() >= cfg.boost_end_time:
            cfg.speed -= cfg.SPEED_BOOST
            cfg.boost_end_time = 0

        # удаление препятствия для замены на новое
        if (cfg.obstacle_lifetime and pygame.time.get_ticks() >= cfg.obstacle_lifetime) and len(cfg.current_obstacles) == 4:
            print("функция заработала")
            cfg.current_obstacles.pop(0)
            cfg.obstacle_lifetime = 0

        screen.fill((161,241,247))

        # сетка
        draw_grid(screen)

        # очки сверху экрана
        ingame_score = score_font.render(f"SCORE: {str(cfg.score).zfill(15)}", True, (82,87,91))
        ingame_score_rect = ingame_score.get_rect(center = (cfg.WIDTH // 2, 50))
        screen.blit(ingame_score, ingame_score_rect)

        # постоянная перезапись головы и удаление хвоста для иллюзии движения
        snake.update_body()

        # рендер каждой части змеюки
        snake.draw_body(screen)

        #рендер еды
        for piece in cfg.current_food:
            pygame.draw.rect(screen, (174,139,253) , pygame.Rect(piece[0], piece[1], cfg.BLOCK, cfg.BLOCK))

        # буста
        for boost in cfg.current_boost:
            pygame.draw.rect(screen, (172,253,139) , pygame.Rect(boost[0], boost[1], cfg.BLOCK, cfg.BLOCK))

        # препятствий поблочно
        for obs in cfg.current_obstacles:
            for block in obs:
                pygame.draw.rect(screen, (32,62,15), pygame.Rect(block[0], block[1], cfg.BLOCK, cfg.BLOCK))

        # столкновение с препятствием поблочно
        for obs in cfg.current_obstacles:
            for block in obs:
                if next_pos == block:
                    cfg.game_over = True
                    cfg.running = False

        # проверка на столкновение с границами и врезание змейки в себя
        if snake.check_collision_border() or snake.self_collision():
            #sound

            # crash_time = pygame.USEREVENT +2
            # pygame.time.set_timer(crash_time, 2500)
            # if event.type == crash_time:
            
            cfg.game_over = True
            cfg.running = False

        #ускорение-возвращение
        snake.get_boost()
            


    #окно паузы
    if cfg.paused:
        # -text
        paused_text = pause_font.render("Пауза!", True, (82,87,91))
        pause_rect = paused_text.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2))
        screen.blit(paused_text, pause_rect)

    pygame.display.flip()

    clock.tick(cfg.speed)


# окно конца игры
while cfg.game_over:

    screen.fill((161,241,247))

    go_show_score = pause_font.render(f"Игра закончена! Ваш счет: {cfg.score}", True, (82,87,91))
    go_score_rect = go_show_score.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2))
    screen.blit(go_show_score, go_score_rect)

    exit_go_text = pause_font.render("Нажмите X для выхода", True, (82,87,91))
    go_exit_rect = exit_go_text.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT - 50) )
    screen.blit(exit_go_text, go_exit_rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                cfg.game_over = False
                

    pygame.display.flip()
    
    clock.tick(cfg.speed)

pygame.quit()

# todo:

# музыка базовая, ускорение
# шрифт из файла
# звук при паузе, геймовере, кратком столкновении со стеной

# картинки и змейку градиентную если получится