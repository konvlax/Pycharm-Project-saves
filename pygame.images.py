import pygame as pg
import sys

w = 1920
h = 1080

sc = pg.display.set_mode((w, h))
sc.fill((100, 150, 200))

# dog_surf = pg.image.load('dog.bmp')
# dog_surf.set_colorkey((255, 255, 255))
# sun_surf = pg.image.load('sun.png')
# sun_rect = sun_surf.get_rect()
# sc.blit(sun_surf, sun_rect)
dog_surf = pg.image.load('dog.bmp').convert()
sun_surf = pg.image.load('sun.png').convert_alpha()
dog_rect = dog_surf.get_rect(bottomright=(w, h))
sc.blit(dog_surf, dog_rect)
pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(20)

