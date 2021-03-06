from matplotlib import pyplot
from statistics import median, mean
from math import inf
from .plot_model import PlotModel


class FitnessPlot:
  def __init__(self, fitnesses):
    self.fitnesses = fitnesses
    self.remove_infinite_values()
  
  def remove_infinite_values(self):
    for index in range(len(self.fitnesses)):
      generation_fitnesses = self.fitnesses[index]
      generation_fitnesses = [x if x != inf else 1000 for x in generation_fitnesses]
      self.fitnesses[index] = generation_fitnesses

  """
  Returns the statistical value for the population fitnesses, given the model.
  If model is "MEAN", it returns the mean of the popoulation fitnesses.
  If model is "MEDIAN", it returns the median of the popoulation fitnesses.
  """
  def calculate_population_fitnesses(self, model):
    results = []
    calc_function = None
    if model == PlotModel.MEAN:
      calc_function = mean
    elif model == PlotModel.MEDIAN:
      calc_function = median
    else:
      raise Exception("Plot model required: 'MEDIAN' or 'MEAN'")

    for generation_fitnesses in self.fitnesses:
      generation_statistical_value = calc_function(generation_fitnesses)
      results.append(generation_statistical_value)

    return results

  """
  Generates a graph of a-maze solver generations vs. population fitness
  """
  def plot(self, model):
    fitnesses = self.calculate_population_fitnesses(model)
    generations = range(1, len(fitnesses) + 1)

    data_dict = {"generations": generations, "fitnesses": fitnesses}

    pyplot.plot(
      "generations",
      "fitnesses",
      data=data_dict,
      color="green",
      marker="o",
      label="generations vs fitnesses",
    )
    pyplot.xticks(generations)
    pyplot.yticks(fitnesses)
    pyplot.show()
