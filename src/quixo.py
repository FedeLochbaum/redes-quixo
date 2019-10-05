class Quixo:
  def __init__(self):
    self.board = [[Cell(row, column) for row in range(5)] for column in range(5)]

class Cell:
  def __init__(self, row, column):
    self.symbol = "empty"
    self.row = row
    self.column = column

