import pygame 

pygame.init()

clock = pygame.time.Clock()

speed = 5
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Дудл джамп")

player_x = 0
player_y = 300
player_size = 30

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    if player_x < 0:
        player_x = screen_width - player_size
    if player_x > screen_width - player_size:
        player_x = 0
    if player_y < 0:
        player_y = screen_height - player_size
    if player_y > screen_height - player_size:    
        player_y = 0

    screen.fill((30, 60, 90))

    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_size, player_size))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

# Домашка!!!

# Змейка Ксю:
# Реализовать рандомное появление еды для змейки (с ограничениями)
# Добавить логику съедания еды и увилечения очков
# Увиличивать змейку и продумать логику столкновения с самой собой и логику движения змейки
# Логика победы и проигрыша
# Поработать над тем чтобы сделать сущности не просто фигурами + задний фон

# Космическая игра Софа:
# Добавить спрайт (круг) и движения корабля и стрелять на пробел
# Реализация анимации движения окружения
# Рандомно отображать врагов и их движения (учесть места спавна, для начала сделать рандомно с середины до конца окна)
# Столкновение с врагом
# Поработаем над картинкой
# Добавить бонусы (усиления) - например, лучше пушка, выпускается не 1 снаряд, а 3 
