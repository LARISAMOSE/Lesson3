import pygame
import random
import time

pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Название и иконка окна
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("image/free-icon-shooting-range-2689911.png")
pygame.display.set_icon(icon)

# Загрузка изображения мишени
target_img = pygame.image.load("image/target.png")

# Размеры мишени
target_width = 80
target_height = 80

# Начальное положение мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость движения мишени (уменьшена)
target_speed_x = random.choice([-1, 1])
target_speed_y = random.choice([-1, 1])

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Подсчет очков
score = 0

# Время игры (в секундах)
game_duration = 60
start_time = time.time()

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

# Основной цикл игры
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_speed_x = random.choice([-1, 1])
                target_speed_y = random.choice([-1, 1])
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Обновляем цвет фона при попадании
                score += 1

    # Движение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Отражение мишени от границ экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Отображение мишени
    screen.blit(target_img, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Проверка на окончание времени игры
    elapsed_time = time.time() - start_time
    if elapsed_time >= game_duration:
        running = False

    pygame.display.update()
    # Добавление задержки для замедления игрового цикла
    pygame.time.delay(30)

# Отображение итогового счета
screen.fill((0, 0, 0))
final_score_text = font.render(f"Игра окончена! Ваш счет: {score}", True, (255, 255, 255))
screen.blit(final_score_text, (
    SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 - final_score_text.get_height() // 2))
pygame.display.update()
time.sleep(5)

# Завершение Pygame
pygame.quit()

