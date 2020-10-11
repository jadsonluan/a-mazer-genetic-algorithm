from random import choice, choices
from math import sqrt
from .cell import Cell
from .maze import Maze
from .directions import Direction, opposite, get_adjacent
from .population import Population


WALL = 0
DOOR = 1

LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3

class Ag:
  def __init__(self, maze, chromosome_size, number_chromosomes):
    self.maze = maze
    self.population = Population(chromosome_size, number_chromosomes)
    self.init()
  
  def init(self):
    generations = 0

    while (0 not in self.population.get_fitness()) and (generations < 10):
      self.evaluation()
      generations += 1
      print(self.population.get_directions())
      print()
      print("---- GERANDO OUTRA POPULAÇÃO ----")
      print()
      self.population.genarate_population()
    print("numero de gerações geradas", generations)

  def evaluation(self):
    solutions = 0
    for i in range(len(self.population.chromosomes)) :
      actualRow, actualCol = self.run_maze(i, self.maze.entrance)
        
      solutions = self.update_fitness(actualRow, actualCol, i, solutions)

    print(solutions)
    if(0 in self.population.get_fitness()):
      print("Encontramos a saída")
    else:
      print("Não encontramos a saída")

  def update_fitness(self, actualRow, actualCol, i, solutions):
    fitness = sqrt((actualRow - self.maze.exit[0])**2 + (actualCol - self.maze.exit[1])**2)
    self.population.change_fitness(i, fitness)
    if(actualRow, actualCol) == self.maze.exit:
      # cromossomo chegou na saída
      print(self.population.chromosomes[i].directions)
      solutions += 1
    return solutions

  def run_maze(self, i, entrance):
    actualRow, actualCol = entrance
    for direction in self.population.chromosomes[i].directions:
      if direction == LEFT:
        if self.maze.maze[actualRow][actualCol].left == DOOR:
          actualRow, actualCol = get_adjacent((actualRow, actualCol), Direction.LEFT)
      elif direction == TOP:
        if self.maze.maze[actualRow][actualCol].top == DOOR:
          actualRow, actualCol = get_adjacent((actualRow, actualCol), Direction.TOP)
      elif direction == RIGHT:
        if self.maze.maze[actualRow][actualCol].right == DOOR:
          actualRow, actualCol = get_adjacent((actualRow, actualCol), Direction.RIGHT)
      elif direction == BOTTOM:
        if self.maze.maze[actualRow][actualCol].left == BOTTOM:
          actualRow, actualCol = get_adjacent((actualRow, actualCol), Direction.BOTTOM)
    return actualRow, actualCol
