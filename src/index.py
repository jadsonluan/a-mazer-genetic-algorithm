# coding: utf-8
from amazer import Maze, Cell, Direction, Ag, MazeCanvas
from plot import FitnessPlot, PlotModel

maze = Maze(10)

print('entrance', maze.entrance)
print('exit', maze.exit)

print("RESOLVENDO O LABIRINTO")
# paramêtros ==> Ag(labirinto, tamanho inicial do cromossomo, tamanho da população, número máximo de gerações, número de elementos a sofrer mutação)
resolution = Ag(maze, 20, 100, 30, 10)

# geração do gráfico a partir dos fitnesses
fitness_plot = FitnessPlot(resolution.all_fitness)
fitness_plot.plot(PlotModel.MEDIAN)

best_solution = None

# encontrando a melhor solução descoberta pelo algoritmo
for solution in resolution.all_solutions:
  if best_solution is None or len(best_solution) > len(solution):
    best_solution = solution

# exibindo melhor solução
if best_solution is not None:
  print(best_solution)
  maze.draw_solution(best_solution)
