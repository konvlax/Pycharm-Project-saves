import pygame
import random

width = 1920
height = 1080
fps = 60

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

rect_size = 50
x = width // 2
y = height // 2
speed_x = 5
speed_y = 5


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('квадратэк')
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += speed_x
    y += speed_y

    if x + rect_size > width or x < 0:
        speed_x = -speed_x
    if y + rect_size > height or y < 0:
        speed_y = -speed_y

    screen.fill(black)

    # pygame.draw.rect(screen, blue, (x, y, rect_size, rect_size))
    pygame.draw.ellipse(screen, green, (x, y, rect_size * 1.5, rect_size))
    pygame.display.flip()

pygame.quit()
