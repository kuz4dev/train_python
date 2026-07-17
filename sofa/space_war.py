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

meteorits = []
spawn_timer = 0
# Интервал между появлением метеоритов в миллисекундах
spawn_interval = 80  

#cчет
score = 0
#жизни
lives = 3


font = pygame.font.SysFont(None, 25)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    
    spaceship_rect = pygame.Rect(spaceship_x, spaceship_y, spaceship_width, spaceship_height)
    
    remaining_meteorits = []

    for meteorit in meteorits:
        meteorit_rect = pygame.Rect(meteorit["x"] - meteorit_radius, meteorit["y"] - meteorit_radius, meteorit_radius * 2, meteorit_radius * 2)

        if spaceship_rect.colliderect(meteorit_rect):
            lives -= 1
        else:
            remaining_meteorits.append(meteorit)

    meteorits = remaining_meteorits

    screen.fill((200, 100, 200))

    for meteorit in meteorits:
        pygame.draw.circle(screen, (255, 255, 255), (meteorit["x"], meteorit["y"]), meteorit_radius)
    pygame.draw.rect(screen, (0, 0, 0), (spaceship_x, spaceship_y, spaceship_width, spaceship_height))
    

    #Счет
    score_text = font.render(f"Метеоритов отбито: {score}", True, (255, 255, 255))
    #Жизни
    lives_text = font.render(f"Полная поломка через: {lives}", True, (255, 255, 255))
    screen.blit(score_text, (25, 25))
    screen.blit(lives_text, (WIDTH - 300, 25))

    pygame.display.flip()

    #фпс
    clock.tick(60)

    #если жизней меньше или равно нулю = экран проигрыша
    if lives <= 0:
        running = False

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
# 1. Cтрельба. при попадании в метеорит. метеорит пропадает.
# 2. ограничение области летания корабля, чтобы не залетал за надписи
# 3. Поставить на паузу
# 4. Добавить задний фон и спрайты
# 5. Добавить музыку и звуки
# 6. Переименовать + добавить комментарии
