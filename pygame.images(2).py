import pygame as pg
import sys

bk = pg.image.load('background.jpg')
w, h = bk.get_size()

sc = pg.display.set_mode((w, h))
bg = pg.Surface((w, h))
sc.blit(bk, (0, 0))

sun = pg.image.load('sun1.png').convert_alpha()
dog = pg.image.load('dog.bmp').convert_alpha()
sun_rect = sun.get_rect(topleft=(0, 20))
dog_rect = dog.get_rect(bottomright=(w, h))

pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                sun_rect.x += -15
            elif i.key == pg.K_RIGHT:
                sun_rect.x += 15
            elif i.key == pg.K_UP:
                sun_rect.y += -15
            elif i.key == pg.K_DOWN:
                sun_rect.y += 15

    sc.blit(bg, dog_rect, dog_rect)
    sc.blit(bg, sun_rect, sun_rect)
    sc.blit(sun, sun_rect)
    pg.display.update()
    sc.blit(bk, (0, 0))

    pg.time.delay(20)
