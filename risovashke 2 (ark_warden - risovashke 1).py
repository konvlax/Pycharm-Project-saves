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
displaysurf.fill(white)

pygame.draw.rect(displaysurf, red, (390, 20, 100, 50))
pygame.draw.polygon(displaysurf, green, ((100, 200), (150, 100), (200, 200)))

a = 300
pixObj = pygame.PixelArray(displaysurf)
for i in range(50):
    pixObj[400][a] = black
    pixObj[415][a] = black
    pixObj[430][a] = black
    pixObj[445][a] = black
    pixObj[460][a] = black
    a += 2
for i in range(50):
    pixObj[a][300] = black
    pixObj[a][315] = black
    pixObj[a][330] = black
    pixObj[a][345] = black
    pixObj[a][360] = black
    pixObj[a][375] = black
    pixObj[a][390] = black
    a += 2
del pixObj

# игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
