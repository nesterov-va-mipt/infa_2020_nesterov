import pygame
from pygame.draw import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (100, 0, 0)

FPS = 30
screen = pygame.display.set_mode((800, 1200))

def elllipse_with_border(rect):
    ellipse(screen, WHITE, rect)
    ellipse(screen, BLACK, rect, 1)

def bear(x, y):
    # бошка
    elllipse_with_border((x + 100, y - 45, 140, 70))
    # туловище
    elllipse_with_border((x, y, 200, 350))
    # жопа
    elllipse_with_border((x + 100, y + 240, 160, 120))
    # нога
    elllipse_with_border((x + 190, y + 340, 100, 30))
    # рука
    elllipse_with_border((x + 165, y + 90, 80, 35))

    # нос
    circle(screen, BLACK, (x + 236, y - 20), 5)
    # моргало
    circle(screen, BLACK, (x + 165, y - 23), 5)
    # пасть
    line(screen, BLACK, (x + 155, y), (x + 225, y))
    arc(screen, BLACK, (x + 190, y - 19, 50, 20), 4.71, 6)
    # уши


def pool(x, y):
    ellipse(screen, (100, 100, 100), (x, y, 300, 100)) 
    ellipse(screen, BLACK, (x, y, 300, 100), 1)
    ellipse(screen, (0, 100, 100), (x + 30, y + 30, 240, 70)) 
    ellipse(screen, BLACK, (x + 30, y + 30, 240, 70), 1) 

def sun(x, y):
    circle(screen, (160, 255, 255), (x, y), 210)
    circle(screen, (0, 255, 255), (x, y), 170)
    line(screen, (160, 255, 255), (x - 190, y), (x + 190, y), 30)
    line(screen, (160, 255, 255), (x, y + 190), (x, y - 190), 30)

    circle(screen, WHITE, (x, y), 20)
    circle(screen, WHITE, (x + 190, y), 15)
    circle(screen, WHITE, (x, y + 190), 15)
    circle(screen, WHITE, (x - 190, y), 15)
    circle(screen, WHITE, (x, y - 190), 15)

def fish(x, y, angle):
    polygon(screen, GRAY, [(x, y), (x - 50, y - 25), (x - 50, y + 25)]) 
    polygon(screen, GRAY, [(x, y), (x + 75, y - 25), (x + 150, y), (x + 75, y + 25)])
    polygon(screen, RED, [(x + 75, y - 25), (x + 120, y - 9), (x + 100, y - 35), (x +
        60, y - 35)])
    polygon(screen, RED, [(x + 100, y + 16), (x + 110, y + 15), (x + 100, y + 20), (x +
        110, y + 27)])


rect(screen, (0, 255, 255), (0, 0, 800, 600))
rect(screen, WHITE, (0, 600, 800, 1200))

sun(500, 150)
pool(450, 700)

# удило
line(screen, BLACK, (300, 700), (350, 620), 4)
line(screen, BLACK, (350, 620), (650, 320), 4)
line(screen, BLACK, (650, 320), (650, 760), 1)

fish(600, 900, 0)

bear(100, 550)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
