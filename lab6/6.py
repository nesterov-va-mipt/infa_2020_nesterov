import pygame
from pygame.draw import *
from random import randint

name = input('Твое имя: ')
if name == '':
    name = 'NoName'

pygame.init()

WIDTH = 1200
HEIGHT = 900
V = 15
T = 100

N = 15

FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:
    def __init__(self, coord, r, v, color):
        self.coord = coord
        self.r = r
        self.v = v
        self.color = color

    def check_click(self, coord):
        return (self.coord[0] - coord[0])**2 + (self.coord[1] - coord[1])**2 <= self.r**2

    def draw(self):
        circle(screen, self.color, tuple(self.coord), self.r)

    def move(self):
        self.coord[0] += self.v[0]
        self.coord[1] += self.v[1]

        if self.coord[0] < self.r:
            self.v[0] = randint(0, V)
        if self.coord[0] > WIDTH - self.r:
            self.v[0] = randint(-V, 0)
        if self.coord[1] < self.r:
            self.v[1] = randint(0, V)
        if self.coord[1] > HEIGHT - self.r:
            self.v[1] = randint(-V, 0)

troll_surf = pygame.transform.scale(pygame.image.load('trollface.png'), (173, 144))
TROLL_R = 75
TROLL_B = 0.01
TROLL_K = 60000

class Troll:
    def __init__(self, coord, v):
        self.coord = coord
        self.v = v
    
    def check_click(self, coord):
        return (self.coord[0] - coord[0])**2 + (self.coord[1] - coord[1])**2 <= TROLL_R**2

    def draw(self):
        global screen
        troll_rect = troll_surf.get_rect(center=(int(self.coord[0]), int(self.coord[1])))
        screen.blit(troll_surf, troll_rect)

    def move(self):
        d2 = (self.coord[0] - cursor_coord[0])**2 + (self.coord[1] - cursor_coord[1])**2
        a = [0, 0]
        a[0] = TROLL_K * (self.coord[0] - cursor_coord[0]) / d2**(3/2)
        a[1] = TROLL_K * (self.coord[1] - cursor_coord[1]) / d2**(3/2)
        
        
        a[0] -= TROLL_B * self.v[0]
        a[1] -= TROLL_B * self.v[1]

        self.v[0] += a[0]
        self.v[1] += a[1]

        self.coord[0] += self.v[0]
        self.coord[1] += self.v[1]

        if self.coord[0] < TROLL_R:
            self.v[0] = randint(0, V)
        if self.coord[0] > WIDTH - TROLL_R:
            self.v[0] = randint(-V, 0)
        if self.coord[1] < TROLL_R:
            self.v[1] = randint(0, V)
        if self.coord[1] > HEIGHT - TROLL_R:
            self.v[1] = randint(-V, 0)

def create_ball():
    r = randint(20, 100)
    return Ball([randint(r, WIDTH - r), randint(r, HEIGHT - r)], r, [randint(-V, V),
        randint(-V, V)], COLORS[randint(0, 5)])


def click(event):
    global balls, score
    new_balls = []
    for ball in balls:
        if ball.check_click(event.pos):
            score += BALL_SCORE
        else:
            new_balls.append(ball)
    if troll.check_click(event.pos):
        score += TROLL_SCORE
        troll.coord = [randint(TROLL_R, WIDTH - TROLL_R), randint(TROLL_R, HEIGHT - TROLL_R)]
    balls = new_balls

def update_record_table():
    f = open('table.txt', 'r')
    lines = f.read().split('\n')
    table = dict()
    for line in lines[1:-1]:
        nick, scr = line.split('\t\t\t\t')
        scr = int(scr)
        table[nick] = scr

    if name in table:
        table[name] = max(table[name], score)
    else:
        table[name] = score

    f.close()
    f = open('table.txt', 'w')
    pairs = [(table[key], key) for key in table]
    pairs.sort()
    pairs.reverse()
    f.write('Name\t\t\tScore\n' + '\n'.join(['{}\t\t\t\t{}'.format(p[1], p[0]) for p in pairs]))
    f.close()

BALL_SCORE = 1
TROLL_SCORE = 100
score = 0

balls = []
for i in range(N):
    balls.append( create_ball() )

troll = Troll([WIDTH // 2, HEIGHT // 2], [randint(0, V // 2), randint(0, V // 2)])
#troll = Troll([WIDTH // 2, HEIGHT // 2], [0, 0])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

cursor_coord = [1000000, 1000000]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            update_record_table()
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
        elif event.type == pygame.MOUSEMOTION:
            cursor_coord = event.pos
    for ball in balls:
        ball.move()
        ball.draw()
    troll.move()
    troll.draw()
    if randint(0, T) == 1:
        balls.pop(randint(0, len(balls) - 1))
    if randint(0, len(balls)) == 0:
        balls.append( create_ball() )
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
