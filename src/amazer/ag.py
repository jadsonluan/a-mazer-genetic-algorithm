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
  def __init__(self, maze, chromosome_size, number_chromosomes, max_generation, mutation_rate):
    self.maze = maze
    self.population = Population(chromosome_size, number_chromosomes, maze.size**2)
    self.all_fitness = []
    self.all_solutions = []
    self.init(max_generation, mutation_rate)
  
  def init(self, max_generation, mutation_rate):
    generations = 0

    for a in range(max_generation):
      self.evaluation()
      generations += 1
      self.population.population_sorted()
      self.all_fitness.append(self.population.get_fitness())
     
      if self.population.find_result:
        break
      print()
      print("GERANDO OUTRA POPULAÇÃO ...")
      print()
      self.population.generate_population()
      self.population.make_mutation(mutation_rate)
    
    print("As soluções encontradas foram:")
    print(self.all_solutions)
    print("Numero de gerações geradas:", generations)
    

  def evaluation(self):
    solutions = 0
    for i in range(len(self.population.chromosomes)) :
      actualRow, actualCol = self.run_maze(i, self.maze.entrance)
        
      solutions = self.update_fitness(actualRow, actualCol, i, solutions)

    print("Número de soluções geradas:", solutions)
    if(0 in self.population.get_fitness()):
      self.population.result_found()
      print("Encontramos a saída")
    else:
      print("Não encontramos a saída")

  def update_fitness(self, actualRow, actualCol, i, solutions):
    fitness = sqrt((actualRow - self.maze.exit[0])**2 + (actualCol - self.maze.exit[1])**2)
    self.population.change_fitness(i, fitness)
    if(actualRow, actualCol) == self.maze.exit:
      # cromossomo chegou na saída
      self.all_solutions.append(self.population.chromosomes[i].directions)
      solutions += 1
    return solutions

  def run_maze(self, i, entrance):
    actualRow, actualCol = entrance
    base = [Direction.LEFT, Direction.TOP, Direction.RIGHT, Direction.BOTTOM]
    for direction in self.population.chromosomes[i].directions:
      if self.maze.maze[actualRow][actualCol].direction(base[direction]) == DOOR:
        actualRow, actualCol = get_adjacent((actualRow, actualCol), base[direction])
    return actualRow, actualCol
