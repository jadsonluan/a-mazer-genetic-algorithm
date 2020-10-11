from random import choice, choices
from .chromosome import Chromosome

class Population:
  def __init__(self, chromosome_size, number_chromosomes):
    self.chromosomes = self.inicialization(chromosome_size, number_chromosomes)
    self.find_result = False
  
  def inicialization(self, chromosome_size, number_chromosomes):
    directions = [0, 1, 2, 3]
    result = []
    
    for a in range(number_chromosomes):
      # parametrizar o valor inicial do fitness
      result.append(Chromosome(choices(directions, k = chromosome_size), 100))
    
    return result

  def get_fitness(self):
    result = []
    for i in self.population_sorted():
      result.append(i.fitness)
    return sorted(result)
    
  def get_directions(self):
    result = []
    for i in self.population_sorted():
      result.append(i.directions)
    return sorted(result)
  
  def change_fitness(self, index, value):
    self.chromosomes[index].fitness = value
  
  def population_sorted(self):
    result = sorted(self.chromosomes, key=lambda chromosome: chromosome.fitness)
    self.chromosomes = result
    return result

  def genarate_population(self):
    #tamanho da população deve ser par
    result = []
    for i in range(0, len(self.chromosomes), 2):
      parent1 = self.chromosomes[i].directions
      parent2 = self.chromosomes[i+1].directions
      child1 = Chromosome(self.change_half(parent1, parent2), 100)
      child2 = Chromosome(self.change_half(parent2, parent1), 100)
      result.append(child1)
      result.append(child2)
    self.chromosomes = result
    self.find_result = False
    return result

  def make_mutation(self, rate):
    for i in range(rate):
      chromosome_index = choice(range(len(self.chromosomes)))
      direction = choice(range(len(self.chromosomes[chromosome_index].directions)))
      change = choice([0, 1, 2, 3])
      self.chromosomes[chromosome_index].directions[direction] = change


  def sum_chromosome(self, parent1, parent2):
    result = []
    for i in range(len(parent1)):
      sum = (parent1[i] + parent2[i]) % 4
      result.append(sum)
    result.append(choice([0, 1, 2, 3]))
    result.append(choice([0, 1, 2, 3]))
    return result
  
  def sub_chromosome(self, parent1, parent2):
    result = []
    for i in range(len(parent1)):
      sub = (parent1[i] - parent2[i]) % 4
      result.append(sub)
    result.append(choice([0, 1, 2, 3]))
    result.append(choice([0, 1, 2, 3]))
    return result
  
  def change_half(self, parent1, parent2):
    length = int(len(parent1)/2)
    result = parent1[0:length] + parent2[length:len(parent1)]
    result.append(choice([0, 1, 2, 3]))
    result.append(choice([0, 1, 2, 3]))
    return result
  
  def result_found(self):
    self.find_result = True
    return True