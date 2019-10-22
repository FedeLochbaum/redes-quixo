from copy import deepcopy
from math import inf
import timeit
import random

## QUIXO GAME
##

BORDER_INDEXES = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                  (1, 4), (2, 4), (3, 4), (4, 4),
                  (4, 3), (4, 2), (4, 1), (4, 0),
                  (3, 0), (2, 0), (1, 0)]

class Game:
  def __init__(self):
    self.board = [[Cell(row, column) for column in range(5)] for row in range(5)]
    self.stack_of_moves = []

  def valid_borders(self, player):
    return list(filter(lambda cell: cell.is_valid_target(player), map(lambda t: self.board[t[0]][t[1]], BORDER_INDEXES)))

  def all_valid_targets(self, player):
    return list(map(lambda cell: cell.index(), self.valid_borders(player)))

  def all_valid_moves(self, player):
    return [move for cell in self.valid_borders(player) for move in self.valid_moves_for_cell(cell)]

  def game_over(self, player = None):
    return self.won_in_any_row(player) or self.won_in_any_column(player) or self.won_in_left_diagonal(player) or self.won_in_right_diagonal(player)

  def won_in_any_row(self, player = None):
    return any(map(lambda row: all_the_same_elements(to_simplify(row), player), self.board))

  def won_in_any_column(self, player = None):
    return any(map(lambda column: all_the_same_elements(to_simplify(column), player), self.columns()))

  def won_in_left_diagonal(self, player = None):
    return all_the_same_elements(to_simplify(self.left_diagonal()), player)

  def won_in_right_diagonal(self, player = None):
    return all_the_same_elements(to_simplify(self.right_diagonal()), player)

  def columns(self):
    return [[self.board[j][i] for j in range(5)] for i in range(5)]

  def left_diagonal(self):
    # starting at lower left corner
    return [self.board[4 - i][i] for i in range(5)]

  def right_diagonal(self):
    # starting at upper left corner
    return [self.board[i][i] for i in range(5)]

  def valid_moves_for_cell(self, cell):
    possible_movements = [
      (cell.index(), BORDER_INDEXES.index((cell.row, 4))),
      (cell.index(), BORDER_INDEXES.index((cell.row, 0))), 
      (cell.index(), BORDER_INDEXES.index((0, cell.column))),
      (cell.index(), BORDER_INDEXES.index((4, cell.column)))]

    return list(filter(lambda move: move[1] != cell.index(), possible_movements))

  def apply_move(self, player, move):
    current_pos = BORDER_INDEXES[move[0]]
    self.board[current_pos[0]][current_pos[1]].update_symbol(player)
    # Missing do a checking if the move is valid
    self.stack_of_moves.append(move)

    if(self.should_move_row(move)):
      self.move_row(move)
    else:
      self.move_column(move)

  def should_move_row(self, move):
    target_row = BORDER_INDEXES[move[0]][0]
    future_row = BORDER_INDEXES[move[1]][0]
    return target_row == future_row

  def should_move_row_from_left(self, move):
    return BORDER_INDEXES[move[1]][1] == 0 # if the future column is 0, should move in this direction -> 

  def should_move_column_from_top(self, move):
    return BORDER_INDEXES[move[1]][0] == 0 # if the future row is 0, should move from top to bottom

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
      current_cell_symbol = current_cell.symbol
      current_cell.update_symbol(to_swap_cell.symbol)
      to_swap_cell.update_symbol(current_cell_symbol)
      current_pos = (x, y + direction)

  def move_column_to_direction(self, move, direction): # direction = +1 | -1 
    # +1 = to bottom
    # -1 = to top

    current_pos = BORDER_INDEXES[move[0]]
    to_move_pos = BORDER_INDEXES[move[1]]

    while(current_pos != to_move_pos):
      x, y = current_pos
      current_cell = self.board[x][y]
      to_swap_cell = self.board[x + direction][y]
      current_cell_symbol = current_cell.symbol
      current_cell.update_symbol(to_swap_cell.symbol)
      to_swap_cell.update_symbol(current_cell_symbol)
      current_pos = (x + direction, y)

  def show(self):
    print('\n')
    print('---------------------')
    for row in self.board:
      [print('|', cell.symbol_to_show(), '', end = '') for cell in row ]
      print('|', end = '')
      print('')
    print('---------------------')
    

class Cell:
  def __init__(self, row, column):
    self.symbol = 'empty'
    self.row = row
    self.column = column

  def update_symbol(self, player):
    self.symbol = player

  def symbol_to_show(self):
    if self.symbol == 'empty':
      return 'W'
    return self.symbol

  def update_pos(self, row, column):
    self.row = row
    self.column = column

  def index(self):
    if (self.row, self.column) in BORDER_INDEXES:
      return BORDER_INDEXES.index((self.row, self.column))
    None

  def is_valid_target(self, player):
    return self.symbol == 'empty' or self.symbol == player


def all_the_same_elements(elements, player = None):
  return all(x == y and x != 'W' and y != 'W' for x, y in zip(elements, elements[1:])) if(player == None) else all(x == y and x == player and y == player for x, y in zip(elements, elements[1:]))

def to_simple_structure(game):
  return list(map(lambda row: to_simplify(row), game.board))

def to_simplify(elems):
  return list(map(lambda cell: cell.symbol_to_show(), elems))

## HEURISTIC
##

strategic_points = [(0, 0), (0, 4), (4, 4), (4, 0), (0, 2), (2, 4), (4, 2), (2, 0)]

def count_of_tokens(game):
  res = (0, 0)
  for i_row in range(len(game.board)):
    for i_column in range(len(game.board[i_row])):
      value = game.board[i_row][i_column].symbol_to_show()
      if(value == 'X'):
        res = (res[0] + 1, res[1])

      if(value == 'O'):
        res = (res[0], res[1] + 1)
  return res

def count_of_strategic_points(game, player):
  return sum(map(lambda pair: 1 if game.board[pair[0]][pair[1]].symbol_to_show() == player else 0, strategic_points), 0)

def in_center(game, player):
  return game.board[2][2].symbol_to_show() == player

def max_count_of_neighbors_in_rows(game, player):
  return max([count_of_neighbors(row, player) for row in game.board])

def max_count_of_neighbors_in_columns(game, player):
  return max([count_of_neighbors(column, player) for column in game.columns()])

def max_count_of_neighbors_in_diagonals(game, player):
  return max([count_of_neighbors(game.left_diagonal(), player), count_of_neighbors(game.right_diagonal(), player)])

def max_count_of_neighbors(game, player):
  mconir = max_count_of_neighbors_in_rows(game, player)
  mconic = max_count_of_neighbors_in_columns(game, player)
  mconid = max_count_of_neighbors_in_diagonals(game, player)
  return max([mconir, mconic, mconid])

def heuristic_1(game, player = 'X', oponent = 'O'):
  player_index = 0 if player == 'X' else 1
  oponent_index = 1 if player_index == 0 else 0

  cot = count_of_tokens(game)
  count_of_tokens_value = (cot[player_index] - cot[oponent_index]) * 1.2 # I think that this value has 20% more importance
  cosp = count_of_strategic_points(game, player)
  center_importance = 16 * (1 if in_center(game, player) else 0)
  return count_of_tokens_value + center_importance + max_count_of_neighbors(game, player) * max(1, cosp)


def count_of_neighbors(elems, player):
  # elems [Cell]
  res = 0
  for cell in elems:
    if cell.symbol_to_show() == player:
      res += 1
    else:
      res = 0
  return res

##  QUIXO PLAYER
##
time_millis = lambda: 1000 * timeit.default_timer()

class Quixo:
  def __init__(self, search_depth = 2, timeout = 50., heuristic = heuristic_1):
    self.game = Game()
    self.player = None
    self.timer_threshold = timeout
    self.search_depth = search_depth
    self.heuristic = heuristic
    self.time_left = None
  
  def set_player(self, player):
    self.player = player
  
  def playerPlay(self):
    if self.player == None: self.set_player('X')
    move_start = time_millis()
    # time_left represent the left time, calculating the passed time (time_millis() - move_start)
    time_left = lambda : self.timer_threshold - (time_millis() - move_start)

    focus, target = self.get_move(time_left)
    self.game.apply_move(self.player, (focus, target))
    return focus + 1, target + 1 # To support the standard order

  def oponentPlay(self, move):
    focus, target = move
    if self.player == None: self.set_player('O')

    oponent_player = 'X' if self.player == 'O' else 'O'

    if not (focus -1, target - 1) in self.game.all_valid_moves(oponent_player): raise Exception('Invalid move')

    self.game.apply_move(oponent_player, (focus - 1, target - 1)) # To support the standard order

  def is_time_over(self):
    if self.time_left() <= 0:
      raise SearchTimeout()

  def get_move(self, time_left):
    self.time_left = time_left
    best_move = self.game.all_valid_moves(self.player)[0]
    depth = 1
    try:
      while (depth <= self.search_depth):
        move = self.alphabeta(self.game, depth, self.player)
        best_move = move
        depth += 1
        if self.time_left() <= 0:
          return best_move
      return best_move

    except SearchTimeout:
      return best_move
  
  def alphabeta(self, game, depth, player, alpha = -inf, beta = inf):
    if player == 'X':
      legal_moves = game.all_valid_moves('X')
      if not legal_moves:
        return (-1, -1)
      best_current_move = legal_moves[0]
      for move in legal_moves:
        self.is_time_over()
        child = deepcopy(game)
        child.apply_move('X', move)
        score = self.max_value(child, depth - 1, alpha, beta)
        if score > alpha:
          alpha = score
          best_current_move = move
      return best_current_move
    else:
      legal_moves = game.all_valid_moves('O')
      if not legal_moves:
        return (-1, -1)
      best_current_move = legal_moves[0]
      for move in legal_moves:
        self.is_time_over()
        child = deepcopy(game)
        child.apply_move('O', move)
        score = self.min_value(child, depth - 1, alpha, beta)
        if score < beta:
          beta = score
          best_current_move = move
      return best_current_move

  def min_value(self, game, depth, alpha, beta):
    if depth == 0:
      return self.heuristic(game)
    legal_moves = game.all_valid_moves('X')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('X', move)
      score = self.max_value(child, depth - 1, alpha, beta)
      if score < beta:
        beta = score
        if beta <= alpha:
          break
    return beta

  def max_value(self, game, depth, alpha, beta):
    if depth == 0:
      return self.heuristic(game)
    legal_moves = game.all_valid_moves('O')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('O', move)
      score = self.min_value(child, depth - 1, alpha, beta)
      if score > alpha:
        alpha = score 
        if alpha >= beta:
          break       
    return alpha

class SearchTimeout(Exception):
  pass
