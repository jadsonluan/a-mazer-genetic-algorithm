from enum import Enum

class Direction(Enum):
  LEFT = 0
  TOP = 1
  RIGHT = 2
  BOTTOM = 3

def opposite(direction):
  if direction == Direction.LEFT:
    return Direction.RIGHT
  elif direction == Direction.TOP:
    return Direction.BOTTOM
  elif direction == Direction.RIGHT:
    return Direction.LEFT
  elif direction == Direction.BOTTOM:
    return Direction.TOP
  else:
    return direction

def left_from(position):
  x, y = position
  return (x, y - 1)

def top_from(position):
  x, y = position
  return (x - 1, y)

def right_from(position):
  x, y = position
  return (x, y + 1)

def bottom_from(position):
  x, y = position
  return (x + 1, y)

def get_adjacent(position, direction):
  if direction == Direction.LEFT:
    return left_from(position)
  elif direction == Direction.TOP:
    return top_from(position)
  elif direction == Direction.RIGHT:
    return right_from(position)
  elif direction == Direction.BOTTOM:
    return bottom_from(position)
  else:
    return position