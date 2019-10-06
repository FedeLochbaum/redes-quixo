BORDER_INDEXES = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                  (1, 4), (2, 4), (3, 4), (4, 4),
                  (4, 3), (4, 2), (4, 1), (4, 0),
                  (3, 0), (2, 0), (1, 0)]

class Quixo:
  def __init__(self):
    self.board = [[Cell(row, column) for row in range(5)] for column in range(5)]

  def valid_borders(self, player):
    filter(lambda cell: cell.is_valid_border(player), map(lambda t: self.board[t[0]][t[1]], BORDER_INDEXES))

  def all_valid_moves(self, player):
    [move for cell in self.valid_borders(player) for move in self.valid_moves_for_cell(cell)]

  def valid_moves_for_cell(self, cell):
    possible_movements = [(cell.row, 4), (cell.row, 0), (4, cell.column), (0, cell.column)]
    filter(lambda t: t != (cell.row, cell.column), possible_movements)

  def apply_move(self, player, move):
    current_pos = BORDER_INDEXES[move[0]]
    self.board[current_pos[0]][current_pos[1]].update_symbol(player)

    if(self.should_move_row(move)):
      self.move_row(move)
    else:
      self.move_column(move)
  
  def should_move_row(self, move):
    target_row = BORDER_INDEXES[move[0]][0]
    future_row = BORDER_INDEXES[move[1]][0]
    target_row == future_row

  def should_move_row_from_left(self, move):
    BORDER_INDEXES[move[1]][1] == 0 # if the future column is 0, should move in this direction -> 

  def should_move_column_from_top(self, move):
    BORDER_INDEXES[move[1]][0] == 0 # if the future row is 0, should move from top to bottom

  def move_row(self, move):
    if(self.should_move_row_from_left(move)):
      self.move_row_from_left(move)
    else:
      self.move_row_from_right(move)

  def move_column(self, move):
    if(self.should_move_column_from_top(move)):
      self.move_column_from_top(move)
    else:
      self.move_column_from_bottom(move)

  def move_row_from_left(self, move):
    self.move_row_to_direction(move, -1)

  def move_row_from_right(self, move):
    self.move_row_to_direction(move, +1)

  def move_column_from_top(self, move):
    self.move_column_to_direction(move, -1)

  def move_column_from_bottom(self, move):
    self.move_column_to_direction(move, +1)

  def move_row_to_direction(self, move, direction): # direction = +1 | -1 
    # +1 = to right
    # -1 = to left
    current_pos = BORDER_INDEXES[move[0]]
    to_move_pos = BORDER_INDEXES[move[1]]

    while(current_pos != to_move_pos):
      x, y = current_pos
      current_cell = self.board[x][y]
      to_swap_cell = self.board[x][y + direction]
      current_cell.update_pos(x, y + direction)
      to_swap_cell.update_pos(x, y)
      self.board[x][y] = to_swap_cell
      self.board[x][y + direction] = current_cell
      to_swap_cell = (x, y + direction)

  def move_column_to_direction(self, move, direction): # direction = +1 | -1 
    # +1 = to bottom
    # -1 = to top

    current_pos = BORDER_INDEXES[move[0]]
    to_move_pos = BORDER_INDEXES[move[1]]

    while(current_pos != to_move_pos):
      x, y = current_pos
      current_cell = self.board[x][y]
      to_swap_cell = self.board[x + direction][y]
      current_cell.update_pos(x + direction, y)
      to_swap_cell.update_pos(x, y)
      self.board[x][y] = to_swap_cell
      self.board[x + direction][y] = current_cell
      to_swap_cell = (x + direction, y)

class Cell:
  def __init__(self, row, column):
    self.symbol = 'empty'
    self.row = row
    self.column = column

  def update_symbol(self, player):
    self.symbol = player

  def index(self):
    if (self.row, self.column) in BORDER_INDEXES:
      return BORDER_INDEXES.index((self.row, self.column))
    None

  def is_valid_border(self, player):
    self.symbol == 'empty' or self.symbol == player
