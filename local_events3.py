import pygame as pg
import sys
win_width = 800
win_height = 600
white = (255, 255, 255)
black = (0, 0, 0)


class Rocket:
    width_rocket = 20
    height_rocket = 50

    def __init__(self, surface, color):
        self.surf = surface
        self.color = color
        self.x = surface.get_width()//2 - Rocket.width_rocket // 2
        self.y = surface.get_height()

    def fly(self):
        pg.draw.rect(self.surf, self.color, (self.x, self.y, Rocket.width_rocket, Rocket.height_rocket))

        self.y -= 3

        if self.y < -Rocket.height_rocket:
            self.y = self.surf.get_height()


sc = pg.display.set_mode((win_width, win_height))

surf_left = pg.Surface((win_width//2, win_height))
surf_left.fill(white)
surf_right = pg.Surface((win_width//2, win_height))

sc.blit(surf_left, (0, 0))
sc.blit(surf_right, (win_width//2, 0))

rocket_left = Rocket(surf_left, black)
rocket_right = Rocket(surf_right, white)

active_left = False
active_right = False

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.MOUSEBUTTONUP:
            if i.pos[0] < win_width//2:
                active_left = True
                active_right = False
            elif i.pos[0] > win_width//2:
                active_right = True
                active_left = False

    if active_left:
        surf_left.fill(white)
        rocket_left.fly()
        sc.blit(surf_left, (0, 0))
        sc.blit(surf_left, (0, 0))
    elif active_right:
        surf_right.fill(black)
        rocket_right.fly()
        sc.blit(surf_right, (win_width//2, 0))

    pg.display.update()
    pg.time.delay(20)
