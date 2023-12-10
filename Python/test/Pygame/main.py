import pygame
from pygame.locals import *

pygame.init()


screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 100) 

text = font.render("Hello, World!", True, (255, 255, 255))
trect = text.get_rect()
trect.center = (250, 250)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

	screen.fill((0, 0, 0))

	screen.blit(text, trect)

	pygame.display.flip()