# coding: utf-8
from amazer import Maze
from amazer import Cell
from amazer import Direction
from amazer import Ag

DOOR = 1
WALL = 0
LAB = "🔥"

# _________
# | _____ |
# |_|   |_S
# |___| |_|
# |E__|_|_|
# 
non_common_wall_maze = [
  [Cell(WALL,WALL,DOOR,DOOR,LAB),Cell(DOOR,WALL,DOOR,WALL,LAB),Cell(DOOR,WALL,DOOR,WALL,LAB),Cell(DOOR,WALL,WALL,DOOR,LAB)],
  [Cell(WALL,DOOR,WALL,WALL,LAB),Cell(WALL,WALL,DOOR,DOOR,LAB),Cell(DOOR,WALL,WALL,DOOR,LAB),Cell(WALL,DOOR,WALL,WALL,LAB)],
  [Cell(WALL,WALL,DOOR,WALL,LAB),Cell(DOOR,DOOR,WALL,WALL,LAB),Cell(WALL,DOOR,WALL,DOOR,LAB),Cell(WALL,WALL,WALL,WALL,LAB)],
  [Cell(WALL,WALL,DOOR,WALL,LAB),Cell(DOOR,WALL,WALL,WALL,LAB),Cell(WALL,DOOR,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB)]
]

def test_maze_non_shared_wall():
  maze1 = Maze(4)
  maze1.maze = non_common_wall_maze
  maze1.entrance = (3,0)
  maze1.exit = (1,3)

  print("=== Aqui começa a criação do labirinto teste. ===")
  maze1.make_solvable("👽", "👾")

# _________
# |E|____ |
# |_|_|_| |
# |_|_|_| |
# |_|_|_|_S
#
common_wall_maze = [
  [Cell(WALL,WALL,WALL,DOOR,LAB),Cell(WALL,WALL,DOOR,WALL,LAB),Cell(DOOR,WALL,DOOR,WALL,LAB),Cell(DOOR,WALL,WALL,DOOR,LAB),],
  [Cell(WALL,DOOR,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,DOOR,WALL,DOOR,LAB),],
  [Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,DOOR,WALL,DOOR,LAB),],
  [Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,DOOR,WALL,WALL,LAB),]
]

def test_maze_shared_wall():
  maze1 = Maze(4)
  maze1.maze = common_wall_maze
  maze1.entrance = (0,0)
  maze1.exit = (3,3)
  
  print("=== Aqui começa a criação do labirinto teste. ===")
  maze1.make_solvable("👽", "👾")

maze = Maze(10)
# maze.display()
print('entrance', maze.entrance)
print('exit', maze.exit)


print("RESOLVENDO O LABIRINTO")

resolution = Ag(maze, 20, 100)
print(resolution.all_fitness)