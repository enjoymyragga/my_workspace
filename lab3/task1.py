import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
gray = (200, 200, 200)
yellow = (255, 255, 0)
red = (255, 0, 0)
screen.fill(gray)
circle(screen, yellow, (200, 200), 100, 0)
circle(screen, red, (150, 180), 25, 0)
circle(screen, (0, 0, 0), (150,180), 12.5, 0)
circle(screen, red, (250, 180), 20, 0)
circle(screen, (0, 0, 0), (250,180), 10, 0)
polygon(screen, (0, 0, 0), [(100, 120), (105, 110),
                            (185, 160), (180, 170)])
polygon(screen, (0, 0, 0), [(220, 170), (215, 160),
                            (295, 130), (300, 140)])
rect(screen, (0, 0, 0), (150, 250, 100, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()