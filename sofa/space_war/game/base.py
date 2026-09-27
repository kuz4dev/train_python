import pygame
import random

from configuration import config as cfg
from .space_ship import Spaceship
from .meteorit import Meteorit

#пока показывает основную игру
def playng_game():
    # создаем экземпляры классов
    ship = Spaceship()
    
    while cfg.running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #если кнопка e нажата
                if event.key == pygame.K_e:
                    #выпуск пули
                    cfg.bullets.append(ship.shoot())
            if event.type == pygame.KEYDOWN:
                #если нажат таб
                if event.key == pygame.K_TAB:
                    # если игра на паузе
                    if cfg.paused:
                        #постави
                        pygame.mixer.music.unpause()
                        #
                    else:
                        pygame.mixer.music.pause()
                    cfg.paused = not cfg.paused
                if event.key == pygame.K_c:
                    cfg.music = not cfg.music
                    if not cfg.paused:
                        if cfg.music:
                            pygame.mixer.music.unpause()
                        else:
                            pygame.mixer.music.pause()
                    
        if not cfg.paused:
            ship.move(pygame.key.get_pressed())

            # Логика метеоритов
            cfg.spawn_timer += 1

            if cfg.spawn_timer >= cfg.spawn_interval:
                cfg.spawn_timer = 0
                cfg.meteorits.append(Meteorit())


            for meteorit in cfg.meteorits:
                meteorit.move()

            for bullet in cfg.bullets:
                bullet["x"] += cfg.bullet_speed
                
            cfg.bullets = [b for b in cfg.bullets if b["x"] < cfg.WIDTH]
            
            spaceship_rect = ship.rect

            remaining_meteorits = []

            for meteorit in cfg.meteorits:
                #столкновение
                hit = False

                if spaceship_rect.colliderect(meteorit.rect):
                    hit = True
                    alive = ship.minus_lives()
                    cfg.running = alive
                    cfg.showing_game_over = not alive

                for bullet in cfg.bullets:
                    bullet_rect = pygame.Rect(bullet["x"] - cfg.bullet_radius // 2, bullet["y"] - cfg.bullet_radius // 2, cfg.bullet_radius, cfg.bullet_radius)
                    
                    if bullet_rect.colliderect(meteorit.rect):
                        hit = True
                        cfg.score += 1
                        if bullet in cfg.bullets:
                            cfg.bullets.remove(bullet)
                        break
                    
                if not hit:
                    remaining_meteorits.append(meteorit)

            cfg.meteorits = remaining_meteorits

        cfg.screen.blit(cfg.background_image, (0, 0))

        #вывод метеоритов
        for meteorit in cfg.meteorits:
            meteorit.draw()
            
        #вывод пуль
        for bullet in cfg.bullets:
            cfg.screen.blit(cfg.bullet_image, (bullet["x"] - cfg.bullet_radius // 2, bullet["y"] - cfg.bullet_radius // 2))
        
        ship.draw()
        
        #Счет
        score_text = cfg.font.render(f"Метеоритов отбито: {cfg.score}", True, (255, 255, 255))
        #Жизни
        lives_text = cfg.font.render(f"Полная поломка через: {ship.lives}", True, (255, 255, 255))
        #вывод текстов
        cfg.screen.blit(score_text, (25, 25))
        cfg.screen.blit(lives_text, (cfg.WIDTH - 360, 25))

        #пауза
        if cfg.paused:
            #текст
            paused_text = cfg.font.render("Пауза!", True, (255, 255, 255))
            control_text = cfg.font.render("WS - управление, E - выстрел", True, (255, 255, 255))
            control_text2 = cfg.font.render("TAB - пауза/продолжить, C - включить/выключить музыку", True, (255, 255, 255))

            #расположение текста
            pause_rect = paused_text.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2))
            control_rect = control_text.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2 + 70))
            control_rect2 = control_text2.get_rect(center = (cfg.WIDTH // 2, cfg.HEIGHT // 2 + 90))

            #вывод текста
            cfg.screen.blit(paused_text, pause_rect)
            cfg.screen.blit(control_text, control_rect)
            cfg.screen.blit(control_text2, control_rect2)

        pygame.display.flip()

        #фпс
        cfg.clock.tick(60)


 #rect круг, draw отрисовка, move движение,  spawn появление