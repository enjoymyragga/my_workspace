import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1000))
hard_brown = (153, 76, 0)
chocolate = (153, 153, 0)
daily = (102, 178, 255)
border = (204, 255, 229)
orange = (255, 128, 0)
ears = (255, 229, 204)
gray = (192, 192, 192)

rect(screen, hard_brown, [(0,0), (800,500)])
rect(screen, chocolate, [(0,500), (800, 1000)])
rect(screen, border, [(430,30), (360,460)])
rect(screen, daily, [(440,40),(160,130)])
rect(screen, daily, [(620,40),(160,130)])
rect(screen, daily, [(440,190),(160,290)])
rect(screen, daily, [(620,190),(160,290)])
ellipse(screen, orange, [(50,600),(60,100)])
ellipse(screen, orange, [(110,525),(500,200)])
cir

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()