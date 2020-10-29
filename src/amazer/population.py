from random import choice, choices
from .chromosome import Chromosome

directions_base = [0, 1, 2, 3]

class Population:
  def __init__(self, chromosome_size, number_chromosomes, initial_fitness):
    self.find_result = False
    self.initial_fitness = initial_fitness
    self.chromosomes = self.inicialization(chromosome_size, number_chromosomes)
  
  def inicialization(self, chromosome_size, number_chromosomes):
    directions = directions_base
    result = []
    for a in range(number_chromosomes):
      result.append(Chromosome(choices(directions, k = chromosome_size), self.initial_fitness))
    return result

  def get_fitness(self):
    result = []
    for i in self.chromosomes:
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

  def generate_population(self):
    
    result = []
    parent_with_weight = choices(self.chromosomes, weights=self.get_fitness(), k=len(self.chromosomes))
    index = len(self.chromosomes)

    #caso o tamanho da população seja ímpar
    if(len(self.chromosomes)/2) != 0:
      index -= 1
      self.odd_children(parent_with_weight, result)

    for i in range(0, index, 2):
      self.crossover(i, result, parent_with_weight)
    
    # setando a nova população
    self.chromosomes = result
    self.find_result = False
    return result

  def odd_children(self, parent_with_weight, result):
    parent1 = parent_with_weight[choice(range(len(self.chromosomes)))].directions
    parent2 = parent_with_weight[choice(range(len(self.chromosomes)))].directions
    child = Chromosome(self.change_half(parent1, parent2), self.initial_fitness)
    result.append(child)

  def crossover(self, i, result, parent_with_weight):
    parent1 = parent_with_weight[i].directions
    parent2 = parent_with_weight[i+1].directions
    # criando dois novos filhos
    child1 = Chromosome(self.change_half(parent1, parent2), self.initial_fitness)
    child2 = Chromosome(self.change_half(parent2, parent1), self.initial_fitness)
    # aumentando o tamanho do cromossomo
    child1.directions.append(choice(directions_base))
    child2.directions.append(choice(directions_base))
    # adicionando os filhos à nova população
    result.append(child1)
    result.append(child2)

  def make_mutation(self, rate):
    options = [True, False]
    rates = [rate, 100-rate]
    
    for i in range(len(self.chromosomes)):
      if(choices(options, weights=rates, k=1)[0]):
        direction = choice(range(len(self.chromosomes[i].directions)))
        change = choice(directions_base)
        self.chromosomes[i].directions[direction] = change


  def sum_chromosome(self, parent1, parent2):
    result = []
    for i in range(len(parent1)):
      sum = (parent1[i] + parent2[i]) % 4
      result.append(sum)
    return result
  
  def sub_chromosome(self, parent1, parent2):
    result = []
    for i in range(len(parent1)):
      sub = (parent1[i] - parent2[i]) % 4
      result.append(sub)
    return result
  
  def change_half(self, parent1, parent2):
    length = int(len(parent1)/2)
    result = parent1[0:length] + parent2[length:len(parent1)]
    return result
  
  def result_found(self):
    self.find_result = True
    return True