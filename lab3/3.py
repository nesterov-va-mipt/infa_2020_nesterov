import pygame
from pygame.draw import *

pygame.init()

WHITE = (254, 254, 254)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (100, 0, 0)
BLUE = (0, 0, 100)

FPS = 30
screen = pygame.display.set_mode((800, 1200))

def elllipse_with_border(rect, screen):
    ellipse(screen, WHITE, rect)
    ellipse(screen, BLACK, rect, 1)

def bear(x, y, screen):
    # удило
    line(screen, BLACK, (x + 200, y + 150), (x + 250, y + 70), 4)
    line(screen, BLACK, (x + 250, y + 70), (x + 550, y - 230), 4)
    line(screen, BLACK, (x + 550, y - 230), (x + 550, y + 210), 1)
    # бошка
    elllipse_with_border((x + 100, y - 45, 140, 70), screen)
    # туловище
    elllipse_with_border((x, y, 200, 350), screen)
    # жопа
    elllipse_with_border((x + 100, y + 240, 160, 120), screen)
    # нога
    elllipse_with_border((x + 190, y + 340, 100, 30), screen)
    # рука
    elllipse_with_border((x + 165, y + 90, 80, 35), screen)

    # нос
    circle(screen, BLACK, (x + 236, y - 20), 5)
    # моргало
    circle(screen, BLACK, (x + 165, y - 23), 5)
    # пасть
    line(screen, BLACK, (x + 155, y), (x + 225, y))
    arc(screen, BLACK, (x + 190, y - 19, 50, 20), 4.71, 6)

def pool(x, y, screen):
    ellipse(screen, (100, 100, 100), (x, y, 300, 100)) 
    ellipse(screen, BLACK, (x, y, 300, 100), 1)
    ellipse(screen, (0, 100, 100), (x + 30, y + 30, 240, 70)) 
    ellipse(screen, BLACK, (x + 30, y + 30, 240, 70), 1) 

def sun(x, y, screen):
    circle(screen, (160, 255, 255), (x, y), 210)
    circle(screen, (0, 255, 255), (x, y), 170)
    line(screen, (160, 255, 255), (x - 190, y), (x + 190, y), 30)
    line(screen, (160, 255, 255), (x, y + 190), (x, y - 190), 30)

    circle(screen, WHITE, (x, y), 20)
    circle(screen, WHITE, (x + 190, y), 15)
    circle(screen, WHITE, (x, y + 190), 15)
    circle(screen, WHITE, (x - 190, y), 15)
    circle(screen, WHITE, (x, y - 190), 15)

def fish(x, y, screen):
    # хвост
    polygon(screen, GRAY, [(x, y), (x - 50, y - 25), (x - 50, y + 25)]) 
    # тушка
    polygon(screen, GRAY, [(x, y), (x + 75, y - 25), (x + 150, y), (x + 75, y + 25)])
    # плавники
    polygon(screen, RED, [(x + 75, y - 25), (x + 120, y - 9), (x + 100, y - 35), (x +
        60, y - 35)])
    polygon(screen, RED, [(x + 105, y + 15), (x + 110, y + 30), (x + 130, y + 20), (x +
        120, y + 10)])
    polygon(screen, RED, [(x + 45, y + 15), (x + 40, y + 30), (x + 20, y + 20), (x +
        30, y + 10)])
    # глаз
    circle(screen, BLUE, (x + 120, y), 7)
    circle(screen, BLACK, (x + 123, y), 3)
    ellipse(screen, WHITE, (x + 113, y - 2, 7, 4))

def scene(screen):
    pool(450, 700, screen)
    
    surf1 = pygame.Surface((200, 65))
    surf1.fill((255, 255, 255, 0))
    surf1.set_colorkey((255, 255, 255, 0))
    fish(50, 35, surf1)
    screen.blit(pygame.transform.scale(pygame.transform.flip(surf1, True, False),
        (100, 32)), (600, 860))

    surf1 = pygame.Surface((200, 65))
    surf1.fill((255, 255, 255, 0))
    surf1.set_colorkey((255, 255, 255, 0))
    fish(50, 35, surf1)
    screen.blit(pygame.transform.scale(pygame.transform.flip(surf1, False, False),
        (100, 32)), (500, 860))

    surf1 = pygame.Surface((200, 65))
    surf1.fill((255, 255, 255, 0))
    surf1.set_colorkey((255, 255, 255, 0))
    fish(50, 35, surf1)

    screen.blit(pygame.transform.scale(pygame.transform.flip(surf1, False, False),
        (100, 32)), (600, 810))

    surf1 = pygame.Surface((200, 65))
    surf1.fill((255, 255, 255, 0))
    surf1.set_colorkey((255, 255, 255, 0))
    fish(50, 35, surf1)
    screen.blit(pygame.transform.scale(pygame.transform.flip(surf1, True, False),
        (100, 32)), (550, 830))

    surf1 = pygame.Surface((200, 65))
    surf1.fill((255, 255, 255, 0))
    fish(50, 35, surf1)
    screen.blit(pygame.transform.scale(pygame.transform.flip(surf1, True, False),
        (60, 19)), (570, 670))

    surf1 = pygame.Surface((200, 65))
    surf1.fill((255, 255, 255, 0))
    fish(50, 35, surf1)
    screen.blit(pygame.transform.scale(pygame.transform.flip(surf1, True, True),
        (60, 19)), (630, 670))

    surf1 = pygame.Surface((200, 65))
    surf1.fill((255, 255, 255, 0))
    fish(50, 35, surf1)
    screen.blit(pygame.transform.scale(pygame.transform.flip(surf1, False, True),
        (60, 19)), (500, 670))

    bear(100, 550, screen)

# фон
rect(screen, (0, 255, 255), (0, 0, 800, 600))
rect(screen, WHITE, (0, 600, 800, 1200))
# солнце
sun(500, 150, screen)

surf1 = pygame.Surface((800, 1200))
surf1.fill((255, 255, 255, 0))
surf1.set_colorkey((255, 255, 255, 0))
scene(surf1)
screen.blit(pygame.transform.scale(surf1, (300, 450)), (0,700))

surf1 = pygame.Surface((800, 1200))
surf1.fill((255, 255, 255, 0))
surf1.set_colorkey((255, 255, 255, 0))
scene(surf1)
screen.blit(pygame.transform.flip(pygame.transform.scale(surf1, (300, 450)), True,
    False), (200,400))

surf1 = pygame.Surface((800, 1200))
surf1.fill((255, 255, 255, 0))
surf1.set_colorkey((255, 255, 255, 0))
scene(surf1)
screen.blit(pygame.transform.flip(pygame.transform.scale(surf1, (300, 450)), True,
    False), (500,350))

surf1 = pygame.Surface((800, 1200))
surf1.fill((255, 255, 255, 0))
surf1.set_colorkey((255, 255, 255, 0))
scene(surf1)
screen.blit(pygame.transform.flip(pygame.transform.scale(surf1, (600, 900)), True,
    False), (300,500))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
