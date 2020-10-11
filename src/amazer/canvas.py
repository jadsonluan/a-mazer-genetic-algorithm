import pygame
import math
from pygame.locals import *

WALL = 0
DOOR = 1

pygame.init()

SCREEN_SIZE = 600

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)


class MazeCanvas():
	def __init__(self, maze, entr, ext):
		self.maze = maze
		self.entrance = entr
		self.exit = ext
		self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
		pygame.display.set_caption("A-Mazer Genetic Algorithm")
	
	def draw(self):
		line_size = math.floor(SCREEN_SIZE / len(self.maze))
		for i in range(len(self.maze)):
			row = self.maze[i]
			for j in range(len(row)):
				cell = row[j]

				if (i, j) == self.entrance:
					pygame.draw.rect(self.screen, COLOR_GREEN, (i * line_size + 1, j * line_size + 1, line_size - 1, line_size - 1))
				
				if (i, j) == self.exit:
					pygame.draw.rect(self.screen, COLOR_RED, (i * line_size + 1, j * line_size + 1, line_size - 1, line_size - 1))

				top_left_coords_from = (i * line_size, j * line_size)
				bottom_right_coords_from = (i * line_size + line_size, j * line_size + line_size)

				left_coords_to = (i * line_size, j * line_size + line_size)
				right_coords_to = (i * line_size + line_size, j * line_size)
				top_coords_to = (i * line_size + line_size, j * line_size)
				bottom_coords_to = (i * line_size, j * line_size + line_size)

				if (cell.left == WALL):
					pygame.draw.line(self.screen, COLOR_WHITE, top_left_coords_from, left_coords_to)
				if (cell.right == WALL):
					pygame.draw.line(self.screen, COLOR_WHITE, bottom_right_coords_from, right_coords_to)
				if (cell.top == WALL):
					pygame.draw.line(self.screen, COLOR_WHITE, top_left_coords_from, top_coords_to)
				if (cell.bottom == WALL):
					pygame.draw.line(self.screen, COLOR_WHITE, bottom_right_coords_from, bottom_coords_to)

		pygame.display.flip()
