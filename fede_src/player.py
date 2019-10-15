from quixo import Quixo
from copy import deepcopy
import timeit
from math import inf
from copy import deepcopy
import random
from utils import to_simple_structure, count_of_neighbors

edges = [(0, 0), (0, 4), (4, 4), (4, 0)]

def random_heuristic(game, player, oponent):
  return random.random()

def count_of_tokens(game):
  res = (0, 0)
  for i_row in range(len(game.board)):
    for i_column in range(len(game.board[i_row])):
      value = game.board[i_row][i_column].symbol_to_show()
      if(value == 'O'):
        res = (res[0] + 1, res[1])

      if(value == 'X'):
        res = (res[0], res[1] + 1)
  return res

def count_of_edges(game, player):
  return sum(map(lambda pair: 1 if game.board[pair[0]][pair[1]].symbol_to_show() == player else 0, edges), 0)

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

def heuristic_1(game, player, oponent):
  player_index = 0 if player == 'O' else 1
  oponent_index = 1 if player_index == 0 else 0

  cot = count_of_tokens(game)
  count_of_tokens_value = (cot[player_index] - cot[oponent_index]) * 1.2 # I think that this value has 20% more importance
  coe = count_of_edges(game, player)
  center_importance = 16 * (1 if in_center(game, player) else 0)
  return count_of_tokens_value + center_importance + max_count_of_neighbors(game, player) * max(1, coe)


time_millis = lambda: 1000 * timeit.default_timer()

class QuixoPlayer:
  def __init__(self, search_depth = 3, timeout = 20., heuristic = heuristic_1):
    self.game = Quixo()
    self.player = None
    self.timer_threshold = timeout
    self.search_depth = search_depth
    self.heuristic = heuristic
    self.time_left = None
  
  def set_player(self, player):
    self.player = player
  
  def playerPlay(self):
    if self.player == None: self.set_player('O')
    move_start = time_millis()
    # time_left represent the left time, calculating the passed time (time_millis() - move_start)
    time_left = lambda : self.timer_threshold - (time_millis() - move_start)

    move = self.get_move(time_left)
    self.game.apply_move(self.player, move)
    return move

  def oponentPlay(self, move):
    if self.player == None: self.set_player('X')

    if move[0] == -1 or move[1] == -1: raise Exception('Invalid move')
    oponent_player = 'O' if self.player == 'X' else 'X'
    self.game.apply_move(oponent_player, move)

  def is_time_over(self):
    if self.time_left() <= 0:
      raise SearchTimeout()

  def get_move(self, time_left):
    self.time_left = time_left
    best_move = self.game.all_valid_moves(self.player)[0]
    depth = 1
    try:
      while (True):
        move = self.alphabeta(self.game, depth, self.player)
        best_move = move
        depth += 1
        if self.time_left() <= 0:
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
        score = self.min_value(child, depth - 1, alpha, beta)
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
        score = self.max_value(child, depth - 1, alpha, beta)
        if score < beta:
          beta = score
          best_current_move = move
      return best_current_move

  def min_value(self, game, depth, alpha, beta):
    if depth == 0:
      return self.heuristic(game, 'O', 'X')
    legal_moves = game.all_valid_moves('O')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('O', move)
      score = self.max_value(child, depth - 1, alpha, beta)
      if score < beta:
        beta = score 
        if beta <= alpha:
          break       
    return beta

  def max_value(self, game, depth, alpha, beta):
    if depth == 0:
      return self.heuristic(game, 'X', 'O')
    legal_moves = game.all_valid_moves('X')
    for move in legal_moves:
      self.is_time_over()
      child = deepcopy(game)
      child.apply_move('X', move)
      score = self.min_value(child, depth - 1, alpha, beta)
      if score > alpha:
        alpha = score 
        if alpha >= beta:
          break       
    return alpha

class SearchTimeout(Exception):
  pass


player1 = QuixoPlayer() #Player O
player2 = QuixoPlayer() #Player X
player1.game.show()
count_of_moves = 0
while(not player1.game.game_over()):
  player2.oponentPlay(player1.playerPlay())
  player1.oponentPlay(player2.playerPlay())
  count_of_moves += 1
  player1.game.show()

print('count_of_moves: ', count_of_moves)
