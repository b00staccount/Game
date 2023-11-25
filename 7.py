import pygame
import os
import time

# Инициализация pygame
pygame.init()

# Определение размеров окна
window_width = 800
window_height = 600

# Создание поверхности для отображения
window = pygame.display.set_mode((window_width, window_height))

# Установка заголовка окна
pygame.display.set_caption("game")

# Загрузка спрайта для дороги

road_img = pygame.image.load(os.path.join('../../Downloads/road2.png'))
road_img = pygame.transform.scale(road_img, (window_width, window_height))

# Загрузка спрайтов для машин
car_img = pygame.image.load(os.path.join('../../Downloads/car.png'))

# Определение размеров машин и полос
car_width = 50
car_height = 80
lane_width = window_width // 4

# Определение начальных позиций машин
car_x = lane_width - car_width // 2
car_y = 300

# Определение скорости движения машин
car_speed = 2

# Определение скорости передвижения машины по горизонтали
car_move_speed = 2

# Определение флага для цикла игры
running = True

# Флаг для ускорения движения машин
accelerate = False

# Счетчик для движения дороги
road_counter = 0

# Ограничение области, в которой может находиться спрайт car
min_x = lane_width - 50
max_x = window_width - lane_width + 20

# Система получения очков за счет проведенного времени
score = 0
clock = pygame.time.Clock()

# Главный игровой цикл
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Проверка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                accelerate = True
                car_speed += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                accelerate = False
                car_speed += 3
        if event.type == pygame.K_LEFT:
            if event.key == pygame.K_l:
                car_img = pygame.image.load(os.path.join('../../Downloads/car_left.png'))
            else:
                car_img = pygame.image.load(os.path.join('../../Downloads/car.png'))

        if event.type == pygame.K_RIGHT:
            if event.key == pygame.K_r:
                car_img = pygame.image.load(os.path.join('../../Downloads/car_right.png'))
            else:
                car_img = pygame.image.load(os.path.join('../../Downloads/car.png'))


    # Обновление позиции дороги
    # if accelerate:
    #     road_counter = car_speed * 2
    # else:
    #     road_counter = car_speed
    print(car_speed)
    if car_speed > 1:
        car_speed -= 0.2
    road_counter -= car_speed

    # Если дорога достигла нижнего края окна, сбрасываем счетчик
    if road_counter <= -window_height:
        road_counter = 0

    # Отрисовка фона
    window.blit(road_img, (0, road_counter))
    window.blit(road_img, (0, road_counter + window_height))

    # Увеличение счета за проведенное время
    score += clock.tick(60) / 1000  # При условии, что цикл игры работает со скоростью 60 кадров в секунду

    #Определение движения машины по горизонтали
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_move_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_move_speed

    if keys[pygame.K_UP]:
        road_counter -= car_speed * 2
    else:
        road_counter -= car_speed

    if keys[pygame.K_LEFT]:
        car_img = pygame.image.load(os.path.join('car_left.png'))
    else:
        car_img = pygame.image.load(os.path.join('car.png'))

    if keys[pygame.K_RIGHT]:
        car_img = pygame.image.load(os.path.join('car_right.png'))



    # Ограничение области для спрайта car
    if car_x < min_x:
        car_x = min_x
    elif car_x > max_x:
        car_x = max_x

    # Отрисовка машин
    window.blit(car_img, (car_x, car_y))

    # Проверка и исправление позиции машин
    if car_y + car_height < 0:
        car_y = window_height

    # Отображение очков на главном экране
    font = pygame.font.Font(None, 36)
    score_text = font.render("score: " + str(int(score)), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Обновление окна
    pygame.display.flip()

# Завершение работы pygame
pygame.quit()