from random import choice
from .cell import Cell
from .directions import Direction, opposite, get_adjacent
from .canvas import MazeCanvas

WALL = 0
DOOR = 1

DEFAULT_LABEL = "🔥"
EMPTY_POSITION = (-1,-1)

class Maze:
  def __init__(self, size):
    self.size = size
    self.maze = self.create_maze(size)
    self.entrance = (choice(range(size)), 0)
    self.exit = (choice(range(size)), size - 1)
    self.canvas = MazeCanvas(self.maze)
    self.init()

  def create_maze(self, size):
    maze = []
    for row in range(self.size):
      maze.append([])
      for col in range(self.size):
        maze[row].append(Cell(WALL, WALL, WALL, WALL, DEFAULT_LABEL))
    return maze

  def is_boundary_cell(self, position):
    row, col = position
    return (row in [0, self.size - 1]) or (col in [0, self.size - 1])

  def init(self):
    for row in range(self.size):
      for col in range(self.size):
        self.randomize_walls((row, col))

    label_entrance = 1
    label_exit = 2
    self.make_solvable(1, 2)
    
  def make_solvable(self, label_entrance, label_exit):
    solved = False
    break_random_wall_from_entrance = True

    while True:
      self.clear_labels()
      print("[🌊] Iniciando FloodFill (Entrada => Saida)!")      
      solved = self.floodfill(self.entrance, self.exit, label_entrance)
      if solved:
        break

      print("[❌] Saída não encontrada!")
      print("[🌊] Iniciando FloodFill (Saida => Entrada)!")
      solved = self.floodfill(self.exit, self.entrance, label_exit, target_label=label_entrance)
      if solved:
        continue

      print("[❌] Saída não encontrada!")
      self.clear_labels()

      if break_random_wall_from_entrance:
        print("[🌊] Iniciando FloodFill (Entrada => Espaço vazio)!")
        self.floodfill(self.entrance, self.exit, label_entrance, target_label=DEFAULT_LABEL)
      else:
        print("[🌊] Iniciando FloodFill (Saída => Espaço vazio)!")
        self.floodfill(self.exit, self.entrance, label_exit, target_label=DEFAULT_LABEL)
      break_random_wall_from_entrance = not break_random_wall_from_entrance
    print("[✅] Saída encontrada! O labirinto possui solução.")

  def clear_labels(self):
    for row in range(self.size):
      for col in range(self.size):
        self.cell((row, col)).label = DEFAULT_LABEL
        
  def cell(self, position):
    row, col = position
    return self.maze[row][col]
  
  def neighbor(self, position, direction):
    neighbor_position = get_adjacent(position, direction)
    return self.cell(neighbor_position)

  def is_boundary_wall(self, position, direction):
    row, col = position
    is_boundary = self.is_boundary_cell((row, col))
    if direction == Direction.LEFT:
      return (is_boundary and col == 0)
    elif direction == Direction.TOP:
      return (is_boundary and row == 0)
    elif direction == Direction.RIGHT:
      return (is_boundary and col == self.size - 1)
    elif direction == Direction.BOTTOM:
      return (is_boundary and row == self.size - 1)
    else: 
      return False

  def floodfill(self, element_position, target_position, label, target_label=None):
    row, col = element_position
    element = self.maze[row][col]

    if element_position == target_position:
      return True
    if element.label == label:
      return False
      
    element.label = label
    self.display(label_only=True)
    print()

    # Se o target_label não for None, então estamos procurando uma label especifica encostada
    # em uma parede. Quando encontramos ela, quebramos essa parede. A label pode ser a usada
    # para o 'flood' da saída ou também uma celula vazia (quando não houver flood da saída proximo)
    if target_label is not None and self.find_and_break_wall(element_position, label, target_label):
      return True

    directions = [Direction.RIGHT, Direction.TOP, Direction.BOTTOM, Direction.LEFT]
    result = False

    # Se algum vizinho encontrar a solução
    for direction in directions:
      if element.direction(direction) == DOOR:
        neighbor_position = get_adjacent(element_position, direction)
        if self.floodfill(neighbor_position, target_position, label, target_label):
          return True
    return False

  def find_and_break_wall(self, position, label, target_label):
    directions = [Direction.RIGHT, Direction.LEFT, Direction.TOP, Direction.BOTTOM]

    for direction in directions:
      if self.check_side(position, direction, label, target_label):
        self.create_door(position, direction)
        print("[🚪] Porta criada em %s na direção %s." % (position, direction))
        return True
    return False

  def check_side(self, position, direction, label, target_label):
    is_boundary_wall = self.is_boundary_wall(position, direction)
    has_neighbor = self.has_neighbor(position, direction)

    if is_boundary_wall or not has_neighbor:
      return False

    element = self.cell(position)
    neighbor = self.neighbor(position, direction)
    neighbor_with_flood = (neighbor.label == target_label)
    wall_between_neighbor = element.direction(direction) == WALL

    return wall_between_neighbor and neighbor_with_flood

  def create_door(self, position, direction):
    if self.has_neighbor(position, direction):
      element = self.cell(position)
      neighbor = self.neighbor(position, direction)
      opposite_direction = opposite(direction)

      element.set_to_direction(direction, DOOR)
      neighbor.set_to_direction(opposite_direction, DOOR)
      return True
    return False

  def has_neighbor(self, position, direction):
    neighbor_position = get_adjacent(position, direction)
    row, col = neighbor_position
    return (row >= 0 and row < self.size) and (col >= 0 and col < self.size)

  def randomize_walls(self, position):
    directions = [Direction.RIGHT, Direction.LEFT, Direction.TOP, Direction.BOTTOM]

    for direction in directions:
      create_door = choice([True,False,False])
      is_boundary_wall = self.is_boundary_wall(position, direction)

      if create_door and not is_boundary_wall and self.has_neighbor(position, direction):
        self.create_door(position, direction)

  def display(self):
    while True:
      self.canvas.draw()
