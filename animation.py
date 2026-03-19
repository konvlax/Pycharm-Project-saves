import pygame, sys
from pygame.locals import *

pygame.init()

fps = 60
fpsclock = pygame.time.Clock()

displaysurf = pygame.display.set_mode((400, 320), 0, 32)
pygame.display.set_caption('animation')

white = (255, 255, 255)
green = (0, 255, 0)
catimg = pygame.image.load('мужчина1.png')
catx = 10
caty = 10
direction = 'right'
cat_speed = 5
while True:
    displaysurf.fill(green)
    # движ угла к углу 😋
    # if direction == 'right':
    #     catx += 2  # Уменьшил скорость, чтобы движение было заметным
    #     caty += 3
    #     if catx >= 55 or caty >= 80:
    #         direction = 'left'
    #
    # elif direction == 'left':
    #     catx -= 2
    #     caty -= 3
    #     if catx <= 0 or caty <= 0:
    #         direction = 'right'

    # движ прямоугольником ☺

    # if direction == 'right':
    #     catx += 5
    #     if catx >= 280:
    #         catx = 280
    #         direction = 'down'
    # elif direction == 'down':
    #     caty += 5
    #     if caty == 190:
    #         direction = 'left'
    # elif direction == 'left':
    #     catx -= 5
    #     if catx == 10:
    #         direction = 'up'
    # elif direction == 'up':
    #     caty -= 5
    #     if caty == 10:
    #         direction = 'right'
    # elif catx == 10 and caty == 10:
    #     cat_speed += 2
    # displaysurf.blit(catimg, (catx, caty))

    # движ с ускорением
    if direction == 'right':
        catx += cat_speed
        if catx >= 280:
            catx = 280
            direction = 'down'
    elif direction == 'down':
        caty += cat_speed
        if caty >= 190:
            direction = 'left'
    elif direction == 'left':
        catx -= cat_speed
        if catx <= 10:
            direction = 'up'
    elif direction == 'up':
        caty -= cat_speed
        if caty <= 10:
            direction = 'right'
    if catx <= 10 and caty <= 10:
        cat_speed += 5
    displaysurf.blit(catimg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsclock.tick(fps)


