from matplotlib import pyplot
from statistics import median, mean
from .plot_model import PlotModel

class FitnessPlot():
    def __init__(self, fitnesses):
        self.fitnesses = fitnesses

    def get_fitnesses_means(self):
        means = []
        for generation_fitnesses in self.fitnesses:
            generation_fitnesses_mean = mean(generation_fitnesses)
            means.append(generation_fitnesses_mean)
        return means
    
    def get_fitnesses_medians(self):
        medians = []
        for generation_fitnesses in self.fitnesses:
            generation_fitnesses_median = median(generation_fitnesses)
            medians.append(generation_fitnesses_median)
        return medians
    
    def plot(self, model):
        data = []
        if model === PlotModel.MEAN:
            data = self.get_fitnesses_means()
        elif model === PlotModel.MEDIAN:
            data = self.get_fitnesses_medians()
        else:
            raise Exception("Plot model required: 'MEDIAN' or 'MEAN'")
