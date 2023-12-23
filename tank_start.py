if score >= 5:
    window.blit(tank_img, (tank_x, tank_y))
    pygame.display.flip()

if tank_rect.colliderect(barrier_rect):
    barrier_img = pygame.image.load(os.path.join('barrier_boom.png'))
if tank_rect.colliderect(car_rect):
    car_img = pygame.image.load(os.path.join('car_boom.png'))