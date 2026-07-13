import pygame
import random

pygame.init()

clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Леталки!")

wolf_width = 130
wolf_height = 70
wolf_x = WIDTH // 5 - wolf_width // 2
wolf_y = HEIGHT - wolf_height - 30
wolf_speed = 8

egg_x = WIDTH // 2
egg_y = HEIGHT
egg_radius = 15
egg_speed = 5

#полоска. когда метеорит сталкивается с полоской += 1 в счет
over_width = 8
over_height = 600
over_x = 1
over_y = HEIGHT - over_height

eggs = []
spawn_timer = 0
spawn_interval = 60  # Интервал между появлением яиц в миллисекундах

score = 0
lives = 3


font = pygame.font.SysFont(None, 40)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Логика передвижения корабля
    #WS не работают
    if keys[pygame.K_UP or pygame.K_W]:
        wolf_y -= wolf_speed
    if keys[pygame.K_DOWN or pygame.K_S]:
        wolf_y += wolf_speed

    if wolf_y < 0:
        wolf_y = 0
    if wolf_y > HEIGHT - wolf_height:
        wolf_y = HEIGHT - wolf_height


    # Логика яйца
    spawn_timer += 1

    if spawn_timer >= spawn_interval:
        spawn_timer = 0
        egg_y = random.randint(150, 600)
        eggs.append({"x": egg_x, "y": egg_y})


    for egg in eggs:
        egg["x"] -= egg_speed

    
    wolf_rect = pygame.Rect(wolf_x, wolf_y, wolf_width, wolf_height)
    over_rect = pygame.Rect(over_x, over_y, over_width, over_height)
    
    remaining_eggs = []

    for egg in eggs:
        egg_rect = pygame.Rect(egg["x"] - egg_radius, egg["y"] - egg_radius, egg_radius * 2, egg_radius * 2)

        if over_rect.colliderect(egg_rect):
            score += 1
        elif egg["x"] - egg_radius > HEIGHT:
            lives += 1
        else:
            remaining_eggs.append(egg)

    eggs = remaining_eggs

    screen.fill((200, 100, 200))

    for egg in eggs:
        pygame.draw.circle(screen, (255, 255, 255), (egg["x"], egg["y"]), egg_radius)
    pygame.draw.rect(screen, (0, 0, 0), (wolf_x, wolf_y, wolf_width, wolf_height))
    pygame.draw.rect(screen, (0, 0, 0), (over_x, over_y, over_width, over_height))

    # Отображение счета очков и жизней
    score_text = font.render(f"Яиц поймано: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Жизней осталось: {lives}", True, (255, 255, 255))
    screen.blit(score_text, (25, 25))
    screen.blit(lives_text, (WIDTH - 300, 25))

    pygame.display.flip()

    clock.tick(60)

    if lives <= 0:
        running = False

game_over_text = font.render("Игра окончена!", True, (0, 0, 0))

showing_game_over = True
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
# Доработка:
# 1. Cтрельба. при попадании в метеорит. метеорит пропадает.
# 2. При пропуске метеорита (не попал и не столкновение)
# счет

# Фича - Поставить на паузу
# Фича - Добавить задний фон и картинки
# Фича - Добавить музыку и звуки


# FIXME:
# Уменьшить расстояние до корабля слева
# Уменьшить корабль
# Сделать так чтобы кометы появлялись сразу у правой грани + сделать их медленнее
# Переименовать + добавить комментарии
