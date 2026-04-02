import pygame as pg
import sys

w = 800
h = 600
bg = (100, 170, 220)

sc = pg.display.set_mode((w, h))
sc.fill(bg)

origin_surf = pg.image.load('мужчина.png').convert_alpha()
origin_rect = origin_surf.get_rect(center=(w/2, h/2))
sc.blit(origin_surf, origin_rect)
pg.display.update()
new_surf = pg.transform.rotate(origin_surf, 0)
pg.time.wait(1000)

x = 0
y = 0
MAIN_rect = origin_surf.get_rect(topleft=(x, y))


sc.fill(bg)
new_rect = new_surf.get_rect(center=(w/2, h/2))
sc.blit(new_surf, new_rect)
pg.display.update()


while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    keys = pg.key.get_pressed()

            # Проверяем зажатые клавиши
    if keys[pg.K_RIGHT]:
        MAIN_rect.x += 10
        new_surf = pg.transform.rotate(origin_surf, 0)
    elif keys[pg.K_LEFT]:
        MAIN_rect.x -= 10
        new_surf = pg.transform.rotate(origin_surf, 180)
    elif keys[pg.K_UP]:
        MAIN_rect.y -= 10
        new_surf = pg.transform.rotate(origin_surf, 90)
    elif keys[pg.K_DOWN]:
        MAIN_rect.y += 10
        new_surf = pg.transform.rotate(origin_surf, 270)



    sc.fill(bg)

    new_rect = new_surf.get_rect(center=(w / 2, h / 2))

    sc.blit(new_surf, MAIN_rect)
    pg.display.update()

    pg.time.delay(100)