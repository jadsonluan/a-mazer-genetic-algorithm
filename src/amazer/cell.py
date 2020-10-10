from .directions import Direction

class Cell:
  def __init__(self, left, top, right, bottom, label=0):
    self.left = left
    self.top = top
    self.right = right
    self.bottom = bottom
    self.label = label

  def direction(self, direction):
    if direction == Direction.LEFT:
      return self.left
    elif direction == Direction.TOP:
      return self.top
    elif direction == Direction.RIGHT:
      return self.right
    elif direction == Direction.BOTTOM:
      return self.bottom
    return ''

  def set_to_direction(self, direction, value):
    if direction == Direction.LEFT:
      self.left = value
    elif direction == Direction.TOP:
      self.top = value
    elif direction == Direction.RIGHT:
      self.right = value
    elif direction == Direction.BOTTOM:
      self.bottom = value

  def __str__(self):
    return "[%s / %s,%s,%s,%s]" % (self.label, self.left, self.top, self.right, self.bottom)