import pygame as pg
import random
import sys
import time

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
font = pg.font.Font(None, 36)

# загрузка базы
base_img = pg.image.load('car1.png').convert_alpha()
base_img = pg.transform.scale(base_img, (100, 100))

base_rect = base_img.get_rect(center=(width // 2, height // 2))

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
    dx = (width // 2 - x) / 100
    dy = (height // 2 - y) / 100
    etype = random.randint(1, 2)

    return [rect, dx, dy, etype]


# таймер появления врагов
spawn_event = pg.USEREVENT + 1
pg.time.set_timer(spawn_event, 1500)

clock = pg.time.Clock()
score = 0
energy = 0
MAX_ENERGY = 10
ENERGY_EVENT = pg.USEREVENT + 2
pg.time.set_timer(ENERGY_EVENT, 200)

# гейм-цикл
while True:
    
    mouse_buttons = pg.mouse.get_pressed()
    sc.fill(black)
    mouse_pos = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            print(score)
            sys.exit()

        if event.type == ENERGY_EVENT:
            if energy < MAX_ENERGY:
                energy += 1

        if event.type == spawn_event:
            enemies.append(create_enemy())

        if pg.mouse.get_pressed()[0] and energy >= 1:
            pg.draw.line(sc, neon_green, (width // 2, height // 2), mouse_pos, 10)
            for e in enemies[:]:
                if e[0].collidepoint(mouse_pos):
                    enemies.remove(e)
                    score += 1
            energy -= 1

    # Логика движения и отрисовки
    for e in enemies[:]:
        rect, dx, dy, etype = e
        rect.x += dx
        rect.y += dy

        if etype == 1:

            pg.draw.rect(sc, neon_red, rect, 2)
        elif etype == 2:

            top_point = (rect.x + rect.width // 2, rect.y)

            left_bottom = (rect.x, rect.y + rect.height)

            right_bottom = (rect.x + rect.width, rect.y + rect.height)

            pg.draw.polygon(sc, neon_red, [top_point, left_bottom, right_bottom], 2)

        pg.draw.circle(sc, neon_red, rect.center, 5)

        if rect.colliderect(base_rect):
            print(f'игра окончена. Счет: {score}')
            sys.exit()

    pg.draw.line(sc, neon_green, (width // 2, height // 2), mouse_pos, 1)

    pg.draw.circle(sc, neon_green, mouse_pos, 15, 2)

    sc.blit(base_img, base_rect)
    text_surface = font.render(f"счет: {score}", True, white)
    text_surface2 = font.render(f"энергия: {energy}", True, white)
    sc.blit(text_surface, (10, 10))
    sc.blit(text_surface2, (100, 10))
    pg.display.flip()
    clock.tick(60)


