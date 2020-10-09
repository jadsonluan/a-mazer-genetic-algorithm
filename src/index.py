# coding: utf-8
from amazer import Maze
from amazer import Cell
from amazer import Direction

DOOR = 1
WALL = 0
LAB = "🔥"

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

non_common_wall_maze = [
  [Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(DOOR,WALL,WALL,WALL,LAB),],
  [Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),],
  [Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),],
  [Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),Cell(WALL,WALL,WALL,WALL,LAB),]
]

maze = Maze(4)
maze.maze = common_wall_maze
maze.entrance = (0,0)
maze.exit = (3,3)
maze.display()
maze.make_solvable("👽", "👾")
maze.display()

# print()
# maze.display(label_only=True)

print('entrance', maze.entrance)
print('exit', maze.exit)