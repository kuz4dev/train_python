import pygame
import random

pygame.init()

clock = pygame.time.Clock()

#ширина окна
WIDTH = 800
#высота окна
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
#название игры
pygame.display.set_caption("Леталки!")

#широта корабля
spaceship_width = 80
#высота корабля
spaceship_height = 70
#широта положения корабля
spaceship_x = WIDTH - 790
#высота положения корабля
spaceship_y = HEIGHT - spaceship_height - 30
#скорость корабля
spaceship_speed = 8

#широта метеорита
meteorit_x = WIDTH - 30
#высота метеорита
meteorit_y = HEIGHT
#радиус метеорита
meteorit_radius = 15
#скорость метеорита
meteorit_speed = 5

#радиус снаряда
bullet_radius = 20
#скорость снаряда
bullet_speed = 7

bullets = []
meteorits = []
spawn_timer = 0
# Интервал между появлением метеоритов в миллисекундах
spawn_interval = 80  

#cчет
score = 0
#жизни
lives = 3

font = pygame.font.SysFont(None, 30)

paused = False

running = True

# background_image = pygame.image.load("assets/space_background.png").convert()
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

spaceship_image = pygame.image.load("assets/spaceship.png").convert_alpha()
spaceship_image = pygame.transform.scale(spaceship_image, (spaceship_width, spaceship_height))

# meteorit_image = pygame.image.load("assets/meteorit.jpg").convert_alpha()
# meteorit_image = pygame.transform.scale(meteorit_image, (meteorit_radius * 2, meteorit_radius * 2))

bullet_image = pygame.image.load("assets/bullet.png").convert_alpha()
bullet_image = pygame.transform.scale(bullet_image, (bullet_radius * 2, bullet_radius * 2))

# # catch_sound = pygame.mixer.Sound("assets/catch.wav")
# # miss_sound = pygame.mixer.Sound("assets/miss.wav")

# pygame.mixer.music.load("assets/main_track.mp3")
# pygame.mixer.music.play(-1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                bullets.append({"x": spaceship_x + spaceship_width, "y": spaceship_y + (spaceship_height // 2)})
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                paused = not paused
                # if paused == True:
                #     pygame.mixer.music.load("assets/main_track.mp3")
                #     pygame.mixer.music.play(-1)
                # else:
                #     pygame.mixer.music.load("assets/pause_track.mp3")
                #     pygame.mixer.music.play(-1)

    if not paused:
        keys = pygame.key.get_pressed()

        # Логика передвижения корабля
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            spaceship_y -= spaceship_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            spaceship_y += spaceship_speed

        if spaceship_y < 0:
            spaceship_y = 0
        if spaceship_y > HEIGHT - spaceship_height:
            spaceship_y = HEIGHT - spaceship_height

        # Логика метеоритов
        spawn_timer += 1

        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            meteorit_y = random.randint(150, 600)
            meteorits.append({"x": meteorit_x, "y": meteorit_y})


        for meteorit in meteorits:
            meteorit["x"] -= meteorit_speed

        for bullet in bullets:
            bullet["x"] += bullet_speed
            
        bullets = [b for b in bullets if b["x"] < WIDTH]
        
        spaceship_rect = pygame.Rect(spaceship_x, spaceship_y, spaceship_width, spaceship_height)

        remaining_meteorits = []

        for meteorit in meteorits:
            # Флаг на столкновение
            hit = False
            
            meteorit_rect = pygame.Rect(meteorit["x"] - meteorit_radius, meteorit["y"] - meteorit_radius, meteorit_radius * 2, meteorit_radius * 2)

            if spaceship_rect.colliderect(meteorit_rect):
                lives -= 1
                hit = True

            for bullet in bullets:
                bullet_rect = pygame.Rect(bullet["x"] - bullet_radius, bullet["y"] - bullet_radius, bullet_radius * 2, bullet_radius * 2)
                
                if bullet_rect.colliderect(meteorit_rect):
                    hit = True
                    score += 1
                    if bullet in bullets:
                        bullets.remove(bullet)
                    break
                
            if not hit:
                remaining_meteorits.append(meteorit)


        meteorits = remaining_meteorits

    screen.fill((200, 100, 200))

    for meteorit in meteorits:
        pygame.draw.circle(screen, (255, 255, 255), (meteorit["x"], meteorit["y"]), meteorit_radius)
        
    for bullet in bullets:
        screen.blit(bullet_image, (bullet["x"] - bullet_radius, bullet["y"] - bullet_radius))
# pygame.draw.circle(screen, (139, 139, 139), (bullet["x"], bullet["y"]), bullet_radius)
        
    screen.blit(spaceship_image, (spaceship_x, spaceship_y))
    
    #Счет
    score_text = font.render(f"Метеоритов отбито: {score}", True, (255, 255, 255))
    
    #Жизни
    lives_text = font.render(f"Полная поломка через: {lives}", True, (255, 255, 255))
    screen.blit(score_text, (25, 25))
    screen.blit(lives_text, (WIDTH - 300, 25))

    if paused:
        paused_text = font.render("Пауза!", True, (255, 255, 255))
        pause_rect = paused_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(paused_text, pause_rect)

    pygame.display.flip()

    #фпс
    clock.tick(60)

    #если жизней меньше или равно нулю = экран проигрыша
    if lives <= 0:
        running = False

pygame.mixer.music.stop()

game_over_text = font.render("Игра окончена!", True, (0, 0, 0))

showing_game_over = True

#пока показывает экран проигрыша
while showing_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((130, 206, 190))
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


#TODO:
# 2. ограничение области летания корабля, чтобы не залетал за надписи
# 4. Добавить задний фон
# 5. Добавить звуки
# 6. добавить комментарии
