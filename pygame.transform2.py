from random import randint
import pygame as pg
import sys

pg.init()
pg.time.set_timer(pg.USEREVENT, 3000)


w = 1920
h = 1070

white = (255, 255, 255)

cars = ('car1.png', 'car2.png', 'car3.png')
cars_surf = []


class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

    def update(self):
        if self.rect.y < h:
            self.rect.y += 2
        else:
            self.rect.y = 0


sc = pg.display.set_mode((w, h))

for i in range(len(cars)):
    cars_surf.append(pg.image.load(cars[i]).convert_alpha())

car1 = Car(randint(1, w), 'car.png')
car2 = Car(randint(1, w), 'car.png')
car3 = Car(randint(1, w), 'car.png')

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    sc.fill(white)
    sc.blit(car1.image, car1.rect)

    pg.display.update()
    pg.time.delay(20)
    if car1.rect.y < h:
        car1.rect.y += 2
    else:
        car1.rect.y = 0
