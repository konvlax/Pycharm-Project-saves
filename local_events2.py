import sys
import pygame as pg
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

sc = pg.display.set_mode((400, 400))
#  1 )
# pg.draw.rect(sc, green, (0, 80, 300, 40))

# surf = pg.Surface((200, 150))
# surf.fill(white)
# surf.set_alpha(200)
# sc.blit(surf, (50, 25))
#
# pg.display.update()
#
# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()
#     pg.time.delay(100)
background = pg.Surface((400, 200))
xb = 0
yb = 100
hero = pg.Surface((100, 100))
hero.fill(red)
x = 0
y = 50

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        if i.type == pg.MOUSEBUTTONUP:
            yb = i.pos[1] - background.get_height() // 2

    if x < background.get_width():
        x += 2
    else:
        x = 0

    sc.fill(black)
    background.fill(green)

    background.blit(hero, (x, y))
    sc.blit(background, (xb, yb))

    pg.display.update()
    pg.time.delay(30)
