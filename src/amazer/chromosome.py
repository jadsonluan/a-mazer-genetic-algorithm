from random import choice, choices

class Chromosome:
  def __init__(self, directions, fitness):
    self.directions = directions
    self.fitness = fitness