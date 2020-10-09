from random import choice
from .cell import Cell
from .directions import Direction, opposite, get_adjacent

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
    print("[🌊] Procurando solução por FloodFill!")
    print("[🌊] Iniciando FloodFill (Entrada => Saida)!")
    solved = self.floodfill(self.entrance, self.exit, label_entrance)

    if solved:
      print("[✅] Saída encontrada! O labirinto possui solução.")
    else:
      print("[❌] Saída não encontrada!")
      print("[🌊] Iniciando FloodFill (Saida => Entrada)!")
      solved = self.floodfill(self.exit, self.entrance, label_exit, second_time=True)

      if solved:
        self.clear_labels()
        self.make_solvable(label_entrance, label_exit)
      else:
        print("[🔨] Busca parede aleatória para quebrar.")
        self.break_random_wall()

  def clear_labels(self):
    for row in range(self.size):
      for col in range(self.size):
        self.cell((row, col)).label = DEFAULT_LABEL

  def break_random_wall(self):
    print("Criando uma porta 🚪 aleatoria!")
    # valid_wall = False
    # while not valid_wall:
    #   position = (choice([0, self.size - 1]), choice([0, self.size - 1]))
    #   if position == self.exit or position == self.entrance:
    #     continue
    
    # element = self.cell()
    # directions = [Direction.LEFT, Direction.TOP, Direction.RIGHT, Direction.BOTTOM]
    # direction = choice(directions)
    # print(element, direction)
        
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
    elif direction == Direction.LEFT:
      return (is_boundary and bottom == self.size - 1)
    else:
      return False

  def floodfill(self, element_position, target_position, label, second_time=False):
    row, col = element_position
    element = self.maze[row][col]

    if element_position == target_position:
      return True
    if element.label == label:
      return False
      
    # element = self.cell(element_position)
    element.label = label
    # self.display(label_only=True)

    # Se for a segunda 'inundação' (flood) e encontrar uma parede que se for quebrada
    # irá conectar a primeira inundação, quebra e retorna True pois achou uma solução.
    if second_time and self.find_and_break_wall(element_position, label):
      return True

    directions = [Direction.LEFT, Direction.TOP, Direction.RIGHT, Direction.BOTTOM]
    result = False

    # Se algum vizinho encontrar a solução
    for direction in directions:
      if element.direction(direction) == DOOR:
        neighbor_position = get_adjacent(element_position, direction)
        if self.floodfill(neighbor_position, target_position, label, second_time):
          return True
    return False

  def find_and_break_wall(self, position, label):
    directions = [Direction.LEFT, Direction.TOP, Direction.RIGHT, Direction.BOTTOM]

    for direction in directions:
      if self.check_side(position, direction, label):
        self.create_door(position, direction)
        print("[🌊] Parede que separa dois 'Floods' encontrada.")
        print("[🚪] Porta criada.")
        return True
    return False

  def check_side(self, position, direction, label):
    is_boundary_wall = self.is_boundary_wall(position, direction)
    has_neighbor = self.has_neighbor(position, direction)

    if is_boundary_wall or not has_neighbor:
      return False

    element = self.cell(position)
    neighbor = self.neighbor(position, direction)
    neighbor_with_flood = (neighbor.label != label and neighbor.label != DEFAULT_LABEL)
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
    directions = [Direction.LEFT, Direction.TOP, Direction.RIGHT, Direction.BOTTOM]

    for direction in directions:
      create_door = choice([True,False])
      is_boundary_wall = self.is_boundary_wall(position, direction)

      if create_door and not is_boundary_wall and self.has_neighbor(position, direction):
        self.cell(position).set_to_direction(direction, DOOR)
        self.neighbor(position, direction).set_to_direction(opposite(direction), DOOR)

  def display(self, label_only=False):
    for row in range(self.size):
      for col in range(self.size):
        print(self.maze[row][col] if not label_only else self.cell((row,col)).label, end=" ")
      print()
