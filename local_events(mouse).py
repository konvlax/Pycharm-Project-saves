import pygame as pg
import sys

white = (255, 255, 255)
red = (225, 0, 50)
green = (0, 255, 0)
blue = (0, 0, 255)

pg.init()
sc = pg.display.set_mode((400, 300))
sc.fill(white)

pg.display.update()

# 1)
# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()
#         if i.type == pg.MOUSEBUTTONDOWN:
#             if i.button == 1:
#                 pg.draw.circle(sc, red, i.pos, 20)
#                 pg.display.update()
#             elif i.button == 3:
#                 pg.draw.circle(sc, blue, i.pos, 20)
#                 pg.draw.rect(sc, green, (i.pos[0] - 10,
#                                          i.pos[1] - 10, 20, 20))
#                 pg.display.update()
#             elif i.button == 2:
#                 sc.fill(white)
#                 pg.display.update()
#     pg.time.delay(20)
# 2)
# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()
#
#     pressed = pg.mouse.get_pressed()
#     pos = pg.mouse.get_pos()
#     if pressed[0]:
#         pg.draw.circle(sc, red, pos, 5)
#         pg.display.update()
#
#     pg.time.delay(1)
# 3)
# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()
#
#     sc.fill(white)
#
#     if pg.mouse.get_focused():
#         pos = pg.mouse.get_pos()
#         pg.draw.rect(sc, blue, (pos[0] -10, pos[1] -10, 20, 20))
#
#         pg.display.update()
#         pg.time.delay(20)
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(100)