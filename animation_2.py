import pygame, sys
from pygame.locals import *

pygame.init()

fps = 60
fpsclock = pygame.time.Clock()

displaysurf = pygame.display.set_mode((530, 759), 0, 32)
pygame.display.set_caption('animation')

white = (255, 255, 255)
green = (0, 255, 0)
catimg = pygame.image.load('мужчина1.png')
background = pygame.image.load('bridge1.png')
catx = 100
caty = 740
cat2x = 220
cat2y = 0
direction1 = 'up'
direction2 = 'down'
cat_speed = 5
while True:
    displaysurf.blit(background, (0, 0))
    if direction1 == 'up':
        caty -= cat_speed
        if caty <= 0:
            direction1 = 'down'
    elif direction1 == 'down':
        caty += cat_speed
        if caty >= 650:
            direction1 = 'up'

        # --- Движение ВТОРОГО ---
    if direction2 == 'down':
        cat2y += cat_speed
        if cat2y >= 650:
            direction2 = 'up'
    elif direction2 == 'up':
        cat2y -= cat_speed
        if cat2y <= 0:
            direction2 = 'down'

    displaysurf.blit(catimg, (catx, caty))
    displaysurf.blit(catimg, (cat2x, cat2y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mx, my = event.pos
            caty = my
            catx = mx
    pygame.display.update()
    fpsclock.tick(fps)