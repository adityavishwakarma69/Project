from random import randint
import pygame
from pygame.locals import *

pygame.font.init()
FONT = pygame.font.Font(None, 30)

class Screen:
	def __init__(self, width, height, fps = 60):
		self.width = width
		self.height = height

		self.display = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("BUBBLE SORT")
		self.clock = pygame.time.Clock()
		self.fps = fps

	def update(self):
		dt = self.clock.tick(self.fps)
		pygame.display.flip()

		return dt

	def fill(self, color = (0, 0, 0)):
		self.display.fill(color)

	def blitrects(self, rects, color = (255, 255, 255)):
		for rect in rects:
			pygame.draw.rect(self.display, color, rect)

	def text(self, text, rect, color, font):
		self.display.blit(font.render(text, True, color), rect)

def bubblesort(nums):
	for i in range(len(nums)):
		for j in range(0, len(nums) - i - 1):
			if nums[j] > nums[j + 1]:
				nums[j], nums[j + 1] = nums[j + 1], nums[j]


def random_list(low, high, size):
	l = []
	for i in range(size):
		l.append(randint(low, high))

	return l

def crect(nums, surface_width, surface_height):
	r = []
	r_width = surface_width // len(nums)
	hf = surface_height // max(nums)                                      #height factor
	for i in range(len(nums)):
		r.append(pygame.Rect(r_width * i, surface_height - nums[i] * hf, r_width, nums[i] * hf))

	return r

def main():

	nums = random_list(0, 100, 50)
	dt = 0
	time = 0 

	for i in range(len(nums)):
		flag = True
		for j in range(0, len(nums) - i - 1):


			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					exit()

			if nums[j] > nums[j + 1]:
				flag = False
				nums[j], nums[j + 1] = nums[j + 1], nums[j]


			scr.fill((90, 90, 90))

			rects = crect(nums, scr.width, scr.height)

			scr.blitrects(rects)

			pygame.draw.rect(scr.display, (255, 0, 0), rects[j])
			scr.text(str(round(time, 2)), (0, 0, 40, 40), (0, 255, 0), FONT)
			dt = scr.update()
			time += dt/1000
		if flag:
			break

#main

pygame.init()
scr = Screen(800, 600, 60)

main()
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			main()