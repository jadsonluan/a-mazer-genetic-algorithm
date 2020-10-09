from random import choice
from .cell import Cell

DOOR = 1
WALL = 0

class Maze:
  def __init__(self, size):
    self.size = size
    self.maze = self.create_maze(size)
    self.entrance = (choice(range(size)), 0)
    self.exit = (choice(range(size)), size - 1)
    self.init()

  def create_maze(self, size):
    maze = []
    for row in range(self.size):
      maze.append([])
      for col in range(self.size):
        maze[row].append(Cell(WALL, WALL, WALL, WALL, 0))
    return maze

  def is_boundary(self, row, col):
    return (row in [0, self.size - 1]) or (col in [0, self.size - 1])

  def init(self):
    for row in range(self.size):
      for col in range(self.size):
        self.update_cell(row, col)

    # FloodFill
    label = 1
    self.floodfill(self.entrance, label)

  def floodfill(self, start, label):
    queue = []
    queue.append(start)
    solved = False
    while queue != [] and not solved:
      r, c = queue.pop(0)
      element = self.maze[r][c]
      element.label = label
      
      # self.printLabels(label)

      if (r,c) == self.exit:
        solved = True
        break

      self.floodfill_step(queue, r, c, label)

    if solved:
      print ("Chegou na solução! 👍")
    else:
      # Rodar o floodfill a partir da saida
      # Se encontrar uma parede comum as duas inundações, quebre-a
      # caso contrário, cria uma porta aleatoria 
      pass

  def floodfill_step(self, queue, row, col, label):
    element = self.maze[row][col]
    if element.left == DOOR and self.maze[row][col-1].label != label:
      queue.append((row, col-1))
    
    if element.top == DOOR and self.maze[row-1][col].label != label:
      queue.append((row-1,col))

    if element.right == DOOR and self.maze[row][col+1].label != label:
      queue.append((row, col+1))

    if element.bottom == DOOR and self.maze[row+1][col].label != label:
      queue.append((row+1, col))

  def printLabels(self, label):
    for row in range(self.size):
      for col in range(self.size):
        result = "🐀" if self.maze[row][col].label == label else "❌"
        if (row, col) == self.entrance:
          result = "👽"
        elif (row, col) == self.exit:
          result = "💎"
        print(result, end=" ")
      print()
    print()

  def left_step(self, row, col):
    create_door = choice([True,False])
    is_boundary = self.is_boundary(row, col)
    if create_door and not (is_boundary and col == 0):
      self.maze[row][col].left = DOOR
      self.maze[row][col-1].right = DOOR

  def top_step(self, row, col):
    create_door = choice([True,False])
    is_boundary = self.is_boundary(row, col)
    if create_door and not (is_boundary and row == 0):
      self.maze[row][col].top = DOOR
      self.maze[row-1][col].bottom = DOOR
    
  def right_step(self, row, col):
    create_door = choice([True,False])
    is_boundary = self.is_boundary(row, col)
    if create_door and not (is_boundary and col == self.size - 1):
      self.maze[row][col].right = DOOR
      self.maze[row][col+1].left = DOOR

  def bottom_step(self, row, col):
    create_door = choice([True,False])
    is_boundary = self.is_boundary(row, col)
    if create_door and not (is_boundary and row == self.size - 1):
      self.maze[row][col].bottom = DOOR
      self.maze[row+1][col].top = DOOR

  def update_cell(self, row, col):
    self.left_step(row, col)
    self.top_step(row, col)
    self.right_step(row, col)
    self.bottom_step(row, col)

  def display(self):
    for row in range(self.size):
      for col in range(self.size):
        print(self.maze[row][col], end="")
      print()
