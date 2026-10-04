from game import config as cfg
import pygame
from game import (
    get_obstacle,
    get_food,
    boost_spawn,
    draw_grid,
    Snake,
)

snake = Snake()

def game_cycle(screen, score_font, pause_font, clock, food_event, boost_event, obstacle_event):

    cfg.load_sound()
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    while cfg.running:
        next_pos = snake.get_next_position()

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
            if (cfg.obstacle_lifetime and pygame.time.get_ticks() >= cfg.obstacle_lifetime) and len(cfg.current_obstacles) == 5:
                print("функция заработала")
                cfg.current_obstacles.pop(0)
                cfg.obstacle_lifetime = 0

            screen.blit(cfg.snake_game_background, (0, 0))

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
                screen.blit(piece[2], (piece[0], piece[1]))
                
            # буста
            for boost in cfg.current_boost:
                pygame.draw.rect(screen, (172,253,139) , pygame.Rect(boost[0], boost[1], cfg.BLOCK, cfg.BLOCK))

            # препятствий поблочно
            for obs in cfg.current_obstacles:
                for block in obs:
                    screen.blit(cfg.obstacle_image, (block[0], block[1]))
                    # pygame.draw.rect(screen, (32,62,15), pygame.Rect(block[0], block[1], cfg.BLOCK, cfg.BLOCK))

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

    pygame.mixer.music.stop()