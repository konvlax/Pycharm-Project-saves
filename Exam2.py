import pygame as pg
import random
import sys

pg.init()

# настройки
width, height = 800, 600
sc = pg.display.set_mode((width, height))
pg.display.set_caption("cyber defense: shapes attack")

# цвета
black = (10, 10, 10)
neon_green = (57, 255, 20)
neon_red = (255, 7, 58)
white = (255, 255, 255)

# загрузка базы
base_img = pg.image.load('car1.png').convert_alpha()
base_img = pg.transform.scale(base_img, (100, 100))
base_rect = base_img.get_rect(center=(width //2, height // 2))

# враги
enemies = []


def create_enemy():
    side = random.choice(['top', 'bottom', 'left', 'right'])
    if side == 'top':
        x, y = random.randint(0, width), -40
    elif side == 'bottom':
        x, y = random.randint(0, width), height + 40
    elif side == 'left':
        x, y = -40, random.randint(0, height)
    else:
        x, y = width + 40, random.randint(0, height)
    rect = pg.Rect(x, y, 30, 30)
    # направление к центру
    dx = (width // 2 - x) / 100
    dy = (height // 2 - y) / 100

    return [rect, dx, dy]


# таймер появления врагов
spawn_event = pg.USEREVENT + 1
pg.time.set_timer(spawn_event, 1500)

clock = pg.time.Clock()
score = 0

# гейм-цикл
while True:
    enemy_type = random.randint(1, 2)
    sc.fill(black)
    mouse_pos = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            print(score)
            sys.exit()

        if event.type == spawn_event:
            enemies.append(create_enemy())

        if event.type == pg.MOUSEBUTTONDOWN:
            for e in enemies[:]:
                if e[0].collidepoint(mouse_pos):
                    enemies.remove(e)
                    score += 1

        for e in enemies[:]:
            e[0].x += e[1]
            e[0].y += e[2]
            if enemy_type == 1:
                pg.draw.rect(sc, neon_red, e[0], 2)
                pg.draw.circle(sc, neon_red, e[0].center, 5)
            elif enemy_type == 1:
                pg.draw.polygon(sc, neon_red, e[0], 2)
                pg.draw.circle(sc, neon_red, e[0].center, 5)

            if e[0].colliderect(base_rect):
                print(f'игра окончена. Счет: {score}')
                sys.exit()

        pg.draw.line(sc, neon_green, (width // 2, height // 2), mouse_pos, 1)
        pg.draw.circle(sc, neon_green, mouse_pos, 15, 2)

        sc.blit(base_img, base_rect)

        pg.display.flip()
        clock.tick(60)

pg.quit()
