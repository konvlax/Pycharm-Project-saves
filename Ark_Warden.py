import pygame, sys
from pygame.locals import *

pygame.init()

# настройка окна
displaysurf = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('рисование')


# настройка цветов
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)
yellow = (255, 215, 0)

# рисование на объекте поверхности
displaysurf.fill(gray)
pygame.draw.polygon(displaysurf, yellow, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(displaysurf, blue, (60, 60), (120, 60), 10)
pygame.draw.line(displaysurf, blue, (120, 60), (60, 120))
pygame.draw.line(displaysurf, blue, (60, 120), (120, 120), 4)
pygame.draw.circle(displaysurf, blue, (300, 50), 20, 0)
pygame.draw.circle(displaysurf, gray, (300, 50), 15, 0)
pygame.draw.ellipse(displaysurf, red, (10, 300, 40, 80), 1)
pygame.draw.rect(displaysurf, red, (390, 20, 100, 50))
pygame.draw.rect(displaysurf, red, (200, 140, 100, 100))

pixObj = pygame.PixelArray(displaysurf)
pixObj[480][380] = black
pixObj[482][382] = black
pixObj[484][384] = black
pixObj[486][386] = black
pixObj[488][388] = black
del pixObj

# игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


