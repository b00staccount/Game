import pygame
import os
import random

pygame.init()

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("game")

barrier_img = pygame.image.load(os.path.join('barrier.png'))
road_img = pygame.image.load(os.path.join('road.png'))
road_img = pygame.transform.scale(road_img, (window_width, window_height))
car_img = pygame.image.load(os.path.join('car.png'))

car_width = 50
car_height = 80
lane_width = window_width // 4

barrier_width = 50
barrier_height = 80

car_x = lane_width + 75
car_y = 400

barrier_x = 200 - 27
barrier_y = 200

car_speed = 2
barrier_speed = -2

car_move_speed = 2.8

running = True

accelerate = False

road_counter = 0

min_x = 200 - 50
max_x = window_width - 200

score = 0
clock = pygame.time.Clock()

def show_game_over_text():
    font = pygame.font.Font(None, 100)
    game_over_text = font.render("WASTED", True, (255, 0, 0))
    text_rect = game_over_text.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(game_over_text, text_rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.key.get_pressed():
                accelerate = True
                car_speed += 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                accelerate = False
                car_speed += 1


    print(car_speed)
    if car_speed > 2.8:
        car_speed -= 0.03
        if car_speed >= 9:
            car_speed = 9
        barrier_speed = -car_speed + 2
    road_counter -= car_speed

    if road_counter <= -window_height:
        road_counter = 0

    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    barrier_rect = pygame.Rect(barrier_x, barrier_y, barrier_width, barrier_height)
    if car_rect.colliderect(barrier_rect):
        car_img = pygame.image.load(os.path.join('car_boom.png'))
        barrier_img = pygame.image.load(os.path.join('barrier_boom.png'))
        running = False

    window.blit(road_img, (0, -road_counter))
    window.blit(road_img, (0, -road_counter - window_height))

    score += clock.tick(60) / 1000

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_move_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_move_speed

    barrier_counter = 0
    barrier_counter -= car_speed
    if barrier_counter <= -window_height:
        barrier_counter = 0


    if accelerate:
        barrier_y -= barrier_speed * 2
    else:
        barrier_y -= barrier_speed

    if keys[pygame.K_UP]:
        road_counter -= car_speed * 2
    else:
        road_counter -= car_speed
    rotation_angle = 0

    if keys[pygame.K_LEFT]:
        rotation_angle += 30
        if rotation_angle > 30:
            rotation_angle = 30

    elif keys[pygame.K_RIGHT]:
        rotation_angle -= 30
        if rotation_angle < -30:
            rotation_angle = -30

    rotated_car_img = pygame.transform.rotate(car_img, rotation_angle)

    window.blit(rotated_car_img, (car_x, car_y))

    if car_x < min_x:
        car_x = min_x
    elif car_x > max_x:
        car_x = max_x

    window.blit(barrier_img, (barrier_x, barrier_y))


    if barrier_y >= window_height:
        barrier_y = 0

        random_num = random.randint(1, 1000) % 5
        barrier_x = 0

        if random_num == 1:
            barrier_x = 175
        elif random_num == 2:
            barrier_x = 275
        elif random_num == 3:
            barrier_x = 375
        elif random_num == 4:
            barrier_x = 475
        else:
            barrier_x = 575

    # 175 275 375

    # Отображаем barrier_img на экране
    window.blit(barrier_img, (barrier_x, barrier_y))

    if barrier_y >= window_height:
        barrier_y = 0

    if car_y + car_height < 0:
        car_y = window_height

    window.blit(barrier_img, (barrier_x, barrier_y))

    if barrier_y >= window_height:
        barrier_y = 0

    if car_y + car_height < 0:
        car_y = window_height

    font = pygame.font.Font(None, 36)
    score_text = font.render("score: " + str(int(score)), True, (255, 255, 255))
    window.blit(score_text, (10, 10))
    pygame.display.flip()
    car_width = 50
    car_height = 30

    if barrier_y >= window_height:
        barrier_y = 0

show_game_over_text()
pygame.display.flip()
pygame.time.wait(500)


pygame.quit()