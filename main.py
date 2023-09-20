#Управление Стрелочки, E - Кушать, SpaceBar - Мяу

import pygame
import random
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создание окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра с котом Барсиком")

# Загрузка изображения кота Барсика
cat_image = pygame.image.load("cat.png")
cat_rect = cat_image.get_rect()
cat_rect.center = (WIDTH // 2, HEIGHT // 2)

# Загрузка карты
map_image = pygame.image.load("map.png")

# Загрузка звука "Мяу"
meow_sound = pygame.mixer.Sound("meow.wav")

# Начальное состояние кота
weight = 6

# Флаг для звука "Мяу"
play_meow = False

# Начальное направление кота
direction = "right"

# Скорость перемещения кота
speed = 5

# Скорость прыжка кота
jump_speed = 5

# Скорость вертикального движения кота
vertical_speed = 5

# Флаги для управления движением
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Таймер для потери веса
lose_weight_timer = pygame.time.get_ticks()
lose_weight_interval = 5000  # 5 секунд в миллисекундах

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if weight >= 0.5:
                    weight -= 0.5
                    if direction == "right":
                        cat_rect.y -= jump_speed  # Увеличение высоты прыжка
                    else:
                        cat_rect.y += jump_speed  # Увеличение высоты прыжка
                    play_meow = True  # Установка флага для воспроизведения "Мяу"
            elif event.key == pygame.K_e:
                weight += 1.5
            elif event.key == pygame.K_LEFT:
                moving_left = True
                direction = "left"  # Изменение направления на "left"
            elif event.key == pygame.K_RIGHT:
                moving_right = True
                direction = "right"  # Изменение направления на "right"
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    # Обновление координат кота в соответствии с флагами движения
    if moving_left:
        cat_rect.x -= speed
    if moving_right:
        cat_rect.x += speed
    if moving_up:
        cat_rect.y -= vertical_speed
    if moving_down:
        cat_rect.y += vertical_speed

    # Проверка состояния кота
    if weight <= 0:
        print("Кот умер от недоедания!")
        running = False
    elif weight > 15:
        print("Кот умер от переедания!")
        running = False

    # Потеря 1 кг каждые 5 секунд
    current_time = pygame.time.get_ticks()
    if current_time - lose_weight_timer >= lose_weight_interval:
        weight -= 1
        lose_weight_timer = current_time

    # Заливка экрана черным цветом
    screen.fill(BLACK)

    # Отображение карты
    screen.blit(map_image, (0, 0))

    # Отображение кота Барсика с учетом направления
    if direction == "right":
        screen.blit(cat_image, cat_rect)
    else:
        # Отразить изображение кота по горизонтали, чтобы он смотрел влево
        flipped_cat_image = pygame.transform.flip(cat_image, True, False)
        screen.blit(flipped_cat_image, cat_rect)

    # Отображение веса кота
    font = pygame.font.Font(None, 36)
    weight_text = font.render("Вес: {} кг".format(weight), True, WHITE)
    screen.blit(weight_text, (10, 10))

    # Воспроизведение звука "Мяу"
    if play_meow:
        meow_sound.play()
        play_meow = False

    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
