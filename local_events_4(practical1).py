import pygame as pg
import sys

pg.init()

win_width = 800
win_height = 600
sc = pg.display.set_mode((win_width, win_height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


class Obj1:
    width = 20
    height = 50

    def __init__(self, color):
        self.color = color


class Obj2:
    width = 30
    height = 10

    def __init__(self, color):
        self.color = color


class Obj3:
    width = 10
    height = 30

    def __init__(self, color):
        self.color = color


o1 = Obj1(red)
o2 = Obj2(green)
o3 = Obj3(blue)

x1, y1 = 100, 100
x2, y2 = 100, 200
x3, y3 = 100, 300



while True:
    sc.fill(white)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:  # ЛКМ - вправо
                x1 += 25
                x2 += 25
                x3 += 25
            elif i.button == 3:  # ПКМ - влево
                x1 -= 25
                x2 -= 25
                x3 -= 25

    # Отрисовка объектов
    pg.draw.rect(sc, o1.color, (x1, y1, o1.width, o1.height))
    pg.draw.rect(sc, o2.color, (x2, y2, o2.width, o2.height))
    pg.draw.rect(sc, o3.color, (x3, y3, o3.width, o3.height))

    pg.display.update()
