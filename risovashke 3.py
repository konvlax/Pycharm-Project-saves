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
l_blue = (32, 178, 170)

# рисование на объекте поверхности
# машина
displaysurf.fill(blue)
pygame.draw.rect(displaysurf, red, (175, 200, 150, 50))
pygame.draw.circle(displaysurf, gray, (200, 250), 15, 0)
pygame.draw.circle(displaysurf, gray, (300, 250), 15, 0)
pygame.draw.rect(displaysurf, l_blue, (290, 205, 30, 20))

# снеговик

pygame.draw.circle(displaysurf, white, (200, 90), 20, 0)
pygame.draw.circle(displaysurf, white, (200, 120), 25, 0)
pygame.draw.circle(displaysurf, white, (200, 150), 30, 0)
pygame.draw.line(displaysurf, black)







while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
