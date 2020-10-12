import pygame
import math
from pygame.locals import *

WALL = 0
DOOR = 1

pygame.init()

SCREEN_SIZE = 600
MAZE_SIZE = 600

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)


class MazeCanvas():
	def __init__(self, entr, ext):
		self.entrance = entr
		self.exit = ext
		self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
		pygame.display.set_caption("A-Mazer Genetic Algorithm")
	
	def get_x_and_y_axis(self, row, col, line_size):
		return [col * line_size, row * line_size]
	
	def draw_entrance(self, line_size):
		row, col = self.entrance
		x, y = self.get_x_and_y_axis(row, col, line_size)
		cell_padding = 5
		pygame.draw.rect(self.screen, COLOR_GREEN, (x + cell_padding, y + cell_padding, line_size - (2 * cell_padding), line_size - (2 * cell_padding)))

	def draw_exit(self, line_size):
		row, col = self.exit
		x, y = self.get_x_and_y_axis(row, col, line_size)
		cell_padding = 5
		pygame.draw.rect(self.screen, COLOR_RED, (x + cell_padding, y + cell_padding, line_size - (2 * cell_padding), line_size - (2 * cell_padding)))

	def draw_cell(self, cell, row, col, line_size):
		x, y = self.get_x_and_y_axis(row, col, line_size)
		top_left_coords_from = (x, y)
		bottom_right_coords_from = (x + line_size - 1, y + line_size - 1)

		left_coords_to = (x, y + line_size - 1)
		right_coords_to = (x + line_size - 1, y)
		top_coords_to = (x + line_size - 1, y)
		bottom_coords_to = (x, y + line_size - 1)

		if (cell.left == WALL):
			pygame.draw.line(self.screen, COLOR_WHITE, top_left_coords_from, left_coords_to)
		if (cell.right == WALL):
			pygame.draw.line(self.screen, COLOR_WHITE, bottom_right_coords_from, right_coords_to)
		if (cell.top == WALL):
			pygame.draw.line(self.screen, COLOR_WHITE, top_left_coords_from, top_coords_to)
		if (cell.bottom == WALL):
			pygame.draw.line(self.screen, COLOR_WHITE, bottom_right_coords_from, bottom_coords_to)
	
	def draw(self, maze):
		line_size = math.floor(MAZE_SIZE / len(maze))
		self.draw_entrance(line_size)
		self.draw_exit(line_size)

		for row in range(len(maze)):
			cells_row = maze[row]
			for col in range(len(cells_row)):
				cell = cells_row[col]
				# self.draw_label()
				self.draw_cell(cell, row, col, line_size)

		pygame.display.flip()
