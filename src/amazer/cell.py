class Cell:
  def __init__(self, left, top, right, bottom, label):
    self.left = left
    self.top = top
    self.right = right
    self.bottom = bottom
    self.label = label

  def __str__(self):
    return "[%s / %s,%s,%s,%s]" % (self.label, self.left, self.top, self.right, self.bottom)