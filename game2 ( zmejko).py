import pygame
import random

width = 1920
height = 1080
fps = 60

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 102)

snake_block = 10
snake_speed = 15

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Жесткая змкейка для Жестких ребят")

clock = pygame.time.Clock()

font_style = pygame.font.SysFont('bahnschrift', 25)
score_font = pygame.font.SysFont('comicsansms', 35)


def display_score(score):
    value = score_font.render(f"ваш счет: {score}", True, yellow)
    screen.blit(value, [10, 10])


def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], block_size, block_size])


def show_message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(width / 2, height / 3))
    screen.blit(mesg, text_rect)


def generate_food():
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10) * 10
    return foodx, foody


def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0


    snake_list = []
    lenght_of_snake = 1

    foodx, foody = generate_food()

    while not game_over:
        while game_close:
            screen.fill(blue)
            show_message('вы проигрыли! q - выход, c - сначала', red)
            display_score(lenght_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game_loop()             # === перезапуск гейм-лупа

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN and y1_change == 0:
                        y1_change = snake_block
                        x1_change = 0

