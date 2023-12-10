import pygame
from pygame.locals import *
from veclib import Vector2d

pygame.init()

screen = pygame.display.set_mode((800, 800))

dt = 0
clock = pygame.time.Clock()
fps = 244

c1pos = Vector2d(360, 200)
c2pos = Vector2d(400, 600)

m1 = 50
m2 = 500

v1 = Vector2d(200, 0)
v2 = Vector2d(0, 200)

g = Vector2d(0, 0)

contact = False

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    v1 = v1 + g * dt
    v2 = v2 + g * dt
    c1pos = c1pos + v1 * dt
    c2pos = c2pos + v2 * dt

    for pos, v in ((c1pos, v1),(c2pos, v2)):
        if pos.x + 40 > 800 or pos.x - 40 < 0:
            v.x = -v.x
        if pos.y + 40 > 800 or pos.y - 40 < 0:
            v.y = -v.y
    
    if (c1pos - c2pos).mag() < 80:
        #v1.x, v2.x = (2 * v2.x + (m1/m2 - 1) * v1.x)/(1 + m1/m2), (2 * v1.x + (m2/m1 - 1) * v2.x)/(1 + m2/m1)
        #v1.y, v2.y = (2 * v2.y + (m1/m2 - 1) * v1.y)/(1 + m1/m2), (2 * v1.y + (m2/m1 - 1) * v2.y)/(1 + m2/m1)
        v1, v2 = (v2 * 2 + v1 * (m1/m2 - 1))/(1 + m1/m2), (v1 * 2 + v2 * (m2/m1 - 1))/(1 + m2/m1)
        print("total kinetic energy : ", 0.5 * ((m1 * v1.mag() ** 2) + (m2 * v2.mag() ** 2)))


    screen.fill((175, 175, 175))  

    pygame.draw.circle(screen, (255, 0, 0), c1pos.astuple(), 40)
    pygame.draw.circle(screen, (0, 0, 0), c1pos.astuple(), 40, 2)
    pygame.draw.line(screen, (0, 0, 0), c1pos.astuple(), (c1pos - Vector2d(-40, v1.dir(), polar = True)).astuple())


    pygame.draw.circle(screen, (0, 0, 255), c2pos.astuple(), 40)
    pygame.draw.circle(screen, (0, 0, 0), c2pos.astuple(), 40, 2)

    pygame.display.flip()
    dt = clock.tick(fps)/1000