import pygame
import os
import assets


pygame.init()

# Определение размеров окна
window_width = 800
window_height = 600

# Создание поверхности для отображения
window = pygame.display.set_mode((window_width, window_height))

# Установка заголовка окна
pygame.display.set_caption("Дорога с машинами")

# Загрузка спрайта для дороги
road_img = pygame.image.load(os.path.join('assets', 'road.png'))
road_img = pygame.transform.scale(road_img, (window_width, window_height))

# Загрузка спрайтов для машин
car_img = pygame.image.load(os.path.join('assets', 'car.png'))


# Определение размеров машин и полос
car_width = 28
car_height = 46
lane_width = window_width // 4

# Определение начальных позиций машин
car_x = lane_width - car_width // 2
car_y = window_height


# Определение скорости движения машин
car_speed = 5

# Определение флага для цикла игры
running = True

# Главный игровой цикл
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка фона
    window.blit(road_img, (0, 0))

    # Обновление позиций машин
    car_y -= car_speed


    # Отрисовка машин
    window.blit(car_img, (car_x, car_y))


    # Проверка и исправление позиции машин
    if car_y + car_height < 0:
        car_y = window_height

    # Обновление окна
    pygame.display.flip()


pygame.quit()