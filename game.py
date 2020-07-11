import pygame
from pygame.locals import *

# Init pygame, define some constants and global variables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (600, 600) # width & height of the window
background = WHITE

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Balls game")
clock = pygame.time.Clock()

# Main loop
run = True
while run:
	screen.fill(background)
	# Event loop
	for event in pygame.event.get():
		if event.type == QUIT:
			run = False

	# pygame.display.flip()
	clock.tick(30)
	pygame.display.update()

pygame.quit()