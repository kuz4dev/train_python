import os
import pygame
import random

from configuration import config as cfg

def playng_game():
    while cfg.running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    cfg.bullets.append({"x": cfg.spaceship_x + cfg.spaceship_width, "y": cfg.spaceship_y + (cfg.spaceship_height // 2)})
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    if cfg.paused:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                    cfg.paused = not cfg.paused
                if event.key == pygame.K_c:
                    cfg.music = not cfg.music
                    if cfg.music:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                    
        if not cfg.paused:
            keys = pygame.key.get_pressed()
            
            #Передвижение корабля
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                cfg.spaceship_y -= cfg.spaceship_speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                cfg.spaceship_y += cfg.spaceship_speed

            #ограничение корабля
            if cfg.spaceship_y < cfg.spaceship_height / 2:
                cfg.spaceship_y = cfg.spaceship_height / 2
            if cfg.spaceship_y > cfg.HEIGHT - cfg.spaceship_height:
                cfg.spaceship_y = cfg.HEIGHT - cfg.spaceship_height

            # Логика метеоритов
            cfg.spawn_timer += 1

            if cfg.spawn_timer >= cfg.spawn_interval:
                cfg.spawn_timer = 0
                meteorit_y = random.randint(150, 600)
                cfg.meteorits.append({"x": cfg.meteorit_x + 80, "y": meteorit_y})


            for meteorit in cfg.meteorits:
                meteorit["x"] -= cfg.meteorit_speed

            for bullet in cfg.bullets:
                bullet["x"] += cfg.bullet_speed
                
            cfg.bullets = [b for b in cfg.bullets if b["x"] < cfg.WIDTH]
            
            spaceship_rect = pygame.Rect(cfg.spaceship_x, cfg.spaceship_y, cfg.spaceship_width, cfg.spaceship_height)

            remaining_meteorits = []

            for meteorit in cfg.meteorits:
                #столкновение
                hit = False
                
                meteorit_rect = pygame.Rect(meteorit["x"] - cfg.meteorit_radius, meteorit["y"] - cfg.meteorit_radius, cfg.meteorit_radius * 2, cfg.meteorit_radius * 2)

                if spaceship_rect.colliderect(meteorit_rect):
                    cfg.lives -= 1
                    hit = True

                for bullet in cfg.bullets:
                    bullet_rect = pygame.Rect(bullet["x"] - cfg.bullet_radius // 2, bullet["y"] - cfg.bullet_radius // 2, cfg.bullet_radius, cfg.bullet_radius)
                    
                    if bullet_rect.colliderect(meteorit_rect):
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
            cfg.screen.blit(cfg.meteorit_image, (meteorit["x"] - cfg.meteorit_radius, meteorit["y"] - cfg.meteorit_radius))
            
        #вывод пуль
        for bullet in cfg.bullets:
            cfg.screen.blit(cfg.bullet_image, (bullet["x"] - cfg.bullet_radius // 2, bullet["y"] - cfg.bullet_radius // 2))
            
        cfg.screen.blit(cfg.spaceship_image, (cfg.spaceship_x, cfg.spaceship_y))
        
        #Счет
        score_text = cfg.font.render(f"Метеоритов отбито: {cfg.score}", True, (255, 255, 255))
        #Жизни
        lives_text = cfg.font.render(f"Полная поломка через: {cfg.lives}", True, (255, 255, 255))
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

        #если жизней меньше или равно нулю = экран проигрыша
        if cfg.lives <= 0:
            cfg.running = False
            cfg.showing_game_over = True

